# XYZ / PhantomBlock

## Preserved defensive research prototype

XYZ is an implemented prototype for defensive firmware-integrity, hardware-anomaly, and external network-evidence assessment. It is preserved inside the portfolio’s `Misc` incubation repository while ownership, licensing, validation, publication, migration, retirement, and rollback decisions remain unresolved.

**Current status:** prototype code and documentation exist; release, deployment, certification, and operational authority are blocked.

## Choose a route

- New reviewer: read [Incubation Status](incubation-status.md).
- New contributor: begin with [Safe Onboarding](onboarding.md).
- Architecture reviewer: inspect [Architecture and Trust Boundaries](architecture.md) and the [Threat Model](threat-model.md).
- Developer: follow the [Developer Guide](developer-guide.md) and [Validation Roadmap](validation.md).
- Release or publication reviewer: read the repository-level `release.md` and `punchlist.md` before considering any workflow or artifact.

## Intended defensive use

The prototype explores evidence collection and conservative assessment for authorized defenders investigating possible persistence or covert communication involving:

- BIOS and UEFI firmware;
- network-interface firmware;
- baseboard management controllers;
- AMT, IPMI, Redfish, and related management planes;
- storage controllers and SSD firmware;
- chipset and PCI-device anomalies;
- kernel hooks, unsigned modules, taint, or suspicious low-level indicators;
- traffic observed outside the target operating system.

These are research targets, not a supported-platform or detection-coverage claim.

## Evidence before conclusions

XYZ must not label a system compromised from one mismatch, open port, or heuristic. Collection records observations; policy assigns conservative severity; human review and corroborating evidence determine any conclusion. A clean local test run cannot establish trusted firmware, detection accuracy, safe isolation, or operational readiness.

## Conceptual workflow

```mermaid
flowchart TD
    A[Approved laboratory scope] --> B[Trusted external environment]
    B --> C[Passive inventory and evidence collection]
    C --> D[Protected baseline comparison]
    C --> E[External packet-capture analysis]
    D --> F[Versioned report]
    E --> F
    F --> G[Human review and corroboration]
    G --> H{Authorized disposition}
    H -->|Investigate| I[Additional evidence]
    H -->|No supported conclusion| J[Record uncertainty]
    H -->|Response separately approved| K[Dry-run-first response boundary]
```

**Equivalent prose:** Work begins only within an approved laboratory scope and a trusted environment outside the target operating system. Passive inventory and evidence collection may feed protected-baseline comparison and external packet analysis. Both produce a versioned report for human review and corroboration. The reviewer may request more evidence, record that no supported conclusion exists, or—under separate authorization—enter a dry-run-first response process.

## Safety boundary

XYZ does not authorize exploitation, authentication bypass, firmware flashing, production isolation, unrestricted scanning, or use against third-party systems. Disruptive integrations remain separate from passive collection and require explicit approval, authentication, allowlists, auditability, idempotency, and verified rollback.

Do not publish credentials, customer data, proprietary firmware, sensitive packet captures, private findings, or production evidence in Git, CI, Pages, issues, or public artifacts.

## What remains unresolved

- permanent repository and owner;
- license and third-party data rights;
- exact supported and unsupported platform matrix;
- trusted-baseline governance and key custody;
- representative and adversarial validation;
- false-positive and false-negative characterization;
- privacy, security, disclosure, retention, and incident procedures;
- package, image, Pages, and release approval;
- migration or retirement procedure and rollback evidence.

The repository does not claim certification, CMMC status, STIG approval, Army authorization, or an Authority to Operate.
