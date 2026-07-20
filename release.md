# Release Plan

## Current decision

Status: `BLOCKED — SCOPE CONFLICT, OWNERSHIP, HOST-OBSERVATION OVERLAP, CONTRACT GLUING, VALIDATION, AND PUBLICATION APPROVAL REQUIRED`

`Misc` remains a non-authoritative holding repository at portfolio priority P4. Fifteen commits added the XYZ / PhantomBlock defensive firmware-assessment prototype before the documentation-first incubation contract was approved. The code, tests, workflows, packaging definitions, compliance mappings, and documentation are preserved as prototype evidence; they do not establish an accepted product, operational detector, certification, authorization, portfolio integration, release, or deployment.

The next release-related decision is not a release. The Architect must approve one of three dispositions:

1. migrate PhantomBlock and its full history into a dedicated Repository `0` host-observation adapter repository;
2. consolidate an approved subset with JusticeForMe under one owner, one shared envelope, modular collector boundaries, and preserved histories; or
3. retire/archive PhantomBlock with limitations and provenance preserved.

No package, live image, dashboard, documentation site, switch adapter, service, or integration is eligible for release from `Misc` while ownership, overlap, contracts, and the gates below remain unresolved.

## Documentation milestone

A documentation-only containment and integration package now provides:

- an expanded repository overview and Pages landing page;
- repository and portfolio boundary documentation;
- architecture, runtime, state, and trust-zone diagrams;
- design contracts and claims-to-evidence guidance;
- a portable host-observation role beneath Repository `0` while preserving Repository `1` authority;
- a JusticeForMe / PhantomBlock overlap decision guide covering collector domains, canonical fields, deduplication, conflicts, privacy, and shared fixtures;
- an obstruction and gluing ledger with pairwise and triple-overlap witnesses;
- bounded developer onboarding and contribution rules;
- ownership, migration, consolidation, retirement, release, and rollback decision paths;
- an expanded punch list and documentation-health checklist;
- updated Pages navigation and Mermaid support.

This milestone improves reviewability and reduces architectural ambiguity. It does not change runtime behavior, supported platforms, package authority, device-control authority, publication authorization, or release status. Documentation remains in review until exact-head strict-build evidence and architectural approval are retained.

## Evidence classification

### Implemented prototype artifacts

- Python package `xyz-firmware-defense` version `0.3.0` under `phantomblock/`.
- CLI, dashboard/API, collection and heuristic assessment code, extension interface, and dry-run isolation abstraction.
- Unit-test source, CI workflow configuration, live-image definition, standalone-binary/SBOM build scripts, example trusted-baseline configuration, compliance mappings, and MkDocs documentation.
- GitHub Pages workflow retained as a deployment capability, but automatic `main` publication was removed by commit `c1d5a1d8dc0d729cdb077c0dcac11dc582c2488c`; it is manual-only and fails closed unless this file is explicitly marked `READY`.
- Deployment review and containment evidence are recorded in `deploy.md` at commit `8f82b63c02f21e4c9cea0530fb86c1db7e42f099`.
- Merged PR #1 head `8a56fc7f2fc0b2b0af3c7b47e06bfad70546b48d` has one successful `PhantomBlock CI` run (`29553292217`) in which editable installation, Ruff, and Pytest completed successfully.

### Documentation and architecture proposals

- PhantomBlock as a specialist hardware, firmware, kernel-integrity, management-plane, and explicitly supplied offline-PCAP observer beneath Repository `0`.
- JusticeForMe as the general Linux operating-system, account, package, service, persistence, and network-configuration observer.
- Repository `1` as the candidate device-baseline, capability, revocation, canonical-receipt, checkpoint, and recovery authority.
- One shared host-observation envelope, canonical field vocabulary, deduplication rule, conflict model, privacy policy, and compatibility fixture suite.
- Bridge as an optional evidence-transport layer that creates no trust.
- QSO-STUDIO and AionUi as review surfaces without implicit approval or mutation authority.

These are documentation proposals, not accepted contracts or implemented integration.

### Not established

