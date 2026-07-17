# Release Plan

## Current Decision

Status: `BLOCKED — SCOPE CONFLICT, OWNERSHIP, VALIDATION, AND PUBLICATION APPROVAL REQUIRED`

`Misc` remains a non-authoritative holding repository at portfolio priority P4. Fifteen commits added the XYZ defensive firmware-assessment prototype before the documentation-first incubation contract was approved. The code, tests, workflows, packaging definitions, compliance mappings, and documentation are preserved as prototype evidence; they do not establish an accepted product, operational detector, certification, authorization, release, or deployment.

The next release-related decision is an Architect ownership decision: migrate XYZ and its full history into a dedicated approved repository, or retire/archive it with limitations preserved. No package, live image, dashboard, documentation site, switch adapter, service, or integration is eligible for release from `Misc` while that decision and the gates below remain unresolved.

## Evidence Classification

### Implemented prototype artifacts

- Python package `xyz-firmware-defense` version `0.3.0` under `phantomblock/`.
- CLI, dashboard/API, collection and heuristic assessment code, extension interface, and dry-run isolation abstraction.
- Unit-test source, CI workflow configuration, live-image definition, standalone-binary/SBOM build scripts, example trusted-baseline configuration, compliance mappings, and MkDocs documentation.
- GitHub Pages workflow configured to publish documentation from `main` with Pages and OIDC write permissions.
- Merged PR #1 head `8a56fc7f2fc0b2b0af3c7b47e06bfad70546b48d` has one successful `PhantomBlock CI` run (`29553292217`) in which editable installation, Ruff, and Pytest completed successfully.

### Not established

- Passing status checks or workflow runs for the current release-planning head; the observed current head has no attached status records or pull-request workflow run.
- Retained test artifacts from the successful PR run; the run published no workflow artifacts and does not certify a release candidate after the subsequent documentation, branding, packaging, and publication commits.
- Representative BIOS/UEFI, NIC, BMC, SSD, chipset, operating-system, switch, or PCAP validation.
- False-positive/false-negative characterization, parser fuzzing, adversarial corpus, Secure Boot or measured-boot validation, signed provenance, or reproducible release evidence.
- Trusted firmware-source governance, approved credentials or privilege model, extension security review, production isolation safety, incident-response integration, or rollback verification.
- License approval, CMMC status, STIG approval, Army authorization, Authority to Operate, certification, or comprehensive implant-detection assurance.

## Selected Completed Work

No work is selected for release. The merged prototype and its successful PR-level lint/test run are retained as implementation evidence only. They remain excluded from a release candidate until ownership, repository scope, licensing, security, validation, publication, provenance, and rollback gates are approved and reproduced at one immutable candidate commit.

## Versioning

- Existing `0.3.0` package metadata is prototype metadata, not an approved release version.
- A dedicated owning repository must select the authoritative name, package identity, version lineage, license, and compatibility policy.
- The first eligible release candidate must be generated from one immutable reviewed commit after migration and all applicable gates pass.
- Tags, packages, images, Pages publication, or release artifacts must not imply acceptance before explicit approval.

## Candidate Scope After Ownership Approval

A future candidate may include only the explicitly reviewed subset of:

- passive inventory and evidence collection;
- firmware and baseline verification with independently governed trusted sources;
- bounded kernel and management-channel heuristics;
- offline external-PCAP analysis;
- read-only dashboard and machine-readable reports;
- reviewed passive extension interfaces;
- disruptive isolation only behind a separately approved, authenticated, allowlisted, audited, dry-run-first interface with rollback verification;
- reproducible packaging, SBOM, checksums, signed provenance, and documentation whose claims match retained evidence.

## Explicit Exclusions

- Unauthorized assessment, credential bypass, exploitation, firmware flashing, destructive remediation, covert collection, unrestricted networking, or default-active switch isolation.
- Customer data, credentials, sensitive firmware images, exploit details, or security findings in the public repository.
- Certification, DoD/Army authorization, operational-readiness, or comprehensive-detection claims unsupported by formal evidence.
- Permanent production ownership by `Misc` or bypass of existing Bridge, AionUi, verification, QSO, or other repository boundaries.

## Planned Changelog Entries

- `Added`: the specifically approved passive assessment, reporting, and reviewed extension subset after migration to its owning repository.
- `Security`: trusted-baseline governance, privilege and credential boundaries, parser and extension hardening, network restrictions, isolation safeguards, vulnerability results, and disclosure limitations.
- `Validation`: supported-platform matrix, representative hardware results, adversarial and malformed-input fixtures, false-positive/false-negative characterization, performance limits, and unsupported-platform behavior.
- `Documentation`: authorized-use policy, non-goals, evidence classifications, operational limits, incident handling, recovery, and rollback.
- `Release`: authoritative package/version identity, immutable source commit, build/test reports, SBOM, source and binary/image artifacts where approved, checksums, signed provenance, migration record, and approval decision.

