# Release Plan

## Current decision

Status: `BLOCKED — SCOPE CONFLICT, OWNERSHIP, VALIDATION, AND PUBLICATION APPROVAL REQUIRED`

`Misc` remains a non-authoritative holding repository at portfolio priority P4. Fifteen commits added the XYZ / PhantomBlock defensive firmware-assessment prototype before the documentation-first incubation contract was approved. The code, tests, workflows, packaging definitions, compliance mappings, and documentation are preserved as prototype evidence; they do not establish an accepted product, operational detector, certification, authorization, release, or deployment.

The next release-related decision is an Architect ownership decision: migrate XYZ and its full history into a dedicated approved repository, or retire/archive it with limitations preserved. No package, live image, dashboard, documentation site, switch adapter, service, or integration is eligible for release from `Misc` while that decision and the gates below remain unresolved.

## Documentation milestone

A documentation-only containment package now provides:

- an expanded repository overview and Pages landing page;
- repository and portfolio boundary documentation;
- architecture, runtime, state, and trust-zone diagrams;
- design contracts and claims-to-evidence guidance;
- bounded developer onboarding and contribution rules;
- an ownership, migration, retirement, release, and rollback decision path;
- a repository punch list and documentation-health checklist;
- updated Pages navigation and Mermaid support.

This milestone improves reviewability. It does not change runtime behavior, supported platforms, package authority, publication authorization, or release status. Documentation remains in review until strict-build evidence and architectural approval are retained.

## Evidence classification

### Implemented prototype artifacts

- Python package `xyz-firmware-defense` version `0.3.0` under `phantomblock/`.
- CLI, dashboard/API, collection and heuristic assessment code, extension interface, and dry-run isolation abstraction.
- Unit-test source, CI workflow configuration, live-image definition, standalone-binary/SBOM build scripts, example trusted-baseline configuration, compliance mappings, and MkDocs documentation.
- GitHub Pages workflow retained as a deployment capability, but automatic `main` publication was removed by commit `c1d5a1d8dc0d729cdb077c0dcac11dc582c2488c`; it is manual-only and fails closed unless this file is explicitly marked `READY`.
- Deployment review and containment evidence are recorded in `deploy.md` at commit `8f82b63c02f21e4c9cea0530fb86c1db7e42f099`.
- Merged PR #1 head `8a56fc7f2fc0b2b0af3c7b47e06bfad70546b48d` has one successful `PhantomBlock CI` run (`29553292217`) in which editable installation, Ruff, and Pytest completed successfully.
- A documentation milestone exists on a feature branch; its changes are review evidence only until the branch head receives retained strict-build and review results.

### Not established

- Passing status checks or workflow runs for the current documentation/release-planning head.
- Retained test or documentation artifacts for the current head.
- Representative BIOS/UEFI, NIC, BMC, SSD, chipset, operating-system, switch, or PCAP validation.
- False-positive/false-negative characterization, parser fuzzing, adversarial corpus, Secure Boot or measured-boot validation, signed provenance, or reproducible release evidence.
- Trusted firmware-source governance, approved credentials or privilege model, extension security review, production isolation safety, incident-response integration, or rollback verification.
- License approval, CMMC status, STIG approval, Army authorization, Authority to Operate, certification, or comprehensive implant-detection assurance.

## Selected completed work

No work is selected for release. The merged prototype, prior PR-level lint/test run, publication containment, and documentation foundation are retained as implementation and review evidence only. They remain excluded from a release candidate until ownership, repository scope, licensing, security, validation, publication, provenance, and rollback gates are approved and reproduced at one immutable candidate commit.

## Versioning

- Existing `0.3.0` package metadata is prototype metadata, not an approved release version.
- A dedicated owning repository must select the authoritative product, repository, package, CLI, schema, and version lineage.
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
- disruptive isolation only behind a separately approved, authenticated, allowlisted, audited, dry-run-first interface with rollback verification;
- reproducible packaging, SBOM, checksums, signed provenance, and documentation whose claims match retained evidence.

## Explicit exclusions

- Unauthorized assessment, credential bypass, exploitation, firmware flashing, destructive remediation, covert collection, unrestricted networking, or default-active switch isolation.
- Customer data, credentials, sensitive firmware images, exploit details, or security findings in the public repository.
- Certification, DoD/Army authorization, operational-readiness, or comprehensive-detection claims unsupported by formal evidence.
- Permanent production ownership by `Misc` or bypass of existing Bridge, AionUi, verification, QSO, or other repository boundaries.

## Planned changelog entries for a future approved owner

- `Added`: the specifically approved passive assessment, reporting, and reviewed extension subset after migration.
- `Security`: trusted-baseline governance, privilege and credential boundaries, parser and extension hardening, network restrictions, isolation safeguards, vulnerability results, and disclosure limitations.
- `Validation`: supported-platform matrix, representative hardware results, adversarial and malformed-input fixtures, false-positive/false-negative characterization, performance limits, and unsupported-platform behavior.
- `Documentation`: authorized-use policy, non-goals, evidence classifications, operational limits, incident handling, recovery, and rollback.
- `Release`: authoritative identity, immutable source commit, build/test reports, SBOM, source and binary/image artifacts where approved, checksums, signed provenance, migration record, and approval decision.

## Acceptance gates

