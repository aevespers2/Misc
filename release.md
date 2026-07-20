# Release Plan

## Current decision

Status: `BLOCKED — SCOPE CONFLICT, OWNERSHIP, CONTRACT GLUING, VALIDATION, AND PUBLICATION APPROVAL REQUIRED`

`Misc` remains a non-authoritative holding repository at portfolio priority P4. Fifteen commits added the XYZ / PhantomBlock defensive firmware-assessment prototype before the documentation-first incubation contract was approved. The code, tests, workflows, packaging definitions, compliance mappings, and documentation are preserved as prototype evidence; they do not establish an accepted product, operational detector, certification, authorization, portfolio integration, release, or deployment.

The next release-related decision is an Architect ownership and disposition decision: migrate XYZ and its full history into a dedicated approved repository with explicit Repository `0` / Repository `1` contracts, or retire/archive it with limitations preserved. No package, live image, dashboard, documentation site, switch adapter, service, or integration is eligible for release from `Misc` while that decision and the gates below remain unresolved.

## Documentation milestone

A documentation-only containment package now provides:

- an expanded repository overview and Pages landing page;
- repository and portfolio boundary documentation;
- architecture, runtime, state, and trust-zone diagrams;
- design contracts and claims-to-evidence guidance;
- bounded developer onboarding and contribution rules;
- an ownership, migration, retirement, release, and rollback decision path;
- a repository punch list and documentation-health checklist;
- an obstruction and gluing ledger with eighteen active incompatibilities;
- a proposed specialist Repository `0` observation-adapter role and preserved Repository `1` authority boundary;
- pairwise and triple-overlap witness requirements;
- a proposed evidence-envelope minimum covering device, policy, collection, artifact, finding, freshness, and limitation identity;
- updated Pages navigation and Mermaid support.

This milestone improves reviewability and integration analysis. It does not change runtime behavior, supported platforms, package authority, device-control authority, publication authorization, or release status. Documentation remains in review until exact-head strict-build evidence and architectural approval are retained.

## Evidence classification

### Implemented prototype artifacts

- Python package `xyz-firmware-defense` version `0.3.0` under `phantomblock/`.
- CLI, dashboard/API, collection and heuristic assessment code, extension interface, and dry-run isolation abstraction.
- Unit-test source, CI workflow configuration, live-image definition, standalone-binary/SBOM build scripts, example trusted-baseline configuration, compliance mappings, and MkDocs documentation.
- GitHub Pages workflow retained as a deployment capability, but automatic `main` publication was removed by commit `c1d5a1d8dc0d729cdb077c0dcac11dc582c2488c`; it is manual-only and fails closed unless this file is explicitly marked `READY`.
- Deployment review and containment evidence are recorded in `deploy.md` at commit `8f82b63c02f21e4c9cea0530fb86c1db7e42f099`.
- Merged PR #1 head `8a56fc7f2fc0b2b0af3c7b47e06bfad70546b48d` has one successful `PhantomBlock CI` run (`29553292217`) in which editable installation, Ruff, and Pytest completed successfully.
- A documentation and gluing-analysis milestone exists on a feature branch; its changes are review evidence only until the exact branch head receives retained strict-build and review results.

### Proposed architecture only

- PhantomBlock as a specialist host-firmware, kernel, management-plane, and offline-PCAP observation adapter beneath Repository `0`.
- Repository `1` as device-baseline, capability, revocation, canonical-receipt, checkpoint, and recovery authority.
- Bridge as an optional evidence-transport layer that creates no trust.
- QSO-STUDIO and AionUi as review surfaces without implicit approval or mutation authority.
- A versioned host-observation envelope and cross-repository fixture set.

These are documentation proposals, not accepted contracts or implemented integration.

### Not established

- Passing status checks or workflow runs for the current documentation/release-planning head.
- Retained test or documentation artifacts for the current head.
- A dedicated owning repository, approved product identity, or accepted migration/retirement decision.
- Device-identity, baseline-identity, evidence-envelope, proposal, capability, receipt, revocation, temporal, privacy, incident, and rollback contract ownership.
- Representative BIOS/UEFI, NIC, BMC, SSD, chipset, operating-system, switch, or PCAP validation.
- False-positive/false-negative characterization, parser fuzzing, adversarial corpus, Secure Boot or measured-boot validation, signed provenance, or reproducible release evidence.
- Trusted firmware-source governance, approved credentials or privilege model, extension security review, production isolation safety, incident-response integration, or rollback verification.
- License approval, CMMC status, STIG approval, Army authorization, Authority to Operate, certification, or comprehensive implant-detection assurance.

## Selected completed work

No work is selected for release. The merged prototype, prior PR-level lint/test run, publication containment, documentation foundation, and gluing analysis are retained as implementation and review evidence only. They remain excluded from a release candidate until ownership, repository scope, contract compatibility, licensing, security, validation, publication, provenance, and rollback gates are approved and reproduced at one immutable candidate commit.

