# Punch List

This list governs bounded documentation, evidence, ownership, migration, retirement, and rollback work for `Misc` and the preserved XYZ / PhantomBlock prototype. Completion of an item does not authorize release, deployment, assessment of third-party systems, certification, or operational integration.

States: `OPEN` · `IN PROGRESS` · `BLOCKED` · `REVIEW` · `DONE` · `NOT APPLICABLE`

## P0 — Containment and decision readiness

| Item | Status | Completion evidence |
|---|---|---|
| Publish a clear repository front door and status notice | DONE | `README.md` and `phantomblock/docs/incubation-status.md` agree on the holding posture. |
| Classify implementation, documentation, workflow, package, image, and compliance artifacts | REVIEW | Evidence classes are documented; file-level inventory remains incomplete. |
| Prevent automatic Pages publication | DONE | `.github/workflows/pages.yml` is manual-only and blocks unless `release.md` is explicitly `READY`. |
| Preserve the prototype and history without capability expansion | REVIEW | Current source is retained; future changes require scope checks. |
| Record intended users, authorized-use boundary, non-goals, and evidence limits | DONE | README, onboarding, threat model, and release plan contain the boundary. |
| Decide dedicated ownership, migration, retirement, or continued hold | BLOCKED | Explicit Architect disposition required. |

## P1 — Documentation and information architecture

| Item | Status | Completion evidence |
|---|---|---|
| Maintain a stable documentation front door | REVIEW | MkDocs navigation and internal-link validation pass at the exact candidate head. |
| Document architecture and trust boundaries with an equivalent prose alternative | REVIEW | `phantomblock/docs/architecture.md` passes documentation validation. |
| Provide safe onboarding before operational commands | REVIEW | `phantomblock/docs/onboarding.md` foregrounds authorization, privacy, and non-deployment boundaries. |
| Provide a developer guide for repository layout, tests, evidence, and change control | REVIEW | `phantomblock/docs/developer-guide.md` is linked from README and MkDocs. |
| Keep `taskchain.md`, `release.md`, `punchlist.md`, and `changelog.md` synchronized | REVIEW | Automated planning-document consistency checks pass. |
| Select a license and document third-party data and firmware rights | BLOCKED | Legal and owner decision required. |

## P2 — Evidence and validation

| Item | Status | Completion evidence |
|---|---|---|
| Create an exact file-level prototype inventory | OPEN | Manifest binds paths, roles, hashes, and evidence classes. |
| Define representative supported and unsupported platform matrices | BLOCKED | Ownership and laboratory scope required. |
| Establish trusted firmware-baseline provenance | BLOCKED | Approved sources, custody, signatures, and update policy required. |
| Add malformed-input, parser, extension, and hostile-report fixtures | OPEN | Synthetic-only fixtures and regressions pass. |
| Characterize false positives, false negatives, and uncertainty | BLOCKED | Representative evidence and independent review required. |
| Retain deterministic documentation and test evidence | REVIEW | Pull-request workflow uploads exact-head reports and input hashes. |

## P3 — Security, privacy, and rollback

| Item | Status | Completion evidence |
|---|---|---|
| Document credential, privilege, management-plane, packet-capture, and firmware boundaries | REVIEW | Threat model and onboarding agree. |
| Separate passive collection from disruptive response | REVIEW | Architecture and extension documentation preserve the boundary. |
| Define correction and withdrawal propagation for published claims | OPEN | Every controlled route has an owner or explicit vacancy. |
| Define repository migration rollback | BLOCKED | Destination repository and owner required. |
| Define retirement and archival procedure | OPEN | Archive preserves source identity, evidence, limitations, and supersession route. |
| Conduct a history-aware secrets and sensitive-data review | BLOCKED | Authorized reviewer and remediation plan required. |

## P4 — Release and publication

| Item | Status | Completion evidence |
|---|---|---|
| Approve a permanent product and package identity | BLOCKED | Ownership decision required. |
| Reproduce clean installation, tests, documentation, SBOM, and checksums | BLOCKED | Dedicated candidate and retained artifacts required. |
| Approve Pages publication | BLOCKED | Documentation candidate, privacy/security/license/accessibility review, and explicit approval required. |
| Approve package, image, service, dashboard, or integration release | BLOCKED | All release gates in `release.md` pass. |
| Verify rollback after any authorized publication or release | BLOCKED | Independent resulting-state evidence required. |

## Decision packet still required

The Architect decision must name the chosen disposition, destination or archival location, scope, owner or vacancy, license path, history-preservation method, compatibility and redirect policy, security/privacy reviewers, evidence custodian, publication authority, rollback owner, and conditions for reopening the decision.

## FYSA-120 mapping

Applied planning categories: `CAT-012`, `CAT-013`, `CAT-017`, `CAT-019`, `CAT-031`, `CAT-040`, `CAT-052`, and `CAT-054`.

Proposed non-authoritative subdivision: **`040-H — incubation-to-ownership documentation, retirement evidence, and reversible repository handoff`**.
