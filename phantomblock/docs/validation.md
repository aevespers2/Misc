# Validation Roadmap

XYZ must be validated as a security assessment instrument, not merely shown to execute successfully.

## Automated validation

- unit tests for hashing, manifests, policy, reporting, and isolation guards;
- schema compatibility tests;
- CLI integration tests;
- malformed manifest and PCAP test corpora;
- parser fuzzing;
- dependency and secret scanning;
- static analysis and type checking;
- deterministic binary and documentation builds.

## Hardware laboratory matrix

Test representative systems across:

- Intel and AMD platforms;
- legacy BIOS and multiple UEFI implementations;
- common NIC vendors and firmware families;
- BMC platforms exposing IPMI and Redfish;
- SATA, NVMe, RAID, and storage-controller combinations;
- physical servers, workstations, laptops, and virtualized environments;
- Secure Boot enabled and disabled configurations.

## Detection characterization

For each detector, document expected evidence, known limitations, false-positive conditions, false-negative risks, required privileges, collection duration, and supported platforms. Tests should include approved firmware, deliberately altered laboratory artifacts, unavailable firmware regions, exposed management interfaces, and clean systems with unusual but legitimate configurations.

## Supply-chain validation

Release validation should include signed source tags, reproducible builds, SBOM generation, provenance attestations, dependency review, vulnerability scanning, checksum publication, artifact signing, and independent installation verification.

## Operational evaluation

Before production deployment, conduct tabletop exercises and controlled scenarios covering evidence acquisition, analyst review, escalation, isolation approval, rollback, incident response, report retention, and recovery from scanner-media compromise.

## Acceptance criteria

A release should not be described as operationally ready until its supported hardware, detection confidence, performance, security controls, deployment assumptions, known limitations, and authorization evidence are documented and independently reviewed.
