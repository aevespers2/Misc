# XYZ

## Trusted assessment below the operating system

XYZ is a defensive firmware-integrity, hardware-anomaly, and network-isolation platform for situations where the host operating system cannot be treated as the root of trust.

It boots from a read-only Linux environment, inventories hardware and firmware, compares readable artifacts against independently maintained baselines, inspects kernel evidence, detects exposed out-of-band management interfaces, analyzes network traffic captured outside the target OS, and prepares controlled isolation actions.

## What XYZ is for

XYZ supports authorized defenders investigating suspected persistence or covert communications involving:

- BIOS and UEFI firmware;
- network-interface firmware;
- baseboard management controllers;
- Intel AMT, IPMI, Redfish, and related management planes;
- storage controllers and SSD firmware;
- chipset and PCI-device anomalies;
- kernel hooks, unsigned modules, taint, or suspicious low-level indicators;
- network traffic that may not be visible to the host operating system.

## Evidence before conclusions

XYZ does not label a system compromised from one mismatch, open port, or heuristic. It records evidence, assigns conservative severity, preserves machine-readable output, and distinguishes **clean**, **investigate**, and corroborated **compromised** states.

## Primary workflow

1. Build or obtain an approved XYZ live image.
2. Verify its signature and checksum.
3. Boot the target system from trusted read-only media.
4. Load a protected known-good firmware manifest.
5. Run the hardware, firmware, kernel, and management-plane assessment.
6. Analyze traffic from a TAP, SPAN, or mirror port when available.
7. Review the report and supporting evidence.
8. Use the isolation workflow only after authorization and human review.

## Safety boundary

XYZ does not exploit devices, bypass authentication, flash firmware, or disable switch ports by default. Disruptive integrations are separated from passive extensions and remain dry-run until explicitly reviewed and configured.

## Project status

XYZ is currently a research and laboratory-evaluation platform. It is being prepared for disciplined technical review and future NIST, DoD RMF, DISA STIG/SRG, and Army authorization workflows, but the repository does not claim certification, approval, or an Authority to Operate.
