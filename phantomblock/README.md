# PhantomBlock MVP

PhantomBlock is a defensive, evidence-first toolkit for assessing firmware, hardware inventory, kernel integrity, management-plane exposure, and externally captured network traffic from a trusted Linux environment.

## MVP capabilities

- Reproducible read-only live image definition using `mkosi`.
- PCI, DMI, CPU, block-device, NIC, and firmware inventory collection.
- Hash-manifest validation for readable firmware artifacts and vendor evidence records.
- Linux kernel anomaly checks for syscall-table indicators, module taint, writable executable mappings, and suspicious hooks exposed by trusted tooling.
- AMT, IPMI, and Redfish exposure detection without authentication bypass attempts.
- Offline PCAP inspection intended for mirror/SPAN/TAP captures outside the target OS.
- Switch-isolation abstraction with a safe dry-run adapter; no port is changed unless explicitly enabled and configured.
- FastAPI dashboard/API showing host status and evidence.

## Safety model

PhantomBlock is defensive. It does not flash firmware, exploit management interfaces, bypass credentials, or modify switch ports by default. Firmware verdicts are only as strong as the supplied trusted manifest and vendor evidence. A mismatch is reported as `investigate`, not automatically declared malicious.

## Quick start

```bash
cd phantomblock
python -m venv .venv
. .venv/bin/activate
pip install -e '.[dev]'
phantomblock collect --output state/report.json
phantomblock dashboard --state-dir state
```

Open `http://127.0.0.1:8080`.

## Trusted hash database

Copy `config/known_good.example.yml` to a protected location, populate it from independently verified vendor releases, and pass it with `--manifest`. Never generate the trusted manifest from the machine being assessed.

## Live image

Install `mkosi`, then run:

```bash
sudo ./image/build.sh
```

The generated image uses a read-only root with a volatile runtime overlay. Validate Secure Boot and signing requirements for your deployment before field use.

## External network inspection

Capture traffic on a network TAP or switch mirror port and copy the PCAP to the analysis station:

```bash
phantomblock inspect-pcap capture.pcap --output state/pcap-report.json
```

## Isolation

The MVP emits a proposed isolation action in dry-run mode. Real switch integration must be implemented through an authenticated adapter with allowlisted devices, ports, change logging, and a tested rollback path.
