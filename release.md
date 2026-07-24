# Release Plan

## Current decision

Status: `BLOCKED — SCOPE CONFLICT, OWNERSHIP, EXIT DISPOSITION, VALIDATION, LICENSING, AND PUBLICATION APPROVAL REQUIRED`

`Misc` remains a non-authoritative holding repository at portfolio priority P4. The XYZ / PhantomBlock code, tests, workflows, packaging definitions, compliance mappings, and documentation are preserved as prototype evidence. They do not establish an accepted product, operational detector, supported-platform claim, certification, authorization, release, publication, or deployment.

The next release-related decision is not a release. An Architect must approve dedicated migration to a named owner, modular consolidation with a named owner, evidence-preserving retirement/archive, or a continued hold with explicit reopening conditions. No package, live image, dashboard, documentation site, switch adapter, service, or integration is eligible for release from `Misc` while that disposition and the gates below remain unresolved.

## Documentation candidate

The repository has a front door, incubation-status guide, accessible architecture, safe onboarding, developer guide, component and portfolio overlap inventory, machine-readable companion, exit and migration playbook, punch list, task chain, release plan, and changelog. These materials improve decision readiness and evidence classification only. They do not convert the prototype into an accepted product or make Pages publication appropriate.

Controlled exit status: `INCUBATION_EXIT_DOCUMENTED_DISPOSITION_UNAPPROVED`.

Component-overlap status: `COMPONENT_OVERLAP_INVENTORY_DOCUMENTED_DISPOSITION_UNAPPROVED`.

The inventory records eighteen component families, ten portfolio overlaps, safe defaults, required compatibility witnesses, ten material gluing failures, and disposition options. It does not complete the exact file-level path-and-hash manifest or select an owner, target, archive, contract, or migration route.

## Evidence classification

### Implemented prototype artifacts

- Python package `xyz-firmware-defense` version `0.3.0` under `phantomblock/`.
- CLI, dashboard/API, collection and heuristic-assessment code, extension interface, and dry-run isolation abstraction.
- Unit-test source, CI configuration, live-image definition, standalone-binary/SBOM build scripts, example trusted-baseline configuration, compliance mappings, and MkDocs documentation.
- GitHub Pages workflow retained as a deployment capability, but automatic `main` publication is disabled; it is manual-only and fails closed unless this file is explicitly marked `READY`.
- Historical deployment-review and containment records.
- Historical exact-generation workflow evidence; each changed descendant requires independent revalidation.

### Documentation and architecture proposals

- Dedicated migration under an approved repository and charter.
- Modular consolidation with JusticeForMe or another named owner under one canonical envelope and field vocabulary.
- Evidence-preserving retirement with immutable archive identity, limitations, retention, withdrawal, and restoration controls.
- Continued frozen incubation when no safe disposition is approved.
- Source-to-target component and commit mapping, correction and revocation propagation, duplicate-authority deprecation, rollback, and restored-state verification.
- Candidate overlap routes connecting observation, proposal, source governance, temporal interpretation, domain interpretation, transport, review, presentation, aggregation, disposition, and recovery repositories.

These are documentation proposals, not accepted contracts or implemented integration.

### Not established

- Approved exit disposition, destination, archive, or owner.
- Complete exact file-level path, digest, evidence, sensitivity, disposition, owner, loss, correction, and rollback manifest.
- Accepted cross-repository overlap edges, producer/consumer registrations, interface ownership, or compatibility witnesses.
- Current release-candidate or resulting-default-head validation evidence.
- Representative BIOS/UEFI, NIC, BMC, SSD, chipset, operating-system, switch, or PCAP validation.
- False-positive/false-negative characterization, parser fuzzing, adversarial corpus, Secure Boot or measured-boot validation, signed provenance, or reproducible release evidence.
- Trusted firmware-source governance, approved credentials or privilege model, extension security review, production isolation safety, incident-response integration, or rollback verification.
- License approval, CMMC status, STIG approval, Army authorization, Authority to Operate, certification, or comprehensive implant-detection assurance.

## Versioning