## Acceptance Gates

| Gate | Status | Requirement |
|---|---|---|
| Scope containment | REVIEW | Freeze feature, packaging, publication, and deployment promotion while preserving the current prototype and history. |
| Ownership | FAIL | Architect approves one dedicated repository and owner, or records retirement/archive. |
| Product definition | FAIL | Intended user, authorized-use boundary, supported platforms, claims, limitations, and non-goals are approved. |
| Repository overlap | FAIL | Compare and disposition overlap with existing security, Bridge, AionUi, verification, and QSO repositories. |
| Punch list / health baseline | FAIL | Add `punchlist.md` and a repository-health report tied to the exact candidate commit; neither currently exists as accepted evidence. |
| License and data rights | FAIL | Select a license and approve dependencies, firmware sources, PCAP handling, documentation, and third-party content. |
| Threat model | PARTIAL | Existing documentation is reviewed against privilege, extension, firmware, network, dashboard, packaging, and publication risks. |
| Validation | NO ACCEPTED EVIDENCE | Representative hardware, negative/adversarial fixtures, fuzzing, false-positive/negative analysis, and isolation rollback pass. |
| Dependencies/build | UNVERIFIED | Clean environments reproduce installation, tests, binary/image outputs, SBOMs, and checksums. |
| CI/status checks | PARTIAL | A prior merged PR head passed editable install, Ruff, and Pytest, but the current planning head has no attached checks and the successful run retained no release artifacts. One immutable candidate must reproduce complete checks and artifacts. |
| Publication | FAIL | GitHub Pages and other public outputs are explicitly approved or disabled. |
| Security/privacy | FAIL | Credential, privilege, network, firmware, evidence, privacy, disclosure, and incident-response boundaries pass review. |
| Provenance/rollback | NO EVIDENCE | Source archive, hashes, signed provenance, migration record, rollback, and retirement procedure are retained. |
| Approval | PENDING | Explicit release approval only after every blocking gate passes. |

## Required Artifacts

- Approved ownership and migration or retirement record.
- Product directive, supported-platform matrix, threat model, authorized-use policy, and repository-overlap decision.
- License and third-party dependency/data/firmware provenance record.
- Complete punch list and repository-health report tied to the exact candidate commit.
- Representative positive, negative, adversarial, malformed-input, extension, privilege, network, and isolation fixtures.
- Hardware-lab results, false-positive/false-negative characterization, performance limits, and unsupported-platform behavior.
- Reproducible build/test logs, retained workflow artifacts, SBOM, checksums, vulnerability results, source archive, signed provenance, review record, and rollback instructions.

## Rollback Criteria

Reject or withdraw a candidate if ownership remains ambiguous; implementation continues in `Misc` without approval; public documentation implies release; license or data rights are unresolved; trusted baselines are derived from an assessed host or lack provenance; privileged or disruptive behavior is not fail-closed; extension boundaries permit uncontrolled mutation; representative and adversarial validation is absent; claims exceed evidence; builds or checks cannot be reproduced; provenance is incomplete; rollback cannot be verified; or an authorizing party declines deployment. Preserve source history, failed evidence, limitations, and disposition records.

## Unresolved Blockers

- Architect decision to migrate XYZ into a dedicated owning repository or retire/archive it.
- Missing `punchlist.md` and accepted repository-health evidence.
- Approval of intended user, authorized-use boundary, repository overlap, license, naming, package identity, and version lineage.
- Explicit decision to disable or approve automatic GitHub Pages publication and all other public artifacts.
- Exact-candidate clean build, complete tests, security review, representative hardware and adversarial validation, retained artifacts, SBOM/checksums, provenance, and rollback drill.
- Trusted firmware and data-source governance, credential/privilege model, extension boundary, false-positive/false-negative characterization, and incident/disclosure policy.

## Release Log

- 2026-07-16 — Established `Misc` as a documentation-first incubation repository with no implementation or deployment authority.
- 2026-07-16 — Detected the addition of the XYZ prototype, CI, packaging, compliance documentation, and automatic Pages publication before incubation approval.
- 2026-07-16 — Preserved the prototype as unaccepted evidence and blocked release pending containment, dedicated ownership or retirement, license, validation, security, publication, provenance, and explicit approval.
- 2026-07-16 — Reclassified CI evidence as partial after verifying one successful merged-PR lint/test run with no retained artifacts; no current-head or release-candidate evidence was established.