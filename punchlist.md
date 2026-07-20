# Repository Punch List

This punch list tracks documentation, repository health, ownership, integration, validation, and release work for the `Misc` incubation repository and the retained XYZ / PhantomBlock prototype. It does not authorize implementation expansion.

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
| Add portable host-observation role | IN REVIEW | `portable-host-observation.md` maps PhantomBlock beneath Repository `0` while preserving Repository `1` authority and non-capabilities. |
| Add JusticeForMe overlap decision guide | IN REVIEW | `host-observation-overlap.md` defines candidate domains, shared envelope, deduplication, conflict resolution, fixtures, and migration options. |
| Add obstruction and gluing analysis | IN REVIEW | `obstruction-and-gluing.md` records identity, authority, evidence, privacy, temporal, incident, and rollback incompatibilities plus pairwise and triple-overlap witnesses. |
| Add bounded developer onboarding and contribution guidance | IN REVIEW | `developer-onboarding.md` and `CONTRIBUTING.md` pass documentation review. |
| Add ownership, promotion, consolidation, retirement, release, and rollback decision path | IN REVIEW | `ownership-and-release.md` and overlap guides reviewed by Architect. |
| Build Pages documentation with strict link and navigation checks | OPEN | Retained `mkdocs build --strict` result tied to the exact PR head. |
| Verify documentation accessibility basics | OPEN | Heading order, link labels, tables, contrast/theme defaults, keyboard navigation, and diagram alternatives reviewed. |

## P1 — ownership and product definition

| Item | Status | Acceptance evidence |
|---|---|---|
| Select dedicated owning repository, approved consolidation, or retirement | BLOCKED | Architect decision record. |
| Approve or reject the proposed Repository `0` specialist observation-adapter role | BLOCKED | Portfolio architecture decision. |
| Resolve JusticeForMe overlap through separate-adapter, merge, or retirement decision | BLOCKED | Approved host-observation ownership record. |
| Approve canonical product, repository, package, CLI, schema, field, and version identities | BLOCKED | Charter and migration/consolidation record. |
| Identify maintainer, security contact, release authority, publication authority, incident owner, and revoker | BLOCKED | Ownership record. |
| Define intended users and authorized-use policy | BLOCKED | Approved product directive. |
| Define supported and unsupported platforms | BLOCKED | Platform and privilege matrix with `UNKNOWN` behavior. |
| Resolve overlap with Repository `0`, Repository `1`, JusticeForMe, Bridge, AionUi, QSO-STUDIO, verification, security, and portfolio Pages repositories | BLOCKED | Repository-boundary and gluing decision. |
| Select license and approve dependency, data, firmware, PCAP, and documentation rights | BLOCKED | License and provenance review. |
| Preserve full histories during migration, consolidation, or archive | BLOCKED | Verified procedure and commit mapping. |

## P1-G — cross-repository gluing

| Item | Status | Acceptance evidence |
|---|---|---|
| Assign device-identity and ownership-scope contract owner | BLOCKED | Versioned identity schema and lifecycle approved. |
| Assign baseline-policy and firmware-manifest authority | BLOCKED | Signed baseline identity, applicability, update, and revocation rules. |
| Assign canonical host-observation envelope and field-vocabulary owner | BLOCKED | Versioned package accepted by Repository `0`, Repository `1`, and adapter owners. |
| Define JusticeForMe and PhantomBlock collector domains | BLOCKED | Non-overlapping charter or approved modular consolidation. |
| Define duplicate, corroborating, conflicting, partial, stale, replayed, and wrong-device semantics | BLOCKED | Deterministic rules and retained fixtures. |
| Approve PhantomBlock → Repository `0` evidence-envelope contract | BLOCKED | Schema, artifact binding, completeness, limitations, privacy, and malformed-input fixtures. |
| Approve Repository `0` → Repository `1` proposal route | BLOCKED | Canonical quarantine route and stale/replay/wrong-device fixtures. |
| Approve capability, receipt, revocation, correction, and checkpoint ownership | BLOCKED | Repository `1` authority contract and shared fixtures. |
| Define temporal and ordering semantics | BLOCKED | Source time, receive time, uncertainty, replay, correction, and revocation order rules. |
| Define Bridge transport and interface-display boundaries | BLOCKED | Round-trip integrity, minimization, revocation, and non-actionable UI fixtures. |
| Define incident freeze, evidence preservation, lost-device recovery, and bounded restart | BLOCKED | Portfolio state machine and tabletop evidence. |
| Validate pairwise and triple-overlap witnesses | BLOCKED | Immutable fixture suite proving meaning remains consistent across all documented paths. |

