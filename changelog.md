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
- 2026-07-24 — Added four controlled incubation dispositions: dedicated migration, modular consolidation, evidence-preserving retirement, and continued hold. No disposition was selected or approved.
- 2026-07-24 — Added `COMPONENT_OVERLAP_INVENTORY_DOCUMENTED_DISPOSITION_UNAPPROVED`; component-family and portfolio-overlap documentation does not select a destination, owner, contract, migration, release, publication, or operational route.

### Architecture

- Experiments must remain non-authoritative, isolated, bounded, reversible, and mapped against existing repository ownership before work begins.
- Successful experiments must migrate to a dedicated approved owner; rejected or inconclusive work must retain provenance and limitations when archived.
- XYZ currently resides under `phantomblock/` and includes a Python package, CLI, dashboard/API, passive assessment logic, extension interface, dry-run isolation abstraction, live-image and binary-build definitions, tests, compliance mappings, and documentation.
- Code and configuration demonstrate a prototype shape only; supported hardware, trusted firmware provenance, detection accuracy, isolation safety, operational security, and authorization readiness remain unverified.
- 2026-07-23 — Added accessible system-context and incubation-lifecycle diagrams with equivalent prose, explicit trust and ownership vacancies, interface-documentation requirements, and fail-closed obstruction conditions.
- 2026-07-24 — Added an authority-neutral exit architecture requiring an immutable source freeze, component disposition ledger, source-to-target or archive provenance, contract-gluing review, duplicate-authority deprecation, correction and revocation propagation, rollback, and restored-state verification.
- 2026-07-24 — Added C01-C18 component families, O01-O10 portfolio overlaps, ten gluing failures, safe defaults, required pairwise witnesses, and a disposition matrix covering dedicated migration, modular consolidation, retirement, and continued hold.

### Documentation

- 2026-07-23 — Added `phantomblock/docs/incubation-status.md`, clarifying evidence classes, source precedence, controlled changes, and the migrate/retire/hold decision.
- 2026-07-23 — Added `phantomblock/docs/onboarding.md` with authorization, privacy, sensitive-data, non-deployment, reproducibility, and first-contribution safeguards.
- 2026-07-23 — Added `phantomblock/docs/developer-guide.md` with change classes, architecture rules, interface-documentation requirements, evidence expectations, pull-request checks, migration, and retirement guidance.
- 2026-07-23 — Added `punchlist.md` and synchronized the README, MkDocs navigation, task chain, release plan, and changelog.
- 2026-07-24 — Added `phantomblock/docs/incubation-exit-and-migration.md` with an accessible decision diagram and prose equivalent, four controlled dispositions, a non-executable manifest template, component and contract ledgers, history-preservation rules, hostile fixture requirements, consolidation and retirement controls, fail-closed stop conditions, reviewer onboarding, and FYSA-120 mapping.
- 2026-07-24 — Synchronized README, MkDocs navigation, documentation front door, `taskchain.md`, `punchlist.md`, `release.md`, and this changelog around `INCUBATION_EXIT_DOCUMENTED_DISPOSITION_UNAPPROVED`.
- 2026-07-24 — Added `phantomblock/docs/component-overlap-inventory.md` and `component-overlap-inventory-v1.json`, with an accessible portfolio relationship diagram, prose equivalent, observed component ledger, ownership conflicts, required witnesses, completion boundary, reviewer onboarding, and skill-tree mapping.
- 2026-07-24 — Synchronized README, MkDocs navigation, `taskchain.md`, `punchlist.md`, `release.md`, and this changelog around the component-overlap milestone while preserving the incomplete exact file-level manifest as a separate blocking task.

### Implementation

- Added package metadata for `xyz-firmware-defense` version `0.3.0`, with Python 3.11+ dependencies and `xyz`/`phantomblock` console entry points.
- Added source, unit tests, CI configuration, binary/SBOM and read-only image build scripts, example trusted-baseline configuration, and documentation assets.
- Added a GitHub Pages workflow. Automatic publication was later removed; the workflow is manual-only and fails closed unless `release.md` is explicitly `READY`.
- No current release-candidate validation, supported-platform evidence, or operational approval is established by this documentation change.
- 2026-07-24 — No runtime, collector, parser, package, API, dashboard, extension, workflow-permission, credential, networking, response, publication, release, deployment, or infrastructure behavior changed in the exit-governance milestone.
- 2026-07-24 — The component-overlap milestone changed documentation and planning records only; it created no adapter, registration, cross-repository integration, migration, capability, credential, service, or publication behavior.

### Security and compliance

