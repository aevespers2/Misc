# Changelog

All notable product, architecture, implementation, release, and deployment changes are recorded here.

## Unreleased

### Product

- 2026-07-16 — Initialized `Misc` as an incubation repository for experimental security, verification, and systems proposals.
- 2026-07-16 — Defined the first objective as approving an intake, evidence, promotion, and retirement contract before accepting implementation.
- 2026-07-16 — Assigned the repository a holding/incubation priority that does not supersede active P0 work in established repositories.
- 2026-07-16 — Detected that later commits added an XYZ defensive firmware-assessment prototype before the incubation contract or experiment classification was approved.
- 2026-07-16 — Preserved XYZ as unaccepted prototype evidence and changed the immediate local objective to containment, ownership review, and either migration to a dedicated repository, retirement, or continued hold. Portfolio priority remains P4.
- 2026-07-23 — Added a repository and documentation front door that clearly separates preserved implementation, configured automation, historical validation, proposals, missing evidence, and blocked authority.

### Architecture

- Experiments must remain non-authoritative, isolated, bounded, reversible, and mapped against existing repository ownership before work begins.
- Successful experiments must migrate to a dedicated approved owner; rejected or inconclusive work must retain provenance and limitations when archived.
- XYZ currently resides under `phantomblock/` and includes a Python package, CLI, dashboard/API, passive assessment logic, extension interface, dry-run isolation abstraction, live-image and binary-build definitions, tests, compliance mappings, and documentation.
- Code and configuration demonstrate a prototype shape only; supported hardware, trusted firmware provenance, detection accuracy, isolation safety, operational security, and authorization readiness remain unverified.
- 2026-07-23 — Added accessible system-context and incubation-lifecycle diagrams with equivalent prose, explicit trust and ownership vacancies, interface-documentation requirements, and fail-closed obstruction conditions.

### Documentation

- 2026-07-23 — Added `phantomblock/docs/incubation-status.md`, clarifying evidence classes, source precedence, controlled changes, and the migrate/retire/hold decision.
- 2026-07-23 — Added `phantomblock/docs/onboarding.md` with authorization, privacy, sensitive-data, non-deployment, reproducibility, and first-contribution safeguards.
- 2026-07-23 — Added `phantomblock/docs/developer-guide.md` with change classes, architecture rules, interface-documentation requirements, evidence expectations, pull-request checks, migration, and retirement guidance.
- 2026-07-23 — Added `punchlist.md` and synchronized the README, MkDocs navigation, task chain, release plan, and changelog.

### Implementation

- Added package metadata for `xyz-firmware-defense` version `0.3.0`, with Python 3.11+ dependencies and `xyz`/`phantomblock` console entry points.
- Added source, unit tests, CI configuration, binary/SBOM and read-only image build scripts, example trusted-baseline configuration, and documentation assets.
- Added a GitHub Pages workflow. Automatic publication was later removed; the workflow is manual-only and fails closed unless `release.md` is explicitly `READY`.
- No current release-candidate validation, supported-platform evidence, or operational approval is established by this documentation change.

### Security and compliance

- Documentation restricts use to owned or explicitly authorized systems, describes dry-run isolation, and disclaims certification and comprehensive detection assurance.
- No repository license has been selected, representative hardware validation is absent, and the compliance mappings are implementation-oriented preparation rather than CMMC status, STIG approval, Army authorization, or an Authority to Operate.
- Public documentation publication, privileged collection, firmware handling, management-plane access, PCAP data, extension loading, and switch-adapter behavior require explicit security, privacy, licensing, and operational review.
- 2026-07-23 — Strengthened public guidance against credentials, proprietary firmware, sensitive packet captures, customer data, private findings, and production evidence in Git, CI, Pages, issues, or public artifacts.

### Validation

- 2026-07-23 — Added deterministic documentation-structure, internal-link, planning-alignment, diagram-alternative, authority-boundary, and workflow-permission checks with hostile regressions.
- 2026-07-23 — Extended the documentation workflow to validate exact `main` heads after relevant merges, while preserving read-only permissions, pinned Actions, non-persistent credentials, retained evidence, and the manual-only Pages boundary.
- Documentation validation establishes structural consistency only; it does not validate detection, hardware support, security, release, publication, or operational capability.

### Release

- No package, image, service, deployment, certification, or production capability is approved from the current prototype.
- The first eligible decision is not a release: the Architect must approve a dedicated owning repository and migration plan, retirement/archive, or continued hold.
- Release remains blocked on ownership, license, threat model, trusted-baseline provenance, representative and adversarial validation, reproducible CI, SBOM/checksums, security review, correction propagation, rollback, and explicit approval.
- 2026-07-23 — Confirmed that the documentation milestone does not change the blocked release or publication status.

### Deployment

- Pages publication remains manual-only and fail-closed until the release plan is explicitly marked `READY`.
- No operational scanner, live image, dashboard, switch isolation adapter, or external integration is authorized for deployment.

## Entry format

- Date
- Category: Product / Architecture / Documentation / Added / Changed / Fixed / Security / Validation / Release / Deployment
- Summary
- Evidence: issue, PR, commit, workflow, artifact, or deployment record
- Impact and migration notes where applicable
