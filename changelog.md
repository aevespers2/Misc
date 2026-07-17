# Changelog

All notable product, architecture, implementation, release, and deployment changes are recorded here.

## Unreleased

### Product
- 2026-07-16 — Initialized `Misc` as an incubation repository for experimental security, verification, and systems proposals.
- 2026-07-16 — Defined the first objective as approving an intake, evidence, promotion, and retirement contract before accepting implementation.
- 2026-07-16 — Assigned the repository a holding/incubation priority that does not supersede active P0 work in established repositories.
- 2026-07-16 — Detected that fifteen later commits added an XYZ defensive firmware-assessment prototype before the incubation contract or experiment classification was approved.
- 2026-07-16 — Preserved XYZ as unaccepted prototype evidence and changed the immediate local objective to containment, ownership review, and either migration to a dedicated repository or retirement. Portfolio priority remains P4.

### Architecture
- Experiments must remain non-authoritative, isolated, bounded, reversible, and mapped against existing repository ownership before work begins.
- Successful experiments must migrate to a dedicated approved owner; rejected or inconclusive work must retain provenance and limitations when archived.
- XYZ currently resides under `phantomblock/` and includes a Python package, CLI, dashboard/API, passive assessment logic, extension interface, dry-run isolation abstraction, live-image and binary-build definitions, tests, compliance mappings, and documentation.
- Code and configuration demonstrate a prototype shape only; supported hardware, trusted firmware provenance, detection accuracy, isolation safety, operational security, and authorization readiness remain unverified.

### Implementation
- Added package metadata for `xyz-firmware-defense` version `0.3.0`, with Python 3.11+ dependencies and `xyz`/`phantomblock` console entry points.
- Added source, unit tests, CI configuration, binary/SBOM and read-only image build scripts, example trusted-baseline configuration, and documentation assets.
- Added a GitHub Pages workflow that can publish documentation from `main` using `pages: write` and `id-token: write` permissions.
- No retained workflow status or exact-commit validation evidence was found for the reviewed head; configured workflows are not equivalent to passing release evidence.

### Security and compliance
- Documentation restricts use to owned or explicitly authorized systems, describes dry-run isolation, and disclaims certification and comprehensive detection assurance.
- No repository license has been selected, representative hardware validation is absent, and the compliance mappings are implementation-oriented preparation rather than CMMC status, STIG approval, Army authorization, or an Authority to Operate.
- Public documentation publication, privileged collection, firmware handling, management-plane access, PCAP data, extension loading, and switch-adapter behavior require explicit security, privacy, licensing, and operational review.

### Release
- No package, image, service, deployment, certification, or production capability is approved from the current prototype.
- The first eligible decision is not a release: the Architect must approve a dedicated owning repository and migration plan or retire/archive the prototype.
- Release remains blocked on ownership, license, threat model, trusted-baseline provenance, representative and adversarial validation, reproducible CI, SBOM/checksums, security review, rollback, and explicit approval.

### Deployment
- Automatic Pages publication is a configured deployment surface and conflicts with the original no-deployment incubation boundary until explicitly approved or disabled.
- No operational scanner, live image, dashboard, switch isolation adapter, or external integration is authorized for deployment.

## Entry Format
- Date
- Category: Product / Architecture / Added / Changed / Fixed / Security / Release / Deployment
- Summary
- Evidence: issue, PR, commit, workflow, artifact, or deployment record
- Impact and migration notes where applicable