| Gate | Status | Requirement |
|---|---|---|
| Scope containment | PARTIAL | Automatic Pages publication is disabled and the workflow fails closed; feature, packaging, and deployment promotion remain frozen while the prototype and history are preserved. |
| Documentation foundation | PARTIAL | Overview, architecture, boundaries, design, onboarding, contribution, decision, and punch-list documents exist on a review branch; strict build, accessibility review, link validation, and independent approval remain required. |
| Ownership | FAIL | Architect approves one dedicated repository and owner, or records retirement/archive. |
| Product definition | FAIL | Intended user, authorized-use boundary, supported platforms, claims, limitations, and non-goals are approved. |
| Repository overlap | FAIL | Compare and disposition overlap with existing security, Bridge, AionUi, verification, and QSO repositories. |
| Punch list / health baseline | PARTIAL | `punchlist.md` now records repository-health and release work; accepted health results tied to an immutable candidate remain absent. |
| License and data rights | FAIL | Select a license and approve dependencies, firmware sources, PCAP handling, documentation, and third-party content. |
| Threat model | PARTIAL | Existing documentation describes privilege, extension, firmware, network, dashboard, packaging, and publication risks; independent review and closure remain absent. |
| Validation | NO ACCEPTED EVIDENCE | Representative hardware, negative/adversarial fixtures, fuzzing, false-positive/negative analysis, and isolation rollback pass. |
| Dependencies/build | UNVERIFIED | Clean environments reproduce installation, tests, documentation, binary/image outputs, SBOMs, and checksums. |
| CI/status checks | PARTIAL | A prior merged PR head passed editable install, Ruff, and Pytest, but the current planning/documentation head has no attached checks or retained artifacts. One immutable candidate must reproduce complete checks and artifacts. |
| Publication | CONTAINED | Automatic publication is disabled; an explicit future Pages/publication target and approval remain required. |
| Security/privacy | FAIL | Credential, privilege, network, firmware, evidence, privacy, disclosure, and incident-response boundaries pass review. |
| Provenance/rollback | PARTIAL | Publication-containment commits and a deployment record exist; candidate archives, hashes, signed provenance, migration record, runtime rollback, and retirement procedure remain unverified. |
| Approval | PENDING | Explicit release approval only after every blocking gate passes. |

## Required artifacts

- Approved ownership and migration or retirement record.
- Product directive, supported-platform matrix, threat model, authorized-use policy, and repository-overlap decision.
- License and third-party dependency/data/firmware provenance record.
- Repository-health report and completed punch list tied to the exact candidate commit.
- Strict documentation build, link review, accessibility review, and claims-to-evidence review tied to the exact documentation head.
- Representative positive, negative, adversarial, malformed-input, extension, privilege, network, and isolation fixtures.
- Hardware-lab results, false-positive/false-negative characterization, performance limits, and unsupported-platform behavior.
- Reproducible build/test logs, retained workflow artifacts, SBOM, checksums, vulnerability results, source archive, signed provenance, review record, and rollback instructions.

## Rollback criteria

Reject or withdraw a candidate if ownership remains ambiguous; implementation continues in `Misc` without approval; public documentation implies release; license or data rights are unresolved; trusted baselines are derived from an assessed host or lack provenance; privileged or disruptive behavior is not fail-closed; extension boundaries permit uncontrolled mutation; representative and adversarial validation is absent; claims exceed evidence; builds or checks cannot be reproduced; provenance is incomplete; rollback cannot be verified; or an authorizing party declines deployment. Preserve source history, failed evidence, limitations, and disposition records.

For the current documentation branch, rollback is removal or reversion of the documentation commits. No runtime or deployment rollback is required because implementation and workflow authority are unchanged.

## Unresolved blockers

- Architect decision to migrate XYZ into a dedicated owning repository or retire/archive it.
- Approval of intended user, authorized-use boundary, repository overlap, license, naming, package identity, and version lineage.
- Explicit approval of any future GitHub Pages publication or other public artifact; automatic publication is currently disabled.
- Exact-head strict documentation build, accessibility/link review, and claims review.
- Exact-candidate clean build, complete tests, security review, representative hardware and adversarial validation, retained artifacts, SBOM/checksums, provenance, and rollback drill.
- Trusted firmware and data-source governance, credential/privilege model, extension boundary, false-positive/false-negative characterization, and incident/disclosure policy.

## Release log

- 2026-07-16 — Established `Misc` as a documentation-first incubation repository with no implementation or deployment authority.
- 2026-07-16 — Detected the addition of the XYZ prototype, CI, packaging, compliance documentation, and automatic Pages publication before incubation approval.
- 2026-07-16 — Preserved the prototype as unaccepted evidence and blocked release pending containment, dedicated ownership or retirement, license, validation, security, publication, provenance, and explicit approval.
- 2026-07-16 — Reclassified CI evidence as partial after verifying one successful merged-PR lint/test run with no retained artifacts; no current-head or release-candidate evidence was established.
- 2026-07-16 — Disabled automatic Pages publication, added a fail-closed explicit-release-readiness gate, and recorded deployment review evidence in `deploy.md`; no deployment ran.
- 2026-07-19 — Prepared a substantial documentation-only containment milestone on a feature branch. Release remains blocked, and the documentation gate remains partial pending strict-build evidence and review.