## P2 — security and validation candidate

| Item | Status | Acceptance evidence |
|---|---|---|
| Establish immutable candidate commit in approved owner | BLOCKED | Candidate identifier and source archive. |
| Reproduce clean installation and tests | BLOCKED | Retained logs with environment and dependency versions. |
| Produce SBOM, checksums, and vulnerability review | BLOCKED | Candidate artifacts and reports. |
| Approve trusted-baseline governance | BLOCKED | Source, signature, applicability, update, revocation, and licensing policy. |
| Validate representative hardware and firmware | BLOCKED | Approved test matrix and retained results. |
| Add negative, adversarial, malformed, incomplete, duplicate, conflicting, stale, replayed, wrong-device, and unsupported fixtures | BLOCKED | Fixture inventory and results. |
| Characterize false positives and false negatives | BLOCKED | Methods, corpus, results, and limitations. |
| Review PCAP parser limits and privacy handling | BLOCKED | Security and data-handling report. |
| Review extension provenance, isolation, and resource controls | BLOCKED | Extension security assessment. |
| Review dashboard authentication, exposure, retention, and tenancy boundary | BLOCKED | Approved deployment design or explicit local-only restriction. |
| Verify dry-run response and any approved active-response rollback | BLOCKED | Idempotency, audit, capability, rollback, and partial-failure evidence. |
| Complete threat model and incident/disclosure plan | BLOCKED | Independent review and closure record. |

## P3 — release and publication

| Item | Status | Acceptance evidence |
|---|---|---|
| Align all public claims with candidate evidence | BLOCKED | Claims-to-evidence matrix. |
| Build source, package, image, and documentation artifacts reproducibly where approved | BLOCKED | Retained artifacts and logs. |
| Sign provenance and record approval chain | BLOCKED | Signature and attestation bundle. |
| Verify deployment, migration, consolidation, retirement, and rollback procedures | BLOCKED | Staged drills and results. |
| Approve Pages, package, image, or service publication targets | BLOCKED | Explicit publication decision. |
| Record support, vulnerability response, withdrawal, correction, revocation, and deprecation policies | BLOCKED | Operational ownership documents. |
| Mark `release.md` ready only after every blocking gate passes | BLOCKED | Architect and independent reviewer approval. |

## Documentation health checklist

- [ ] All Pages navigation targets exist.
- [ ] `mkdocs build --strict` passes at the exact PR head.
- [ ] Root README links resolve.
- [ ] Mermaid diagrams render or have meaningful surrounding text.
- [ ] No page claims certification, authorization, release, or comprehensive detection.
- [ ] Current commands and package metadata match source.
- [ ] Proposed schemas and controls are labeled as proposals.
- [ ] Sensitive-data and authorization warnings are prominent.
- [ ] `taskchain.md`, `release.md`, `punchlist.md`, and `changelog.md` describe the same current posture.
- [ ] Migration, consolidation, and retirement remain available outcomes.
- [ ] Repository `0` / Repository `1` roles remain proposals until approved.
- [ ] JusticeForMe and PhantomBlock overlap is explicit rather than silently duplicated.
- [ ] Duplicate evidence cannot be counted as independent corroboration without a witness.
- [ ] Observation cannot self-authorize response.

## Evidence log

Add dated entries only when evidence is retained and tied to an immutable commit, pull request, workflow, artifact, or decision record.

- 2026-07-19 — Documentation milestone prepared on a feature branch: expanded repository overview; revised Pages landing and architecture; added repository boundaries, design contracts, developer onboarding, ownership/release guidance, contribution rules, and this punch list. Validation and architectural gates remain blocked pending review and retained build evidence.
- 2026-07-20 — Added an obstruction and gluing ledger with eighteen active incompatibilities, a proposed bounded Repository `0` adapter role, Repository `1` authority boundary, evidence-envelope proposal, and required pairwise and triple-overlap witnesses. No implementation or authority changed.
- 2026-07-20 — Added portable host-observation and JusticeForMe overlap guides, updated Pages navigation, and introduced shared field, deduplication, conflict, privacy, and compatibility gates without changing runtime or release scope.