- Passing status checks or retained artifacts for the current documentation head.
- Approved dedicated-adapter, JusticeForMe consolidation, or retirement disposition.
- Accepted owner for the host-observation envelope and canonical field vocabulary.
- Device-identity, baseline-identity, evidence-envelope, proposal, capability, receipt, revocation, temporal, privacy, incident, and rollback contract ownership.
- Representative BIOS/UEFI, NIC, BMC, SSD, chipset, operating-system, switch, or PCAP validation.
- False-positive/false-negative characterization, parser fuzzing, adversarial corpus, Secure Boot or measured-boot validation, signed provenance, or reproducible release evidence.
- Trusted firmware-source governance, approved credentials or privilege model, extension security review, production isolation safety, incident-response integration, or rollback verification.
- License approval, CMMC status, STIG approval, Army authorization, Authority to Operate, certification, or comprehensive implant-detection assurance.

## Versioning

- Existing `0.3.0` package metadata is prototype metadata, not an approved release version.
- A dedicated owner or approved consolidated repository must select the authoritative product, repository, package, CLI, schema, field, and version lineage.
- Host-observation envelopes, canonical fields, findings, baseline references, capabilities, receipts, revocations, corrections, and checkpoints require independently versioned contracts.
- The first eligible release candidate must be generated from one immutable reviewed commit after migration or consolidation and all applicable gates pass.
- Tags, packages, images, Pages publication, or release artifacts must not imply acceptance before explicit approval.

## Candidate scope after ownership approval

A future candidate may include only the explicitly reviewed subset of:

- passive inventory and evidence collection;
- firmware and baseline verification with independently governed trusted sources;
- bounded kernel and management-channel heuristics;
- offline external-PCAP analysis;
- read-only dashboard and machine-readable reports;
- reviewed passive extension interfaces;
- a versioned host-observation envelope and canonical field vocabulary shared with Repository `0`, Repository `1`, and JusticeForMe where applicable;
- Repository `0` integration for observation composition and proposal preparation;
- Repository `1` validation for identity, policy, freshness, replay, capability, revocation, receipt, and recovery semantics;
- disruptive isolation only behind a separately approved, authenticated, allowlisted, audited, dry-run-first interface with rollback verification;
- reproducible packaging, SBOM, checksums, signed provenance, and documentation whose claims match retained evidence.

## Explicit exclusions

- Unauthorized assessment, credential bypass, exploitation, firmware flashing, destructive remediation, covert collection, unrestricted networking, or default-active switch isolation.
- Customer data, credentials, sensitive firmware images, exploit details, or security findings in the public repository.
- Counting duplicate observations as independent corroboration without evidence of independence.
- Letting an observation, report, dashboard action, successful command, or transported message self-authorize remediation or canonical state.
- Certification, DoD/Army authorization, operational-readiness, or comprehensive-detection claims unsupported by formal evidence.
- Permanent production ownership by `Misc` or bypass of Repository `0`, Repository `1`, JusticeForMe, Bridge, AionUi, QSO-STUDIO, or other repository boundaries.

## Acceptance gates

| Gate | Status | Requirement |
|---|---|---|
| Scope containment | PARTIAL | Automatic Pages publication is disabled and promotion remains frozen while source and history are preserved. |
| Documentation foundation | PARTIAL | Overview, architecture, boundaries, portable role, JusticeForMe overlap, gluing analysis, onboarding, decision guides, and punch list exist; exact-head strict build, accessibility, link validation, and approval remain required. |
| Ownership/disposition | FAIL | Approve dedicated adapter, JusticeForMe consolidation, or retirement/archive. |
| Product definition | FAIL | Intended user, authorized-use boundary, supported platforms, claims, limitations, and non-goals are approved. |
| Host-observation overlap | FAIL | JusticeForMe and PhantomBlock domains, identities, canonical fields, deduplication, conflict semantics, privacy, and histories are reconciled. |
| Repository `0` / Repository `1` gluing | FAIL | Device, baseline, envelope, proposal, capability, receipt, revocation, correction, temporal, incident, and rollback contracts are versioned and owned. |
| License and data rights | FAIL | Select a license and approve dependencies, firmware sources, PCAP handling, documentation, and third-party content. |
| Threat model | PARTIAL | Existing documentation covers privilege, extension, firmware, network, dashboard, packaging, publication, overlap, and authority risks; independent review remains absent. |
| Validation | NO ACCEPTED EVIDENCE | Representative hardware and duplicate, conflict, partial, stale, replay, wrong-device, malformed, adversarial, and rollback fixtures pass. |
| Dependencies/build | UNVERIFIED | Clean environments reproduce installation, tests, documentation, binary/image outputs, SBOMs, and checksums. |
| Publication | CONTAINED | Automatic publication is disabled; explicit future targets and approval remain required. |
| Security/privacy | FAIL | Credential, privilege, network, firmware, evidence, privacy, retention, disclosure, and incident controls pass review. |
| Provenance/rollback | PARTIAL | Containment commits and deployment review exist; candidate archives, hashes, signed provenance, migration/consolidation manifests, runtime rollback, and retirement procedures remain unverified. |
| Approval | PENDING | Explicit release approval only after every blocking gate passes. |

