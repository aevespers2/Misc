# XYZ

**XYZ** is an advanced defensive firmware-integrity, hardware-anomaly, and network-isolation platform designed to assess systems from a trusted environment that does not depend on the host operating system.

XYZ exists because sophisticated implants can persist below the operating system in BIOS/UEFI, NIC firmware, BMCs, storage controllers, SSD firmware, management engines, and other privileged hardware components. Traditional endpoint tooling may not see those layers, so XYZ collects evidence from a read-only Linux environment, validates firmware artifacts, inspects kernel state, detects exposed out-of-band management channels, analyzes externally captured traffic, and prepares controlled isolation actions.

> **Authorized defensive use only.** XYZ is intended for systems you own or are explicitly authorized to assess. It does not exploit management interfaces, bypass credentials, flash firmware, or disable switch ports by default.

## Why XYZ Was Built

Modern defensive tools usually assume the operating system and its telemetry can be trusted. XYZ begins from the opposite assumption: when firmware or hardware-level persistence is suspected, the host OS may be incomplete, misleading, or compromised. The project therefore uses a trusted boot environment, evidence-first collection, independently sourced firmware manifests, conservative verdict logic, and externally observed network traffic.

The goal is not to declare compromise from a single anomaly. XYZ separates evidence collection from decision policy and reports uncertain findings as **investigate** until corroborated.

## Core Capabilities

- Bootable read-only Linux scanner with volatile runtime state.
- Hardware fingerprinting for PCI devices, chipset data, DMI, CPU, storage, NICs, modules, and firmware inventory.
- Firmware integrity validation for readable BIOS/UEFI, NIC, BMC, SSD, and vendor firmware artifacts against trusted SHA-256 manifests.
- Linux kernel anomaly checks for taint, suspicious log indicators, syscall-related symbol visibility, and module anomalies.
- Out-of-band channel detection for Intel AMT, IPMI/RMCP, Redfish, and related management-plane exposure.
- Offline PCAP inspection for traffic captured from a TAP, SPAN, or switch mirror port outside the target OS.
- Guarded switch-port isolation abstraction that remains dry-run until a reviewed vendor adapter is configured.
- Fleet reporting dashboard and JSON API.
- Stable extension API for passive collectors, verifiers, detectors, analyzers, and report enrichers.
- Standalone Linux binary build with checksum and CycloneDX SBOM generation.
- Initial NIST, DoD RMF, DISA STIG/SRG, SSDF, and Army authorization-preparation mappings.

## What XYZ Looks For

XYZ is designed to surface evidence such as:

- unexpected or changed firmware hashes;
- undocumented hardware, PCI devices, controllers, or firmware revisions;
- exposed AMT, IPMI, Redfish, or other management interfaces;
- suspicious kernel taint, unsigned-module indicators, hook-related log evidence, or missing expected symbols;
- management-plane traffic visible outside the host OS;
- mismatch between observed hardware state and an approved baseline;
- systems that should be isolated pending investigation.

A finding is evidence requiring interpretation. It is not automatically proof of a nation-state implant, malware family, or compromise.

## Project Structure

```text
phantomblock/
├── src/phantomblock/       # Core engine and extension framework
├── image/                  # Read-only live-image definition
├── config/                 # Trusted firmware manifest examples
├── packaging/              # Standalone binary and SBOM build
├── compliance/             # Control mappings and authorization preparation
├── docs/                   # GitHub Pages documentation
├── tests/                  # Automated tests
└── pyproject.toml          # Package and tool configuration
```

The internal Python package remains `phantomblock` for compatibility, while the product and command-line interface are branded **XYZ**.

## Quick Start

### Install from source

```bash
cd phantomblock
python -m venv .venv
. .venv/bin/activate
python -m pip install -e '.[dev]'
xyz collect --output state/report.json
xyz dashboard --state-dir state
```

Open `http://127.0.0.1:8080`.

### Build the standalone binary

```bash
cd phantomblock
./packaging/build-binary.sh
```

Expected outputs:

```text
dist/xyz
dist/xyz.sha256
dist/xyz.cdx.json
```

