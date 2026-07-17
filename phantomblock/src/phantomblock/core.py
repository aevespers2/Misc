from __future__ import annotations

import hashlib
import json
import os
import re
import socket
import subprocess
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml


def _run(*cmd: str, timeout: int = 20) -> dict[str, Any]:
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, check=False)
        return {"command": list(cmd), "returncode": proc.returncode,
                "stdout": proc.stdout.strip(), "stderr": proc.stderr.strip()}
    except (FileNotFoundError, subprocess.TimeoutExpired) as exc:
        return {"command": list(cmd), "error": str(exc)}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


@dataclass
class Finding:
    check: str
    severity: str
    summary: str
    evidence: dict[str, Any] = field(default_factory=dict)


@dataclass
class HostReport:
    host: str
    collected_at: str
    inventory: dict[str, Any]
    findings: list[Finding]
    status: str

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        return data


def collect_inventory() -> dict[str, Any]:
    commands = {
        "pci": ("lspci", "-nnvv"),
        "firmware": ("fwupdmgr", "get-devices", "--json"),
        "dmi": ("dmidecode", "--type", "bios", "--type", "system", "--type", "baseboard"),
        "cpu": ("lscpu", "--json"),
        "block": ("lsblk", "--json", "-O"),
        "network": ("ip", "-json", "link"),
        "modules": ("lsmod",),
    }
    return {name: _run(*cmd) for name, cmd in commands.items()}


def verify_manifest(manifest_path: Path | None) -> list[Finding]:
    if manifest_path is None:
        return [Finding("firmware_manifest", "info", "No trusted manifest supplied")]
    manifest = yaml.safe_load(manifest_path.read_text()) or {}
    findings: list[Finding] = []
    for item in manifest.get("artifacts", []):
        path = Path(item["path"])
        expected = str(item["sha256"]).lower()
        if not path.exists():
            findings.append(Finding("firmware_hash", "medium", f"Artifact unavailable: {path}"))
            continue
        actual = sha256_file(path)
        severity = "clean" if actual == expected else "high"
        summary = "Trusted artifact hash matched" if actual == expected else "Trusted artifact hash mismatch"
        findings.append(Finding("firmware_hash", severity, summary,
                                {"path": str(path), "expected": expected, "actual": actual}))
    return findings


def scan_kernel() -> list[Finding]:
    findings: list[Finding] = []
    taint = Path("/proc/sys/kernel/tainted")
    if taint.exists():
        value = taint.read_text().strip()
        findings.append(Finding("kernel_taint", "clean" if value == "0" else "medium",
                                f"Kernel taint value: {value}"))
    kallsyms = Path("/proc/kallsyms")
    if kallsyms.exists() and os.access(kallsyms, os.R_OK):
        text = kallsyms.read_text(errors="replace")
        syscall_symbols = re.findall(r"^[0-9a-fA-F]+\s+\w\s+(__x64_sys_\w+|sys_call_table)$", text, re.M)
        findings.append(Finding("syscall_symbols", "clean" if syscall_symbols else "medium",
                                f"Observed {len(syscall_symbols)} syscall-related symbols"))
    modules = _run("dmesg", "--level=alert,crit,err,warn")
    suspicious = [line for line in modules.get("stdout", "").splitlines()
                  if re.search(r"rootkit|hook|taint|unsigned module|verification failed", line, re.I)]
    findings.append(Finding("kernel_log", "high" if suspicious else "clean",
                            "Suspicious kernel log indicators found" if suspicious else "No selected kernel log indicators",
                            {"matches": suspicious[:50]}))
    return findings


def detect_oob(hosts: list[str] | None = None) -> list[Finding]:
    hosts = hosts or ["127.0.0.1"]
    ports = {16992: "Intel AMT HTTP", 16993: "Intel AMT HTTPS", 623: "IPMI/RMCP", 443: "Redfish/HTTPS"}
    findings: list[Finding] = []
    for host in hosts:
        for port, label in ports.items():
            sock = socket.socket()
            sock.settimeout(0.35)
            try:
                opened = sock.connect_ex((host, port)) == 0
            finally:
                sock.close()
            if opened:
                findings.append(Finding("oob_interface", "medium", f"Reachable {label}", {"host": host, "port": port}))
    if not findings:
        findings.append(Finding("oob_interface", "clean", "No selected management ports reachable on requested hosts"))
    return findings


def inspect_pcap(path: Path) -> dict[str, Any]:
    from scapy.all import IP, IPv6, TCP, UDP, rdpcap
    packets = rdpcap(str(path))
    flows: dict[str, int] = {}
    management_hits: list[dict[str, Any]] = []
    watched = {623: "IPMI", 16992: "AMT", 16993: "AMT-TLS", 443: "HTTPS/possible Redfish"}
    for packet in packets:
        if IP in packet:
            src, dst = packet[IP].src, packet[IP].dst
        elif IPv6 in packet:
            src, dst = packet[IPv6].src, packet[IPv6].dst
        else:
            continue
        sport = dport = 0
        proto = "other"
        if TCP in packet:
            sport, dport, proto = packet[TCP].sport, packet[TCP].dport, "tcp"
        elif UDP in packet:
            sport, dport, proto = packet[UDP].sport, packet[UDP].dport, "udp"
        key = f"{src}:{sport}>{dst}:{dport}/{proto}"
        flows[key] = flows.get(key, 0) + 1
        if sport in watched or dport in watched:
            management_hits.append({"flow": key, "service": watched.get(dport) or watched.get(sport)})
    return {"pcap": str(path), "packets": len(packets), "flows": flows,
            "management_plane_hits": management_hits[:500]}


def collect_report(manifest: Path | None = None, oob_hosts: list[str] | None = None) -> HostReport:
    findings = verify_manifest(manifest) + scan_kernel() + detect_oob(oob_hosts)
    rank = {"clean": 0, "info": 0, "low": 1, "medium": 2, "high": 3, "critical": 4}
    max_rank = max((rank.get(f.severity, 0) for f in findings), default=0)
    status = "compromised" if max_rank >= 4 else "investigate" if max_rank >= 2 else "clean"
    return HostReport(socket.gethostname(), datetime.now(timezone.utc).isoformat(), collect_inventory(), findings, status)


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