## Required artifacts

- Approved dedicated-adapter, JusticeForMe consolidation, or retirement decision.
- Product directive, supported-platform matrix, threat model, authorized-use policy, and repository-overlap decision.
- Canonical host-observation envelope and field-vocabulary ownership record.
- Device, baseline, proposal, capability, receipt, revocation, correction, temporal, incident, and rollback contracts.
- License and third-party dependency/data/firmware provenance record.
- Repository-health report and completed punch list tied to the exact candidate commit.
- Strict documentation build, link review, accessibility review, and claims-to-evidence review tied to the exact documentation head.
- Representative positive, negative, duplicate, independent-corroboration, conflicting, partial, stale, replayed, wrong-device, privacy, malformed, extension, privilege, network, and response-boundary fixtures.
- Hardware-lab results, false-positive/false-negative characterization, performance limits, and unsupported-platform behavior.
- Reproducible build/test logs, retained workflow artifacts, SBOM, checksums, vulnerability results, source archive, signed provenance, review record, and rollback instructions.

## Rollback criteria

Reject or withdraw a candidate if ownership remains ambiguous; implementation continues in `Misc` without approval; JusticeForMe overlap remains implicit; duplicate observations can inflate confidence; public documentation implies release; license or data rights are unresolved; trusted baselines lack independent provenance; privileged or disruptive behavior is not fail-closed; representative and adversarial validation is absent; claims exceed evidence; builds or checks cannot be reproduced; provenance is incomplete; rollback cannot be verified; or an authorizing party declines deployment.

For the current documentation branch, rollback is removal or reversion of documentation commits. No runtime or deployment rollback is required because implementation and workflow authority are unchanged.

## Unresolved blockers

- Approve dedicated PhantomBlock ownership, JusticeForMe consolidation, or retirement/archive.
- Assign canonical host-observation envelope and field-vocabulary ownership.
- Approve device identity, baseline authority, Repository `0` proposal route, Repository `1` capability/receipt/revocation authority, and temporal semantics.
- Approve intended user, authorized-use boundary, license, naming, package identity, supported platforms, privacy, retention, incident, and recovery owners.
- Obtain exact-head strict documentation build, accessibility/link review, and claims review.
- Complete exact-candidate builds, tests, representative hardware and adversarial validation, artifacts, SBOM/checksums, provenance, and rollback exercises.

## Release log

- 2026-07-16 — Established `Misc` as a documentation-first incubation repository with no implementation or deployment authority.
- 2026-07-16 — Detected the addition of the XYZ prototype, CI, packaging, compliance documentation, and automatic Pages publication before incubation approval.
- 2026-07-16 — Preserved the prototype as unaccepted evidence and blocked release pending containment, dedicated ownership or retirement, license, validation, security, publication, provenance, and explicit approval.
- 2026-07-16 — Disabled automatic Pages publication and recorded deployment containment; no deployment ran.
- 2026-07-19 — Prepared a substantial documentation-only containment milestone; release remained blocked.
- 2026-07-20 — Added portable host-observation, JusticeForMe overlap, and obstruction/gluing documentation. Release remains blocked and no runtime, authority, or publication scope changed.