## Versioning

- Existing `0.3.0` package metadata is prototype metadata, not an approved release version.
- A dedicated owning repository must select the authoritative product, repository, package, CLI, schema, and version lineage.
- Host-observation envelopes, findings, baseline references, capabilities, receipts, revocations, corrections, and checkpoints require independently versioned contracts.
- The first eligible release candidate must be generated from one immutable reviewed commit after migration and all applicable gates pass.
- Tags, packages, images, Pages publication, or release artifacts must not imply acceptance before explicit approval.

## Candidate scope after ownership approval

A future candidate may include only the explicitly reviewed subset of:

- passive inventory and evidence collection;
- firmware and baseline verification with independently governed trusted sources;
- bounded kernel and management-channel heuristics;
- offline external-PCAP analysis;
- read-only dashboard and machine-readable reports;
- reviewed passive extension interfaces;
- a versioned, device-bound, privacy-classified evidence envelope;
- Repository `0` integration for observation composition and proposal preparation;
- Repository `1` validation for identity, policy, freshness, replay, capability, revocation, receipt, and recovery semantics;
- disruptive isolation only behind a separately approved, authenticated, allowlisted, audited, dry-run-first interface with rollback verification;
- reproducible packaging, SBOM, checksums, signed provenance, and documentation whose claims match retained evidence.

## Explicit exclusions

- Unauthorized assessment, credential bypass, exploitation, firmware flashing, destructive remediation, covert collection, unrestricted networking, or default-active switch isolation.
- Customer data, credentials, sensitive firmware images, exploit details, or security findings in the public repository.
- Certification, DoD/Army authorization, operational-readiness, or comprehensive-detection claims unsupported by formal evidence.
- Permanent production ownership by `Misc` or bypass of Repository `0`, Repository `1`, Bridge, AionUi, QSO-STUDIO, verification, or other repository boundaries.
- Treating a finding, dashboard action, successful command, or transported message as self-authorizing canonical state.

## Planned changelog entries for a future approved owner

- `Added`: the specifically approved passive assessment, reporting, envelope, and reviewed extension subset after migration.
- `Security`: trusted-baseline governance, privilege and credential boundaries, parser and extension hardening, network restrictions, isolation safeguards, vulnerability results, and disclosure limitations.
- `Validation`: supported-platform matrix, representative hardware results, adversarial and malformed-input fixtures, false-positive/false-negative characterization, performance limits, unsupported-platform behavior, and gluing witnesses.
- `Documentation`: authorized-use policy, non-goals, evidence classifications, operational limits, contract ownership, incident handling, recovery, migration, retirement, and rollback.
- `Release`: authoritative identity, immutable source commit, build/test reports, SBOM, source and binary/image artifacts where approved, checksums, signed provenance, contract manifest, migration record, and approval decision.

## Acceptance gates

| Gate | Status | Requirement |
|---|---|---|
| Scope containment | PARTIAL | Automatic Pages publication is disabled and the workflow fails closed; feature, packaging, and deployment promotion remain frozen while the prototype and history are preserved. |
| Documentation foundation | PARTIAL | Overview, architecture, boundaries, design, onboarding, contribution, decision, punch-list, and gluing documents exist on a review branch; exact-head strict build, accessibility review, link validation, and independent approval remain required. |
| Ownership | FAIL | Architect approves one dedicated repository and owner, or records retirement/archive. |
| Product definition | FAIL | Intended user, authorized-use boundary, supported platforms, claims, limitations, and non-goals are approved. |
| Portfolio role | FAIL | Approve or reject the proposed Repository `0` specialist observation-adapter role and Repository `1` authority boundary. |
| Contract gluing | FAIL | Assign owners and accepted versions for device, baseline, envelope, proposal, capability, receipt, revocation, correction, temporal, privacy, incident, and rollback contracts; retain pairwise and triple-overlap fixtures. |
| Repository overlap | FAIL | Compare and disposition overlap with existing security, Bridge, AionUi, QSO-STUDIO, verification, and QSO repositories. |
| Punch list / health baseline | PARTIAL | `punchlist.md` records repository-health, gluing, and release work; accepted health results tied to an immutable candidate remain absent. |
| License and data rights | FAIL | Select a license and approve dependencies, firmware sources, PCAP handling, documentation, and third-party content. |
| Threat model | PARTIAL | Existing documentation describes privilege, extension, firmware, network, dashboard, packaging, transport, and publication risks; independent review and closure remain absent. |
| Validation | NO ACCEPTED EVIDENCE | Representative hardware, negative/adversarial fixtures, fuzzing, false-positive/negative analysis, envelope tests, gluing tests, and isolation rollback pass. |
| Dependencies/build | UNVERIFIED | Clean environments reproduce installation, tests, documentation, binary/image outputs, SBOMs, and checksums. |
| CI/status checks | PARTIAL | A prior merged PR head passed editable install, Ruff, and Pytest, but the current planning/documentation head has no retained accepted evidence yet. One immutable candidate must reproduce complete checks and artifacts. |
| Publication | CONTAINED | Automatic publication is disabled; an explicit future Pages/publication target and approval remain required. |
| Security/privacy | FAIL | Credential, privilege, network, firmware, evidence, privacy, disclosure, temporal, correction, and incident-response boundaries pass review. |
| Provenance/rollback | PARTIAL | Publication-containment commits and a deployment record exist; candidate archives, hashes, signed provenance, migration record, contract manifest, runtime rollback, and retirement procedure remain unverified. |
| Approval | PENDING | Explicit release approval only after every blocking gate passes. |

