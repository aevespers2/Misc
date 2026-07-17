# Release Plan

## Current Decision

Status: `BLOCKED — INCUBATION CONTRACT AND RELEASE EVIDENCE REQUIRED`

`Misc` is a non-authoritative holding repository for bounded experimental proposals. The repository contains an initial task chain and changelog defining the incubation boundary, but it has no `punchlist.md`, no repository-health evidence, no retained CI or status-check evidence for an immutable release candidate, and no approved intake/exit contract. No implementation, package, service, deployment, or production capability is eligible for release.

## Versioning

- Scheme: Semantic Versioning for approved documentation contracts and any later isolated experiment artifacts.
- First eligible candidate: `0.0.1-incubation-charter`.
- The first candidate is documentation-only and grants no execution, network, credential, publication, or deployment authority.
- Each later experiment requires its own proposal identifier and prerelease version until promoted to an approved owning repository or retired.
- Tag only one immutable reviewed commit after all applicable gates pass.

## Release Scope

The first candidate may include only:

- the approved repository purpose and non-goals;
- an intake template with proposal ID, owner, intended user, problem statement, dependencies, and overlap review;
- evidence-state, data, privacy, license, credential, network, resource, and stop-condition fields;
- experiment directory and naming conventions;
- validation or falsification requirements;
- promotion, migration, archival, deletion, provenance, and rollback rules;
- a completed release punch list and repository-health record for the exact candidate commit.

## Explicit Exclusions

- Executable experiments, packages, services, deployments, or public capability claims.
- Credentials, sensitive datasets, unrestricted networking, remote mutation, autonomous publication, or production integrations.
- Work that duplicates or overrides ownership in QSO, Bridge, VTX, Alistaire, AionUi, temporal-invariant, or other established repositories.
- Promotion of an experiment without a dedicated approved destination, retained evidence, and migration/rollback plan.

## Selected Completed Work

Candidate inputs currently present:

- a task chain defining the incubation repository role, first objective, success criteria, non-goals, priority, and builder rules;
- a changelog recording the documentation-only product boundary and absence of authorized deployment.

These items are not selected as releasable completed work until the intake/exit contract is approved, a punch list exists and is completed, documentation is independently verified, provenance is retained, and the exact candidate receives release approval.

## Planned Changelog Entries

- `Added`: approved incubation intake, evidence, ownership-conflict, promotion, migration, archival, and retirement contract.
- `Security`: explicit credential, network, data, privacy, license, resource, and stop boundaries.
- `Documentation`: experiment naming, validation evidence, limitations, provenance, and disposition instructions.
- `Release`: documentation-only charter artifact, checksums, source archive, repository-health report, rollback record, and approval decision.
- `Excluded`: implementation and deployment authority before a separately approved experiment proposal.

## Acceptance Gates

| Gate | Status | Requirement |
|---|---|---|
| Product approval | PENDING | Architect approves the incubation purpose, intake fields, exit criteria, and repository-conflict policy. |
| Task completion | FAIL | P0 is `DONE` with evidence and a repository punch list exists and is complete for the candidate. |
| Tests/validation | NO EVIDENCE | Templates and rules are checked for completeness, deterministic identifiers, invalid/missing-field rejection, and promotion/retirement decision coverage. |
| Security/privacy | NO EVIDENCE | Credential, network, data, privacy, license, resource, publication, and remote-mutation boundaries are reviewed and fail closed. |
| Documentation | PARTIAL | Task chain and changelog exist; intake template, operating instructions, examples, limitations, and disposition workflow are missing or unverified. |
| Repository ownership | PENDING | The charter proves this repository does not duplicate or supersede established repository authority. |
| Provenance | NO EVIDENCE | Exact commit, review record, commands/results, artifact hashes, repository URL, and approval are retained. |
| CI/status checks | NO EVIDENCE | No immutable release candidate has retained status checks or workflow evidence. |
| Rollback | NO EVIDENCE | Rejected proposals and charter changes can be reverted without losing history, evidence, or disposition records. |
| Approval | PENDING | Explicit release approval only after every blocking gate passes. |

## Artifact Requirements

- Approved incubation charter and machine-readable or structured intake template.
- Completed `punchlist.md` and repository-health report tied to the exact candidate commit.
- Validation fixtures for complete, incomplete, overlapping, unsafe, unlicensed, credential-dependent, and unbounded proposals.
- Security/privacy/license boundary review and repository-ownership comparison record.
- Promotion, migration, archive, retirement, and rollback examples.
- Source archive, SHA-256 checksums, provenance manifest, review/approval record, and release notes.

## Rollback Criteria

Reject or withdraw the candidate if the repository purpose remains ambiguous; an experiment can bypass intake or approval; ownership overlaps an established repository; required evidence, data rights, privacy, license, credential, network, resource, or stop fields are missing; invalid proposals do not fail closed; implementation or deployment authority is implied; provenance or hashes are incomplete; documentation cannot be reproduced; or promotion/retirement cannot preserve history and limitations. Restore the previous reviewed commit and retain the rejected candidate, findings, and disposition record.

## Unresolved Blockers

- The incubation intake and exit contract requires approval.
- `punchlist.md` is absent.
- No repository-health, validation, security/privacy, documentation-verification, provenance, checksum, artifact, or rollback evidence exists.
- No immutable release candidate has retained CI workflow or status-check evidence.
- No proposal has yet demonstrated the complete intake-to-promotion-or-retirement lifecycle.
- No release approver or accepted ownership-conflict disposition has been recorded.

## Release Log

- 2026-07-16 — Established `0.0.1-incubation-charter` as the first possible documentation-only candidate and held it blocked pending product approval and complete release evidence.
- 2026-07-16 — Recorded the missing punch list, absent repository-health/CI evidence, required artifacts, acceptance gates, rollback criteria, and prohibition on implementation or deployment authority.