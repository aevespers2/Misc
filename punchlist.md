# Repository Punch List

This punch list tracks documentation, repository-health, ownership, validation, and release work for the `Misc` incubation repository and the retained XYZ / PhantomBlock prototype. It does not authorize implementation expansion.

Statuses: `OPEN` · `IN REVIEW` · `BLOCKED` · `DONE` · `NOT APPLICABLE`

## P0 — containment and documentation integrity

| Item | Status | Acceptance evidence |
|---|---|---|
| Preserve current prototype source and history without promoting it as a product | DONE | Source and commit history remain in `Misc`; task and release plans classify it as prototype evidence. |
| Disable automatic Pages publication | DONE | Pages workflow is manual-only and fails closed unless `release.md` is explicitly `READY`. |
| Publish a clear repository overview and status boundary | IN REVIEW | Expanded `README.md` and Pages landing page reviewed against planning records. |
| Document repository and portfolio boundaries | IN REVIEW | `repository-boundaries.md` reviewed and linked from Pages navigation. |
| Document architecture, trust zones, data flow, and runtime sequence | IN REVIEW | Architecture guide contains Mermaid diagrams and evidence classifications. |
| Document design contracts and claim language | IN REVIEW | `design-contracts.md` reviewed against current source and release posture. |
| Add bounded developer onboarding and contribution guidance | IN REVIEW | `developer-onboarding.md` and `CONTRIBUTING.md` pass documentation review. |
| Add ownership, promotion, retirement, release, and rollback decision path | IN REVIEW | `ownership-and-release.md` reviewed by Architect. |
| Build Pages documentation with strict link and navigation checks | OPEN | Retained `mkdocs build --strict` result tied to the PR head. |
| Verify documentation accessibility basics | OPEN | Heading order, link labels, tables, contrast/theme defaults, keyboard navigation, and diagram alternatives reviewed. |

## P1 — ownership and product definition

| Item | Status | Acceptance evidence |
|---|---|---|
| Select dedicated owning repository or approve retirement | BLOCKED | Architect decision record. |
| Approve canonical product, repository, package, CLI, and version identities | BLOCKED | Charter and migration record. |
| Identify maintainer, security contact, release authority, and publication authority | BLOCKED | Ownership record. |
| Define intended users and authorized-use policy | BLOCKED | Approved product directive. |
| Define supported and unsupported platforms | BLOCKED | Platform matrix. |
| Resolve overlap with Bridge, AionUi, verification, QSO, and portfolio Pages repositories | BLOCKED | Repository-boundary decision. |
| Select license and approve dependency, data, firmware, and documentation rights | BLOCKED | License and provenance review. |
| Preserve full history during migration or archive | BLOCKED | Verified migration/archive procedure and commit mapping. |

## P2 — security and validation candidate

| Item | Status | Acceptance evidence |
|---|---|---|
| Establish immutable candidate commit in approved owner | BLOCKED | Candidate identifier and source archive. |
| Reproduce clean installation and tests | BLOCKED | Retained logs with environment and dependency versions. |
| Produce SBOM, checksums, and vulnerability review | BLOCKED | Candidate artifacts and reports. |
| Approve trusted-baseline governance | BLOCKED | Source, signature, applicability, update, revocation, and licensing policy. |
| Validate representative hardware and firmware | BLOCKED | Approved test matrix and retained results. |
| Add negative, adversarial, malformed, and unsupported fixtures | BLOCKED | Fixture inventory and results. |
| Characterize false positives and false negatives | BLOCKED | Methods, corpus, results, and limitations. |
| Review PCAP parser limits and privacy handling | BLOCKED | Security and data-handling report. |
| Review extension provenance, isolation, and resource controls | BLOCKED | Extension security assessment. |
| Review dashboard authentication, exposure, retention, and tenancy boundary | BLOCKED | Approved deployment design or explicit local-only restriction. |
| Verify dry-run response and any approved active-response rollback | BLOCKED | Idempotency, audit, rollback, and partial-failure evidence. |
| Complete threat model and incident/disclosure plan | BLOCKED | Independent review and closure record. |

## P3 — release and publication

| Item | Status | Acceptance evidence |
|---|---|---|
| Align all public claims with candidate evidence | BLOCKED | Claims-to-evidence matrix. |
| Build source, package, image, and documentation artifacts reproducibly where approved | BLOCKED | Retained artifacts and logs. |
| Sign provenance and record approval chain | BLOCKED | Signature and attestation bundle. |
| Verify deployment and rollback procedures | BLOCKED | Staged drill and results. |
| Approve Pages, package, image, or service publication targets | BLOCKED | Explicit publication decision. |
| Record support, vulnerability response, withdrawal, and deprecation policies | BLOCKED | Operational ownership documents. |
| Mark `release.md` ready only after every blocking gate passes | BLOCKED | Architect and independent reviewer approval. |

## Documentation health checklist

- [ ] All Pages navigation targets exist.
- [ ] `mkdocs build --strict` passes at the PR head.
- [ ] Root README links resolve.
- [ ] Mermaid diagrams render or have meaningful surrounding text.
- [ ] No page claims certification, authorization, release, or comprehensive detection.
- [ ] Current commands and package metadata match source.
- [ ] Proposed schemas and controls are labeled as proposals.
- [ ] Sensitive-data and authorization warnings are prominent.
- [ ] `taskchain.md`, `release.md`, and `changelog.md` describe the same current posture.
- [ ] Migration and retirement remain available outcomes.

## Evidence log

Add dated entries only when evidence is retained and tied to an immutable commit, pull request, workflow, artifact, or decision record.

- 2026-07-19 — Documentation milestone prepared on a feature branch: expanded repository overview; revised Pages landing and architecture; added repository boundaries, design contracts, developer onboarding, ownership/release guidance, contribution rules, and this punch list. Validation and architectural gates remain blocked pending review and retained build evidence.