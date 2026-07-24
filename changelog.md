# Changelog

All notable product, architecture, implementation, documentation, release, and deployment changes are recorded here.

## Unreleased

### Product

- 2026-07-16 — Initialized `Misc` as an incubation repository for experimental security, verification, and systems proposals.
- 2026-07-16 — Defined the first objective as approving an intake, evidence, promotion, and retirement contract before accepting implementation.
- 2026-07-16 — Assigned the repository a holding/incubation priority that does not supersede active P0 work in established repositories.
- 2026-07-16 — Detected that fifteen later commits added an XYZ defensive firmware-assessment prototype before the incubation contract or experiment classification was approved.
- 2026-07-16 — Preserved XYZ as unaccepted prototype evidence and changed the immediate local objective to containment, ownership review, and either migration to a dedicated repository or retirement. Portfolio priority remains P4.
- 2026-07-20 — Proposed the lowest-overlap retained role as a specialist host-firmware, kernel, management-plane, and offline-PCAP observation adapter beneath Repository `0`, with Repository `1` retaining device-baseline, capability, revocation, canonical-receipt, and recovery authority. This is not an approved product or integration decision.
- 2026-07-20 — Added three explicit disposition options: dedicated PhantomBlock adapter, approved modular consolidation with JusticeForMe, or evidence-preserving retirement/archive.
- 2026-07-24 — Added explicit `REMAIN_IN_INCUBATION` as a fail-closed fourth disposition when no owner, destination, consolidation, or retirement decision is approved.

### Architecture

- Experiments must remain non-authoritative, isolated, bounded, reversible, and mapped against existing repository ownership before work begins.
- Successful experiments must migrate to a dedicated approved owner; rejected or inconclusive work must retain provenance and limitations when archived.
- XYZ currently resides under `phantomblock/` and includes a Python package, CLI, dashboard/API, passive assessment logic, extension interface, dry-run isolation abstraction, live-image and binary-build definitions, tests, compliance mappings, and documentation.
- Code and configuration demonstrate a prototype shape only; supported hardware, trusted firmware provenance, detection accuracy, isolation safety, operational security, and authorization readiness remain unverified.
- 2026-07-19 — Expanded the architecture documentation with system-context, logical-component, runtime-sequence, trust-zone, failure-behavior, and authority-boundary diagrams.
- 2026-07-19 — Added repository-boundary documentation separating temporary incubation evidence from permanent package, baseline, credential, data, deployment, and release authority.
- 2026-07-19 — Added design contracts for authorization, collection, baselines, findings, output provenance, extensions, dashboards, response separation, reproducibility, and claims discipline.
- 2026-07-19 — Added a promotion/retirement decision model requiring a dedicated repository and owner before release work can proceed.
- 2026-07-20 — Added an obstruction and gluing ledger covering eighteen identity, ownership, device, baseline, evidence, freshness, artifact-binding, result, authority, credential, network, privacy, extension, platform, temporal, incident, publication, and rollback incompatibilities.
- 2026-07-20 — Added pairwise contract edges and triple-overlap witnesses across device → PhantomBlock → Repository `0`, Repository `0` → Repository `1` → response adapter, PhantomBlock → Bridge → review interface, and incident authority → Repository `1` → downstream consumers.
- 2026-07-20 — Added a proposed host-observation envelope minimum without changing current package output or claiming a trusted signing system.
- 2026-07-20 — Added a portable first-install mapping that keeps PhantomBlock below Repository `0` and preserves Repository `1` as the candidate authority for device identity, baselines, capabilities, revocations, receipts, checkpoints, and recovery.
- 2026-07-20 — Added a JusticeForMe overlap analysis proposing separate collector domains, one canonical host-observation envelope, deterministic duplicate/conflict handling, shared privacy rules, and retained compatibility fixtures.
- 2026-07-24 — Added a component-level incubation exit model requiring explicit disposition, semantic and interface ownership, source-to-target provenance, duplicate-authority retirement, contract-gluing review, rollback, and independently reviewable restored-state evidence.

### Implementation

- Added package metadata for `xyz-firmware-defense` version `0.3.0`, with Python 3.11+ dependencies and `xyz` / `phantomblock` console entry points.
- Added source, unit tests, CI configuration, binary/SBOM and read-only image build scripts, example trusted-baseline configuration, and documentation assets.
- Added a GitHub Pages workflow that can publish documentation using `pages: write` and `id-token: write` permissions.
- Earlier release-planning generations lacked current exact-head evidence; predecessor documentation head `5e4229641faac822868673127d305554a269d28a` later passed PhantomBlock CI run `29859387473`. That evidence applies only to that immutable generation.
- 2026-07-19 — No runtime, collector, heuristic, package, API, deployment, credential, networking, or target-mutation behavior changed in the documentation milestone.
- 2026-07-20 — No runtime, evidence schema, collector, adapter, credential, capability, remediation, publication, or deployment behavior changed in the gluing-analysis or overlap milestones.
- 2026-07-24 — No runtime, collector, parser, package, CLI, API, dashboard, extension, adapter, workflow-permission, credential, networking, response, publication, or deployment behavior changed in the incubation-exit milestone.

### Documentation