### Build the read-only live image

```bash
cd phantomblock
sudo ./image/build.sh
```

The image definition uses a read-only root with a volatile runtime overlay. Secure Boot, image signing, measured boot, and platform-specific boot policy must be validated before operational deployment.

## Trusted Firmware Database

Copy `config/known_good.example.yml` to protected storage and populate it only from independently verified vendor releases or an approved organizational baseline.

```bash
xyz collect \
  --manifest /secure/baselines/known-good.yml \
  --output state/report.json
```

Never generate the trusted baseline from the machine being assessed.

## External Network Inspection

Capture traffic from a TAP, SPAN, or mirror port and analyze it on the trusted XYZ station:

```bash
xyz inspect-pcap capture.pcap --output state/pcap-report.json
```

## Isolation

```bash
xyz isolate switch-01 Gi1/0/7
```

The default adapter performs a dry run only. Production isolation requires an authenticated, allowlisted, auditable, vendor-specific adapter with rollback verification and operator approval.

## Extension Model

XYZ uses a versioned capability API. Extensions can add passive inventory, verification, detection, traffic analysis, or reporting functions without changing the core engine. General extensions are prohibited from mutating the target. Active response functions remain isolated behind separate guarded interfaces.

## Security Model

XYZ follows these principles:

1. Do not trust the host OS when assessing below-OS persistence.
2. Separate evidence collection from verdict policy.
3. Never treat one heuristic as proof of compromise.
4. Default all disruptive actions to dry-run.
5. Require independently verified firmware baselines.
6. Preserve evidence provenance and machine-readable reports.
7. Keep extensions passive unless explicitly reviewed and isolated.
8. Produce SBOMs, checksums, test evidence, and release artifacts.

## Compliance and DoD/Army Preparation

The repository includes implementation-oriented preparation for:

- NIST SP 800-53 Rev. 5;
- NIST SP 800-53A assessment procedures;
- NIST SP 800-171 Rev. 3 and SP 800-171A Rev. 3;
- NIST SP 800-218 SSDF;
- DoD Risk Management Framework;
- applicable DISA Application Security and Development STIG/SRG requirements;
- Army overlays, mission-owner requirements, and eMASS/ATO evidence packages.

These mappings are not certification, CMMC status, STIG approval, Army authorization, or an Authority to Operate. Formal deployment requires system categorization, control tailoring, FIPS analysis, threat modeling, data-flow documentation, vulnerability management, signed provenance, approved cryptographic modules where applicable, STIG checklist evidence, representative hardware testing, incident-response procedures, configuration management, POA&M tracking, and assessment by the responsible authorizing organization.

## Current Maturity

XYZ is suitable for:

- architecture review;
- laboratory evaluation;
- defensive research;
- prototype demonstrations;
- development of organization-specific collectors and switch adapters.

It is not yet represented as a certified operational security product.

## Validation Roadmap

- representative BIOS/UEFI, NIC, BMC, and SSD test matrix;
- reproducible and signed release pipeline;
- SLSA-style provenance;
- dependency and container scanning;
- fuzz testing for parsers and manifest ingestion;
- negative and adversarial test corpus;
- Secure Boot and measured-boot validation;
- hardware-lab false-positive and false-negative characterization;
- formal STIG checklist and RMF evidence package;
- performance benchmarks for large PCAPs and fleet reporting.

## Documentation

The GitHub Pages site is built from `docs/` using MkDocs and the workflow in `.github/workflows/pages.yml`.

## Responsible Disclosure

Do not publish sensitive findings, credentials, customer data, firmware images, or exploit details in public issues. Security reports should include affected version, environment, reproducible evidence, impact, and a safe method of contact.

## License

No license has yet been selected. Until a license is added, normal copyright restrictions apply.

## Disclaimer

XYZ is a defensive research and assessment platform. It does not guarantee detection of all firmware implants, hardware backdoors, covert channels, or compromised systems. Results depend on trusted baselines, platform visibility, hardware support, collection privileges, and analyst interpretation.