- Existing `0.3.0` package metadata is prototype metadata, not an approved release version.
- A dedicated or consolidated owner must select the authoritative name, package identity, version lineage, license, compatibility policy, and deprecation route.
- The first eligible release candidate must be generated from one immutable reviewed commit after an approved disposition and all applicable gates pass.
- Tags, packages, images, Pages publication, inventories, migration manifests, or release artifacts must not imply acceptance before explicit approval.

## Candidate scope after ownership approval

A future candidate may include only an explicitly reviewed subset of:

- passive inventory and evidence collection;
- firmware and baseline verification with independently governed trusted sources;
- bounded kernel and management-channel heuristics;
- offline external-PCAP analysis;
- read-only dashboard and machine-readable reports;
- reviewed passive extension interfaces;
- disruptive isolation only behind a separately approved, authenticated, allowlisted, audited, dry-run-first interface with resulting-state and rollback verification;
- reproducible packaging, SBOM, checksums, signed provenance, and documentation whose claims match retained evidence.

## Explicit exclusions

- Unauthorized assessment, credential bypass, exploitation, firmware flashing, destructive remediation, covert collection, unrestricted networking, or default-active switch isolation.
- Customer data, credentials, sensitive firmware images, private packet captures, exploit details, or security findings in the public repository.
- Certification, DoD/Army authorization, operational-readiness, supported-platform, or comprehensive-detection claims unsupported by formal evidence.
- Permanent production ownership by `Misc` or bypass of existing portfolio repository boundaries.
- Treating a copied directory, inventory, manifest, passing workflow, or documentation approval as product, integration, release, or deployment authorization.
- Destructive history rewriting solely to simplify transfer.

## Acceptance gates

| Gate | Status | Requirement |
|---|---|---|
| Scope containment | REVIEW | Manual-only Pages gate remains fail-closed; feature, package, image, and deployment promotion remain frozen. |
| Documentation integrity | REVIEW | README, MkDocs pages, component inventory, exit playbook, `taskchain.md`, `punchlist.md`, `release.md`, and `changelog.md` agree and pass exact-head checks. |
| Exit disposition | FAIL | Architect approves dedicated migration, modular consolidation, evidence-preserving retirement, or continued hold. |
| Component-family inventory | REVIEW | C01-C18 and O01-O10 are documented; reviewer confirmation and exact-source rebinding remain required. |
| File and history disposition | FAIL | Every relevant path and authority surface receives a digest-bound disposition; source-to-target or archive provenance is independently reviewable. |
| Ownership | FAIL | Destination or archive, semantic/interface owners, security/privacy reviewers, evidence custodian, correction/revocation owners, publication authority, and rollback owner are named or explicitly vacant. |
| Product definition | FAIL | Intended user, authorized-use boundary, supported and unsupported platforms, claims, limitations, and non-goals are approved. |
| Repository overlap | FAIL | Overlap with JusticeForMe, Repository `0`, Repository `1`, QSO-SEEKER, the temporal repository, QSO-DIGITALIS, Bridge, QSO-STUDIO, AionUi, QSO-FABRIC, verification, and security repositories is reviewed and dispositioned. |
| License and data rights | FAIL | License and dependency, firmware, PCAP, documentation, and third-party-content rights are approved. |
| Threat model | PARTIAL | Documentation records privilege, extension, firmware, network, dashboard, packaging, publication, migration, consolidation, retirement, overlap, and authority risks; independent review remains absent. |
| Validation | NO ACCEPTED EVIDENCE | Representative hardware and negative, adversarial, duplicate, conflict, stale, replay, wrong-device, correction, revocation, withdrawal, and rollback fixtures pass. |
| Dependencies/build | UNVERIFIED | Clean environments reproduce installation, tests, documentation, binary/image outputs, SBOMs, and checksums. |
| CI/status checks | PARTIAL | Documentation checks exist; one immutable current candidate must reproduce complete checks and retain artifacts. |
| Accessibility | REVIEW | Diagrams have equivalent prose and documentation routes are structured; generated-site accessibility evidence remains required. |
| Publication | CONTAINED | Automatic publication is disabled; explicit Pages target, review, and approval remain required. |
| Security/privacy | FAIL | Credential, privilege, network, firmware, evidence, privacy, disclosure, retention, correction, revocation, incident-response, and overlap boundaries pass review. |
| Provenance/rollback | PARTIAL | Containment records exist; approved path/hash manifest, source-to-target map, candidate archives, signed provenance, rollback drill, and restored-state verification remain absent. |
| Approval | PENDING | Explicit release and publication approval only after every blocking gate passes. |

