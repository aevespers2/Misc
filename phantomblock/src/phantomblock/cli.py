from __future__ import annotations

import argparse
from pathlib import Path

import uvicorn

from .core import collect_report, inspect_pcap, write_json
from .dashboard import create_app
from .isolation import DryRunSwitchAdapter


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="xyz",
        description="XYZ defensive firmware, hardware, and out-of-band assessment platform",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    collect = sub.add_parser("collect", help="Collect trusted-environment hardware and kernel evidence")
    collect.add_argument("--manifest", type=Path)
    collect.add_argument("--oob-host", action="append", dest="oob_hosts")
    collect.add_argument("--output", type=Path, default=Path("state/report.json"))

    pcap = sub.add_parser("inspect-pcap", help="Inspect a PCAP captured from a TAP or mirror port")
    pcap.add_argument("pcap", type=Path)
    pcap.add_argument("--output", type=Path, default=Path("state/pcap-report.json"))

    dash = sub.add_parser("dashboard", help="Serve the XYZ fleet reporting dashboard")
    dash.add_argument("--state-dir", type=Path, default=Path("state"))
    dash.add_argument("--host", default="127.0.0.1")
    dash.add_argument("--port", type=int, default=8080)

    isolate = sub.add_parser("isolate", help="Create a switch-port isolation dry run")
    isolate.add_argument("device")
    isolate.add_argument("port")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    if args.command == "collect":
        report = collect_report(args.manifest, args.oob_hosts)
        write_json(args.output, report.to_dict())
        print(args.output)
    elif args.command == "inspect-pcap":
        write_json(args.output, inspect_pcap(args.pcap))
        print(args.output)
    elif args.command == "dashboard":
        uvicorn.run(create_app(args.state_dir), host=args.host, port=args.port)
    elif args.command == "isolate":
        print(DryRunSwitchAdapter().isolate(args.device, args.port).to_dict())


if __name__ == "__main__":
    main()