- Documentation restricts use to owned or explicitly authorized systems, describes dry-run isolation, and disclaims certification and comprehensive detection assurance.
- No repository license has been selected, representative hardware validation is absent, and the compliance mappings are implementation-oriented preparation rather than CMMC status, STIG approval, Army authorization, or an Authority to Operate.
- Public documentation publication, privileged collection, firmware handling, management-plane access, PCAP data, extension loading, and switch-adapter behavior require explicit security, privacy, licensing, and operational review.
- 2026-07-23 — Strengthened public guidance against credentials, proprietary firmware, sensitive packet captures, customer data, private findings, and production evidence in Git, CI, Pages, issues, or public artifacts.
- 2026-07-24 — Added fail-closed exit conditions for unclear source or target identity, incomplete component dispositions, vacant required owners, lossy or untested transformations, ambiguous copied history, duplicate authority surfaces, unpropagated corrections or revocations, sensitive-data handling gaps, unauthorized credential or infrastructure operations, and unverifiable rollback or restoration.
- 2026-07-24 — Added overlap-specific security defaults for collector duplication, proposal/execution collapse, unsupported canonical disposition, untrusted source input, stale evidence, observation/interpretation collapse, external handoff, UI authority inflation, aggregate evidence inflation, and rollback resurrection.

### Validation

- 2026-07-23 — Added deterministic documentation-structure, internal-link, planning-alignment, diagram-alternative, authority-boundary, and workflow-permission checks with hostile regressions.
- 2026-07-23 — Extended the documentation workflow to validate exact `main` heads after relevant merges, while preserving read-only permissions, pinned Actions, non-persistent credentials, retained evidence, and the manual-only Pages boundary.
- Documentation validation establishes structural consistency only; it does not validate detection, hardware support, security, release, publication, or operational capability.
- 2026-07-24 — Required every changed descendant and resulting state to retain its own exact-head validation; historical passing evidence remains historical evidence only.
- 2026-07-24 — Required the Markdown and JSON component inventories, lifecycle routes, status markers, diagram alternatives, and exact-source currentness to remain synchronized.
- 2026-07-24 — Repaired documentation-workflow concurrency so every pull-request and `main` generation is isolated by immutable submitted SHA and cannot cancel evidence collection for an earlier exact head; added hostile regressions that reject mutable PR/ref grouping and cross-generation cancellation.

### Release

- No package, image, service, deployment, certification, or production capability is approved from the current prototype.
- The first eligible decision is not a release: the Architect must approve dedicated migration, modular consolidation, evidence-preserving retirement, or continued hold.
- Release remains blocked on ownership, exact file-level disposition, source-to-target history, accepted overlap witnesses, license, threat model, trusted-baseline provenance, representative and adversarial validation, reproducible CI, SBOM/checksums, security review, correction and revocation propagation, rollback, restoration, and explicit approval.
- 2026-07-23 — Confirmed that the documentation milestone does not change the blocked release or publication status.
- 2026-07-24 — Classified the exit playbook as `DOCUMENTED_NOT_APPROVED`; documentation and workflow success cannot authorize migration, release, publication, or operational use.
- 2026-07-24 — Recorded the component inventory as review evidence only; an inventory, path manifest, or overlap graph cannot authorize ownership, migration, integration, release, or deployment.

### Deployment

- Pages publication remains manual-only and fail-closed until the release plan is explicitly marked `READY`.
- No operational scanner, live image, dashboard, switch isolation adapter, or external integration is authorized for deployment.
- 2026-07-24 — Exit-governance documentation did not move source, publish Pages, rotate credentials, deploy services, apply infrastructure, or authorize active response.
- 2026-07-24 — Component-overlap documentation did not invoke external systems, access firmware or packet evidence, change credentials, publish Pages, move source, activate consumers, deploy services, or apply infrastructure.

### FYSA-120

- 2026-07-24 — Applied `CAT-011`, `CAT-012`, `CAT-013`, `CAT-017`, `CAT-018`, `CAT-019`, `CAT-031`, `CAT-032`, `CAT-040`, `CAT-052`, and `CAT-054` as a capability map, not proof of competence or authority.
- 2026-07-24 — Applied `CAT-017`, `CAT-022`, `CAT-031`, `CAT-040`, `CAT-052`, `CAT-054`, and `CAT-059` to the exact-head evidence-continuity repair; existing refinement `031-L` covers this repair class.
- 2026-07-24 — Proposed non-authoritative refinement `040-P — Incubation exit, authority-neutral migration, modular consolidation, and evidence-preserving retirement`, superseding the narrower local `040-H` proposal for this repository.
- 2026-07-24 — Proposed non-authoritative refinement `013-M — Incubated component-family inventories, cross-repository overlap ledgers, and disposition-safe ownership graphs`.

## Entry format

- Date
- Category: Product / Architecture / Documentation / Added / Changed / Fixed / Security / Validation / Release / Deployment
- Summary
- Evidence: issue, PR, commit, workflow, artifact, or deployment record
- Impact and migration notes where applicable