## Required artifacts

- Approved disposition and destination, consolidated owner, archive, or hold record.
- Complete exact file-level path-and-hash disposition manifest.
- Reviewed component and overlap inventory bound to its exact source generation.
- Source-to-target commit map or immutable archive identity with authenticity evidence.
- Product directive, supported-platform matrix, threat model, authorized-use policy, and repository-overlap decision.
- License and third-party dependency/data/firmware provenance record.
- Representative positive, negative, adversarial, malformed-input, duplicate, conflict, stale, replay, wrong-device, correction, revocation, withdrawal, extension, privilege, network, and isolation fixtures.
- Hardware-lab results, uncertainty and false-positive/false-negative characterization, performance limits, and unsupported-platform behavior.
- Reproducible build/test/documentation logs, retained workflow artifacts, SBOM, checksums, vulnerability results, source archive, signed provenance, review record, rollback instructions, and restored-state evidence.
- Publication manifest, controlled-route inventory, correction/withdrawal propagation evidence, and resulting-public-state verification if Pages is ever approved.

## Rollback and withdrawal criteria

Reject, withdraw, or hold a candidate if ownership remains ambiguous; any component or path lacks a disposition; implementation continues in `Misc` without approval; copied history cannot be distinguished from destination-authored work; duplicate authority surfaces remain active; public documentation implies release; license or data rights are unresolved; trusted baselines lack independent provenance; privileged or disruptive behavior is not fail-closed; representative and adversarial validation is absent; claims exceed evidence; builds or checks cannot be reproduced; correction or revocation cannot reach controlled consumers; provenance is incomplete; rollback cannot be verified; or the restored state cannot be independently verified. Preserve source history, failed evidence, limitations, supersession, and disposition records.

## Unresolved blockers

- Architect decision for dedicated migration, modular consolidation, evidence-preserving retirement/archive, or continued hold.
- Complete exact file-level evidence, disposition, ownership, and source-to-target history manifest.
- Accepted resolution for every O01-O10 overlap edge and required compatibility witness.
- Intended user, supported-platform, license, naming, package-identity, and version-lineage approval.
- Explicit approval of any future GitHub Pages publication or other public artifact.
- Exact-candidate clean build, complete tests, security review, representative hardware and adversarial validation, retained artifacts, SBOM/checksums, provenance, and rollback/restoration drill.
- Trusted firmware and data-source governance, credential/privilege model, extension boundary, uncertainty characterization, incident/disclosure policy, retention, and correction/revocation propagation.

## Release log

- 2026-07-16 — Established `Misc` as a documentation-first incubation repository with no implementation or deployment authority.
- 2026-07-16 — Detected the addition of the XYZ prototype, CI, packaging, compliance documentation, and Pages capability before incubation approval.
- 2026-07-16 — Preserved the prototype as unaccepted evidence and blocked release pending containment, ownership or retirement, license, validation, security, publication, provenance, and explicit approval.
- 2026-07-16 — Disabled automatic Pages publication and retained a fail-closed explicit-readiness gate.
- 2026-07-23 — Added the incubation documentation front door and punch list; the release decision remains blocked and unchanged.
- 2026-07-24 — Added the current-head exit and migration playbook and synchronized release gates without selecting a disposition or changing authority.
- 2026-07-24 — Added the component-family and portfolio-overlap inventory; release remains blocked pending exact path-level disposition, accepted ownership, compatibility witnesses, validation, and explicit approval.

## FYSA-120 mapping

Applied categories: `CAT-011`, `CAT-012`, `CAT-013`, `CAT-017`, `CAT-018`, `CAT-019`, `CAT-031`, `CAT-032`, `CAT-040`, `CAT-052`, and `CAT-054`.

Proposed non-authoritative refinements:

- **`040-P — Incubation exit, authority-neutral migration, modular consolidation, and evidence-preserving retirement`**.
- **`013-M — Incubated component-family inventories, cross-repository overlap ledgers, and disposition-safe ownership graphs`**.

Taxonomy membership does not establish approval or competence.
