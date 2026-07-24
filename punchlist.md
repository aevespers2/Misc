# Punch List

This list governs bounded documentation, evidence, ownership, migration, consolidation, retirement, and rollback work for `Misc` and the preserved XYZ / PhantomBlock prototype. Completion of an item does not authorize release, deployment, assessment of third-party systems, certification, or operational integration.

States: `OPEN` · `IN PROGRESS` · `BLOCKED` · `REVIEW` · `DONE` · `NOT APPLICABLE`

## P0 — Containment and decision readiness

| Item | Status | Completion evidence |
|---|---|---|
| Publish a clear repository front door and status notice | DONE | `README.md` and `phantomblock/docs/incubation-status.md` agree on the holding posture. |
| Classify implementation, documentation, workflow, package, image, and compliance component families | REVIEW | `component-overlap-inventory.md` records C01-C18 and the exact source manifest binds all tracked paths to those families; reviewer confirmation remains required. |
| Inventory cross-repository overlaps and gluing failures | REVIEW | O01-O10, safe defaults, required witnesses, and ten material obstruction classes are documented without selecting authority. |
| Prevent automatic Pages publication | DONE | `.github/workflows/pages.yml` is manual-only and blocks unless `release.md` is explicitly `READY`. |
| Preserve the prototype and history without capability expansion | REVIEW | Current source is retained; future changes require scope checks and explicit manifest rebinding. |
| Record intended users, authorized-use boundary, non-goals, and evidence limits | DONE | README, onboarding, threat model, file manifest, and release plan contain the boundary. |
| Document dedicated migration, modular consolidation, evidence-preserving retirement, and continued hold | REVIEW | `phantomblock/docs/incubation-exit-and-migration.md` defines controlled dispositions without selecting one. |
| Decide dedicated migration, modular consolidation, retirement, or continued hold | BLOCKED | Explicit Architect disposition required. |

## P1 — Documentation and information architecture

| Item | Status | Completion evidence |
|---|---|---|
| Maintain a stable documentation front door | REVIEW | MkDocs navigation and internal-link validation cover the component and file manifests and pass at the exact candidate head. |
| Document architecture and trust boundaries with an equivalent prose alternative | REVIEW | `phantomblock/docs/architecture.md` passes documentation validation. |
| Provide a component and overlap inventory with accessible graph and prose | REVIEW | Markdown and JSON inventories agree on status, components, overlaps, obstructions, and next artifact. |
| Provide an exact file disposition manifest with accessible flow and prose | REVIEW | Markdown and JSON bind all 42 tracked paths at `68703e138ffa1df26924dd4e018078a246531ace` to Git blob identity, component/evidence/sensitivity classes, limitations, common fail-closed disposition, owner vacancies, correction, rollback, and successor rebinding. |
| Provide safe onboarding before operational commands | REVIEW | `phantomblock/docs/onboarding.md` foregrounds authorization, privacy, and non-deployment boundaries. |
| Provide a developer guide for repository layout, tests, evidence, and change control | REVIEW | `phantomblock/docs/developer-guide.md` is linked from README and MkDocs. |
| Provide an exit playbook with an equivalent prose decision path | REVIEW | Exit guide includes accessible flow, source freeze, component ledger, manifest, contract review, rollback, restoration, and onboarding. |
| Keep `taskchain.md`, `release.md`, `punchlist.md`, and `changelog.md` synchronized | REVIEW | Automated planning-document consistency checks include the frozen-source status and pass. |
| Select a license and document third-party data and firmware rights | BLOCKED | Legal and owner decision required. |

## P2 — Evidence and validation

| Item | Status | Completion evidence |
|---|---|---|
| Create an exact file-level prototype inventory | REVIEW | The 42-path Markdown/JSON manifest is complete for frozen source `68703e1…`; independent tree/blob verification and successor rebinding remain required. |
| Assign every component and authority surface a disposition | REVIEW | Every manifest entry inherits `REMAIN_IN_INCUBATION_PENDING_ARCHITECT`; Architect selection of a final controlled disposition remains blocked. |
| Preserve source-to-target history | BLOCKED | Approved destination or archive and independently reviewable commit map required. |
| Define representative supported and unsupported platform matrices | BLOCKED | Ownership and laboratory scope required. |
| Establish trusted firmware-baseline provenance | BLOCKED | Approved sources, custody, signatures, and update policy required. |
| Add malformed-input, parser, extension, and hostile-report fixtures | OPEN | Synthetic-only fixtures and regressions pass. |
| Add duplicate, conflict, stale, replay, wrong-device, correction, revocation, withdrawal, and rollback fixtures | OPEN | Cross-repository and triple-overlap cases fail closed. |
| Characterize false positives, false negatives, and uncertainty | BLOCKED | Representative evidence and independent review required. |
| Retain deterministic documentation and test evidence | REVIEW | Pull-request workflow uploads exact-head reports and input hashes. |

## P3 — Security, privacy, and rollback

| Item | Status | Completion evidence |
|---|---|---|
| Document credential, privilege, management-plane, packet-capture, and firmware boundaries | REVIEW | Threat model, onboarding, component inventory, and file classifications agree. |
| Separate passive collection from disruptive response | REVIEW | Architecture and C12 preserve the boundary. |
| Define correction and withdrawal propagation for published claims | OPEN | The manifest defines a source correction route, but every controlled consumer still needs an owner or explicit vacancy and acknowledgment evidence. |
| Define repository migration and consolidation rollback | BLOCKED | Destination repository and owner required. |
| Define retirement and archival procedure | REVIEW | Exit playbook preserves source identity, evidence, limitations, deprecation, and restoration criteria. |
| Verify restored-state evidence | BLOCKED | Prior state is independently reconstructable and exact-head checks pass after restoration. |
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

The Architect decision must name the chosen disposition, destination or archival location, scope, owner or vacancy, license path, history-preservation method, compatibility and redirect policy, security/privacy reviewers, evidence custodian, publication authority, correction and revocation owners, rollback owner, restoration witness, and conditions for reopening the decision. The exact source manifest informs this decision but cannot make it.

## FYSA-120 mapping

Applied planning categories: `CAT-011`, `CAT-012`, `CAT-013`, `CAT-017`, `CAT-018`, `CAT-019`, `CAT-031`, `CAT-032`, `CAT-040`, `CAT-052`, and `CAT-054`.

Proposed non-authoritative refinements:

- **`040-P — Incubation exit, authority-neutral migration, modular consolidation, and evidence-preserving retirement`**.
- **`013-M — Incubated component-family inventories, cross-repository overlap ledgers, and disposition-safe ownership graphs`**.
- **`017-F — Exact-generation file disposition manifests, blob-bound provenance, and successor rebinding`**.