- 2026-07-19 — Expanded the root README into a complete repository overview covering current status, incubation purpose, prototype inventory, safe local review, contribution boundary, and required architectural decision.
- 2026-07-19 — Rewrote the Pages landing page to distinguish implemented artifacts, configured workflows, local test evidence, proposals, and accepted evidence.
- 2026-07-19 — Added Pages-ready repository boundaries, design contracts, developer onboarding, and ownership/release guides.
- 2026-07-19 — Added `CONTRIBUTING.md` with documentation, evidence, security, and scope-control requirements.
- 2026-07-19 — Added `punchlist.md` with containment, ownership, validation, release, publication, and documentation-health gates.
- 2026-07-19 — Reorganized MkDocs navigation and added Mermaid diagram support.
- 2026-07-19 — Updated `taskchain.md`, `release.md`, and this changelog to record the documentation milestone without advancing implementation or release scope.
- 2026-07-20 — Added `phantomblock/docs/obstruction-and-gluing.md` and linked it from the root README and MkDocs navigation.
- 2026-07-20 — Added `phantomblock/docs/portable-host-observation.md` and `phantomblock/docs/host-observation-overlap.md` and linked both from the README and Pages navigation.
- 2026-07-20 — Expanded `taskchain.md`, `punchlist.md`, and `release.md` with device-trust, JusticeForMe overlap, canonical-field, deduplication, conflict, gluing-fixture, incident, privacy, temporal, migration, consolidation, retirement, and rollback gates.
- 2026-07-24 — Added `phantomblock/docs/incubation-exit-and-migration.md` with an accessible Mermaid diagram and prose equivalent, four controlled dispositions, a non-executable manifest template, component and contract ledgers, source-history preservation, consolidation and retirement controls, validation, fail-closed conditions, reviewer onboarding, and FYSA-120 mapping.
- 2026-07-24 — Synchronized the README, Pages landing page and navigation, `taskchain.md`, `punchlist.md`, `release.md`, and changelog around `INCUBATION_EXIT_DOCUMENTED_DISPOSITION_UNAPPROVED`.

### Security and compliance

- Documentation restricts use to owned or explicitly authorized systems, describes dry-run isolation, and disclaims certification and comprehensive detection assurance.
- No repository license has been selected, representative hardware validation is absent, and compliance mappings are implementation-oriented preparation rather than CMMC status, STIG approval, Army authorization, or an Authority to Operate.
- Public documentation publication, privileged collection, firmware handling, management-plane access, PCAP data, extension loading, and switch-adapter behavior require explicit security, privacy, licensing, and operational review.
- 2026-07-19 — Strengthened warnings against real credentials, proprietary firmware, real incident data, unauthorized assessment, remote dashboard exposure, unreviewed extensions, and active response integrations.
- 2026-07-20 — Clarified that observation cannot self-authorize response; Repository `0` proposal preparation and Repository `1` capability authority remain distinct and unapproved.
- 2026-07-20 — Added fail-closed requirements for device identity, baseline provenance, freshness, replay, artifact binding, privacy classification, temporal ordering, corrections, revocations, and incident recovery.
- 2026-07-20 — Clarified that duplicate observations from JusticeForMe and PhantomBlock are not independent corroboration unless source independence is demonstrated.
- 2026-07-24 — Added fail-closed exit conditions for incomplete component dispositions, unclear source or target generations, vacant authority owners, lossy transformations, unpropagated corrections or revocations, sensitive-data handling gaps, unauthorized infrastructure or credential operations, duplicate authority surfaces, and unverifiable restoration.

### Release

- No package, image, service, deployment, certification, portfolio integration, or production capability is approved from the current prototype.
- The first eligible decision is not a release: the Architect must approve dedicated migration, approved JusticeForMe consolidation, evidence-preserving retirement, or explicit continued incubation.
- Release remains blocked on ownership, product and schema identity, host-observation overlap, gluing contracts, exit manifest and history map, license, threat model, trusted-baseline provenance, representative and adversarial validation, reproducible CI, SBOM/checksums, security review, rollback, restoration, and explicit approval.
- 2026-07-19 — Classified the documentation foundation and repository punch list as partial review evidence; strict documentation build, accessibility/link review, and independent approval remain required.
- 2026-07-20 — Classified the obstruction/gluing and host-observation overlap guides as architectural review evidence only; they do not authorize migration, consolidation, integration, release, or deployment.
- 2026-07-24 — Classified the exit playbook as `DOCUMENTED_NOT_APPROVED`; it defines evidence and governance requirements but does not approve a destination, archive, release, publication, or operational authority.

### Deployment

- Automatic Pages publication was removed; the retained workflow is manual-only and fails closed unless `release.md` is explicitly marked `READY`.
- No operational scanner, live image, dashboard, switch isolation adapter, host-observation integration, or external service is authorized for deployment.
- 2026-07-19 — Documentation changes did not alter the fail-closed Pages workflow or authorize a deployment.
- 2026-07-20 — Gluing and overlap documentation did not alter workflow authority, network access, credentials, or deployment posture.
- 2026-07-24 — Exit-governance documentation did not move source, change repository settings, publish Pages, rotate credentials, deploy services, apply infrastructure, or authorize active response.

## Entry format

- Date
- Category: Product / Architecture / Added / Changed / Fixed / Security / Release / Deployment / Documentation
- Summary
- Evidence: issue, PR, commit, workflow, artifact, or deployment record
- Impact and migration notes where applicable
