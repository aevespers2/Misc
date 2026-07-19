# Changelog

All notable product, architecture, implementation, documentation, release, and deployment changes are recorded here.

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
- 2026-07-19 — Expanded the architecture documentation with system-context, logical-component, runtime-sequence, trust-zone, failure-behavior, and authority-boundary diagrams.
- 2026-07-19 — Added repository-boundary documentation separating temporary incubation evidence from permanent package, baseline, credential, data, deployment, and release authority.
- 2026-07-19 — Added design contracts for authorization, collection, baselines, findings, output provenance, extensions, dashboards, response separation, reproducibility, and claims discipline.
- 2026-07-19 — Added a promotion/retirement decision model requiring a dedicated repository and owner before release work can proceed.

### Implementation

- Added package metadata for `xyz-firmware-defense` version `0.3.0`, with Python 3.11+ dependencies and `xyz` / `phantomblock` console entry points.
- Added source, unit tests, CI configuration, binary/SBOM and read-only image build scripts, example trusted-baseline configuration, and documentation assets.
- Added a GitHub Pages workflow that can publish documentation using `pages: write` and `id-token: write` permissions.
- No retained workflow status or exact-commit validation evidence was found for the reviewed release-planning head; configured workflows are not equivalent to passing release evidence.
- 2026-07-19 — No runtime, collector, heuristic, package, API, deployment, credential, networking, or target-mutation behavior changed in the documentation milestone.

### Documentation

- 2026-07-19 — Expanded the root README into a complete repository overview covering current status, incubation purpose, prototype inventory, safe local review, contribution boundary, and required architectural decision.
- 2026-07-19 — Rewrote the Pages landing page to distinguish implemented artifacts, configured workflows, local test evidence, proposals, and accepted evidence.
- 2026-07-19 — Added Pages-ready repository boundaries, design contracts, developer onboarding, and ownership/release guides.
- 2026-07-19 — Added `CONTRIBUTING.md` with documentation, evidence, security, and scope-control requirements.
- 2026-07-19 — Added `punchlist.md` with containment, ownership, validation, release, publication, and documentation-health gates.
- 2026-07-19 — Reorganized MkDocs navigation and added Mermaid diagram support.
- 2026-07-19 — Updated `taskchain.md`, `release.md`, and this changelog to record the documentation milestone without advancing implementation or release scope.

### Security and compliance

- Documentation restricts use to owned or explicitly authorized systems, describes dry-run isolation, and disclaims certification and comprehensive detection assurance.
- No repository license has been selected, representative hardware validation is absent, and compliance mappings are implementation-oriented preparation rather than CMMC status, STIG approval, Army authorization, or an Authority to Operate.
- Public documentation publication, privileged collection, firmware handling, management-plane access, PCAP data, extension loading, and switch-adapter behavior require explicit security, privacy, licensing, and operational review.
- 2026-07-19 — Strengthened warnings against real credentials, proprietary firmware, real incident data, unauthorized assessment, remote dashboard exposure, unreviewed extensions, and active response integrations.

### Release

- No package, image, service, deployment, certification, or production capability is approved from the current prototype.
- The first eligible decision is not a release: the Architect must approve a dedicated owning repository and migration plan or retire/archive the prototype.
- Release remains blocked on ownership, license, threat model, trusted-baseline provenance, representative and adversarial validation, reproducible CI, SBOM/checksums, security review, rollback, and explicit approval.
- 2026-07-19 — Classified the documentation foundation and repository punch list as partial review evidence; strict documentation build, accessibility/link review, and independent approval remain required.

### Deployment

- Automatic Pages publication was removed; the retained workflow is manual-only and fails closed unless `release.md` is explicitly marked `READY`.
- No operational scanner, live image, dashboard, switch isolation adapter, or external integration is authorized for deployment.
- 2026-07-19 — Documentation changes did not alter the fail-closed Pages workflow or authorize a deployment.

## Entry format

- Date
- Category: Product / Architecture / Added / Changed / Fixed / Security / Release / Deployment / Documentation
- Summary
- Evidence: issue, PR, commit, workflow, artifact, or deployment record
- Impact and migration notes where applicable
