# Release Plan

## Current decision

Status: `BLOCKED — SCOPE CONFLICT, OWNERSHIP, VALIDATION, LICENSING, AND PUBLICATION APPROVAL REQUIRED`

`Misc` remains a non-authoritative holding repository at portfolio priority P4. The XYZ / PhantomBlock code, tests, workflows, packaging definitions, compliance mappings, and documentation are preserved as prototype evidence. They do not establish an accepted product, operational detector, supported-platform claim, certification, authorization, release, publication, or deployment.

The next release-related decision is not a release. An Architect must approve migration to a dedicated owning repository, retirement/archive with provenance and limitations, or a continued hold with explicit reopening conditions. No package, live image, dashboard, documentation site, switch adapter, service, or integration is eligible for release from `Misc` while that disposition and the gates below remain unresolved.

## Documentation candidate

The repository now has a front door, incubation-status guide, accessible architecture, safe onboarding, developer guide, punch list, task chain, release plan, and changelog. These materials improve decision readiness and evidence classification only. They do not convert the prototype into an accepted product or make Pages publication appropriate.

## Evidence classification

### Implemented prototype artifacts

- Python package `xyz-firmware-defense` version `0.3.0` under `phantomblock/`.
- CLI, dashboard/API, collection and heuristic-assessment code, extension interface, and dry-run isolation abstraction.
- Unit-test source, CI configuration, live-image definition, standalone-binary/SBOM build scripts, example trusted-baseline configuration, compliance mappings, and MkDocs documentation.
- GitHub Pages workflow retained as a deployment capability, but automatic `main` publication is disabled; it is manual-only and fails closed unless this file is explicitly marked `READY`.
- Historical deployment-review and containment records.
- A historical pull-request workflow in which editable installation, Ruff, and Pytest completed successfully.

### Not established

- Current release-candidate or resulting-default-head validation evidence.
- Retained release artifacts from the historical lint/test run.
- Representative BIOS/UEFI, NIC, BMC, SSD, chipset, operating-system, switch, or PCAP validation.
- False-positive/false-negative characterization, parser fuzzing, adversarial corpus, Secure Boot or measured-boot validation, signed provenance, or reproducible release evidence.
- Trusted firmware-source governance, approved credentials or privilege model, extension security review, production isolation safety, incident-response integration, or rollback verification.
- License approval, CMMC status, STIG approval, Army authorization, Authority to Operate, certification, or comprehensive implant-detection assurance.

## Versioning

- Existing `0.3.0` package metadata is prototype metadata, not an approved release version.
- A dedicated owning repository must select the authoritative name, package identity, version lineage, license, compatibility policy, and deprecation route.
- The first eligible release candidate must be generated from one immutable reviewed commit after migration and all applicable gates pass.
- Tags, packages, images, Pages publication, or release artifacts must not imply acceptance before explicit approval.

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

## Acceptance gates

| Gate | Status | Requirement |
|---|---|---|
| Scope containment | REVIEW | Manual-only Pages gate remains fail-closed; feature, package, image, and deployment promotion remain frozen. |
| Documentation integrity | REVIEW | README, MkDocs pages, `taskchain.md`, `punchlist.md`, `release.md`, and `changelog.md` agree and pass exact-head checks. |
| Ownership/disposition | FAIL | Architect approves one dedicated repository and owner, retirement/archive, or continued hold with reopening conditions. |
| Product definition | FAIL | Intended user, authorized-use boundary, supported and unsupported platforms, claims, limitations, and non-goals are approved. |
| Repository overlap | FAIL | Overlap with existing security, Bridge, AionUi, verification, and QSO repositories is inventoried and dispositioned. |
| License and data rights | FAIL | License and dependency, firmware, PCAP, documentation, and third-party-content rights are approved. |
| Threat model | PARTIAL | Documentation records privilege, extension, firmware, network, dashboard, packaging, and publication risks; independent review remains absent. |
| Validation | NO ACCEPTED EVIDENCE | Representative hardware, negative/adversarial fixtures, fuzzing, uncertainty, false-positive/negative analysis, and isolation rollback pass. |
| Dependencies/build | UNVERIFIED | Clean environments reproduce installation, tests, documentation, binary/image outputs, SBOMs, and checksums. |
| CI/status checks | PARTIAL | Historical checks exist; one immutable current candidate must reproduce complete checks and retain artifacts. |
| Accessibility | REVIEW | Diagrams have equivalent prose and documentation routes are structured; generated-site accessibility evidence remains required. |
| Publication | CONTAINED | Automatic publication is disabled; explicit Pages target, review, and approval remain required. |
| Security/privacy | FAIL | Credential, privilege, network, firmware, evidence, privacy, disclosure, retention, and incident-response boundaries pass review. |
| Provenance/rollback | PARTIAL | Containment records exist; file-level manifest, candidate archives, hashes, signed provenance, migration/retirement record, runtime rollback, and resulting-state verification remain absent. |
| Approval | PENDING | Explicit release and publication approval only after every blocking gate passes. |