## Required artifacts

- Approved ownership and migration or retirement record.
- Product directive, supported-platform matrix, threat model, authorized-use policy, and repository-overlap decision.
- Approved portfolio-role and cross-repository contract decision.
- License and third-party dependency/data/firmware provenance record.
- Repository-health report and completed punch list tied to the exact candidate commit.
- Strict documentation build, link review, accessibility review, and claims-to-evidence review tied to the exact documentation head.
- Versioned device, baseline, evidence, proposal, capability, receipt, revocation, temporal, privacy, incident, and rollback contract manifest.
- Pairwise and triple-overlap positive, negative, stale, replay, malformed, wrong-device, unsupported-version, partial-failure, correction, revocation, and rollback fixtures.
- Representative hardware-lab results, false-positive/false-negative characterization, performance limits, and unsupported-platform behavior.
- Reproducible build/test logs, retained workflow artifacts, SBOM, checksums, vulnerability results, source archive, signed provenance, review record, and rollback instructions.

## Rollback criteria

Reject or withdraw a candidate if ownership remains ambiguous; implementation continues in `Misc` without approval; public documentation implies release; license or data rights are unresolved; trusted baselines are derived from an assessed host or lack provenance; privileged or disruptive behavior is not fail-closed; extension boundaries permit uncontrolled mutation; Repository `0` and Repository `1` disagree on identity or authority; stale, replayed, incomplete, or corrected evidence can be accepted as current; representative and adversarial validation is absent; claims exceed evidence; builds or checks cannot be reproduced; provenance is incomplete; rollback cannot be verified; or an authorizing party declines deployment. Preserve source history, failed evidence, limitations, revocations, and disposition records.

For the current documentation branch, rollback is removal or reversion of the documentation commits. No runtime or deployment rollback is required because implementation and workflow authority are unchanged.

## Unresolved blockers

- Architect decision to migrate XYZ into a dedicated owning repository or retire/archive it.
- Approval or rejection of the proposed Repository `0` specialist observation-adapter role.
- Approval of intended user, authorized-use boundary, repository overlap, license, naming, package identity, and version lineage.
- Assignment and acceptance of device, baseline, envelope, proposal, capability, receipt, revocation, temporal, privacy, incident, and rollback contracts.
- Explicit approval of any future GitHub Pages publication or other public artifact; automatic publication is currently disabled.
- Exact-head strict documentation build, accessibility/link review, and claims review.
- Exact-candidate clean build, complete tests, security review, representative hardware and adversarial validation, retained artifacts, SBOM/checksums, provenance, gluing fixtures, and rollback drill.
- Trusted firmware and data-source governance, credential/privilege model, extension boundary, false-positive/false-negative characterization, and incident/disclosure policy.

## Release log

- 2026-07-16 — Established `Misc` as a documentation-first incubation repository with no implementation or deployment authority.
- 2026-07-16 — Detected the addition of the XYZ prototype, CI, packaging, compliance documentation, and automatic Pages publication before incubation approval.
- 2026-07-16 — Preserved the prototype as unaccepted evidence and blocked release pending containment, dedicated ownership or retirement, license, validation, security, publication, provenance, and explicit approval.
- 2026-07-16 — Reclassified CI evidence as partial after verifying one successful merged-PR lint/test run with no retained artifacts; no current-head or release-candidate evidence was established.
- 2026-07-16 — Disabled automatic Pages publication, added a fail-closed explicit-release-readiness gate, and recorded deployment review evidence in `deploy.md`; no deployment ran.
- 2026-07-19 — Prepared a substantial documentation-only containment milestone on a feature branch. Release remained blocked pending strict-build evidence and review.
- 2026-07-20 — Added a portfolio obstruction/gluing analysis and updated planning gates around a proposed Repository `0` observation-adapter role and Repository `1` authority boundary. No runtime, credential, response, publication, or release authority changed.