## Required artifacts

- Approved ownership and migration, retirement, or hold record.
- File-level prototype and documentation manifest with exact source identities and evidence classes.
- Product directive, supported-platform matrix, threat model, authorized-use policy, and repository-overlap decision.
- License and third-party dependency/data/firmware provenance record.
- Representative positive, negative, adversarial, malformed-input, extension, privilege, network, and isolation fixtures.
- Hardware-lab results, uncertainty and false-positive/false-negative characterization, performance limits, and unsupported-platform behavior.
- Reproducible build/test/documentation logs, retained workflow artifacts, SBOM, checksums, vulnerability results, source archive, signed provenance, review record, and rollback instructions.
- Publication manifest, controlled-route inventory, correction/withdrawal propagation evidence, and resulting-public-state verification if Pages is ever approved.

## Rollback and withdrawal criteria

Reject, withdraw, or hold a candidate if ownership remains ambiguous; implementation continues in `Misc` without approval; public documentation implies release; license or data rights are unresolved; trusted baselines lack independent provenance; privileged or disruptive behavior is not fail-closed; extension boundaries permit uncontrolled mutation; representative and adversarial validation is absent; claims exceed evidence; builds or checks cannot be reproduced; correction cannot reach controlled consumers; provenance is incomplete; or rollback cannot be verified. Preserve source history, failed evidence, limitations, supersession, and disposition records.

## Unresolved blockers

- Architect decision to migrate XYZ into a dedicated owning repository, retire/archive it, or continue a documented hold.
- Complete file-level evidence, ownership, and repository-overlap inventory.
- Intended user, supported-platform, license, naming, package-identity, and version-lineage approval.
- Explicit approval of any future GitHub Pages publication or other public artifact.
- Exact-candidate clean build, complete tests, security review, representative hardware and adversarial validation, retained artifacts, SBOM/checksums, provenance, and rollback drill.
- Trusted firmware and data-source governance, credential/privilege model, extension boundary, uncertainty characterization, incident/disclosure policy, retention, and correction propagation.

## Release log

- 2026-07-16 — Established `Misc` as a documentation-first incubation repository with no implementation or deployment authority.
- 2026-07-16 — Detected the addition of the XYZ prototype, CI, packaging, compliance documentation, and Pages capability before incubation approval.
- 2026-07-16 — Preserved the prototype as unaccepted evidence and blocked release pending containment, ownership or retirement, license, validation, security, publication, provenance, and explicit approval.
- 2026-07-16 — Disabled automatic Pages publication and retained a fail-closed explicit-readiness gate.
- 2026-07-23 — Added the incubation documentation front door and punch list; the release decision remains blocked and unchanged.

## FYSA-120 mapping

Applied categories: `CAT-012`, `CAT-013`, `CAT-017`, `CAT-019`, `CAT-031`, `CAT-040`, `CAT-052`, and `CAT-054`. Proposed subdivision `040-H` is a planning gap only and grants no authority.
