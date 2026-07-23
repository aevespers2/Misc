# Task Chain

Architect owns intake, scope, promotion, migration, and retirement decisions. Builders preserve evidence and may continue bounded documentation, validation, or maintenance only after the proposal is classified and without expanding capability, publication, release, or operational authority.

States: `PROPOSED` · `READY` · `IN PROGRESS` · `BLOCKED` · `REVIEW` · `DONE`

## Product directive

- **Next objective:** Complete decision readiness for the XYZ defensive firmware-assessment prototype, then obtain an Architect decision to migrate it into a dedicated owning repository, retire/archive it, or continue a documented hold before additional capability, packaging, publication, or deployment work proceeds.
- **User outcome:** A defensive researcher can understand one clearly labeled prototype, reproduce documentation and local checks, and distinguish implementation, configured automation, historical validation, proposals, missing evidence, and blocked authority.
- **MVP scope:** preserve the current prototype and history; maintain an accessible front door, architecture, onboarding, developer guide, threat model, evidence classification, punch list, release gates, and changelog; inventory implemented collectors, firmware/hash checks, kernel and management-channel heuristics, PCAP analysis, dashboard/API, extension interface, dry-run isolation abstraction, image/packaging scripts, tests, CI, documentation, and compliance mappings; compare ownership with existing portfolio repositories; select a dedicated destination or retirement path; choose a license; document data, firmware, credential, network, privilege, hardware, evidence, false-positive, publication, correction, migration, retirement, and rollback boundaries; establish representative validation and adversarial fixtures; and prohibit release or deployment until evidence and approvals are complete.
- **Priority:** Portfolio priority remains `P4 — HOLDING / INCUBATION`; this does not supersede active P0 work elsewhere. Local P0 exists because implementation and a Pages-capable workflow arrived before the approved incubation contract, creating a scope conflict that must remain visible.
- **Success criteria:** the documentation routes agree; every capability claim is evidence-classified; the prototype has one approved owner and destination or a recorded retirement/hold decision; repository overlap is resolved; no license, data-rights, credential, firmware, hardware, networking, privacy, publication, or rollback ambiguity remains; representative and adversarial tests quantify supported platforms and limitations; reproducible exact-head evidence is retained; and no operational, certification, DoD/Army authorization, or detection-assurance claim exceeds the evidence.
- **Non-goals:** treating `Misc` as the permanent production repository; continuing feature expansion while ownership is unresolved; scanning systems without explicit authorization; exploiting management interfaces; flashing firmware; enabling disruptive isolation by default; storing customer data, credentials, firmware images, private packet captures, or sensitive findings; claiming comprehensive implant detection, CMMC status, STIG approval, Army authorization, or an ATO; or allowing documentation publication to imply product release.
- **Release rationale:** Preserving the prototype while freezing promotion protects useful research evidence without rewarding a bypass of the repository intake contract. A dedicated approved owner or a provenance-preserving retirement decision is required before a privileged defensive assessment tool can be packaged, publicly represented, deployed, or integrated.

## Scope-conflict finding

The repository's original documentation stated that implementation and deployment were prohibited until the incubation contract was accepted. Later commits added a Python package branded XYZ under `phantomblock/`, version `0.3.0`, source and tests, live-image and binary-build scripts, compliance mappings, CI, extensive documentation, and a GitHub Pages workflow. These artifacts are preserved as prototype implementation and configured automation; they are not accepted release, deployment, detection, certification, or authorization evidence.

## Active chain

| Priority | Task | Owner | Depends on | Status | Acceptance criteria |
|---|---|---|---|---|---|
| Local P0.0 | Preserve scope containment and manual-only publication gate | Architect + Builder | — | REVIEW | Existing implementation and history remain intact; automatic Pages publication is disabled; no capability, package, release, or deployment promotion occurs. |
| Local P0.1 | Maintain the incubation documentation front door | Builder | P0.0 | REVIEW | README, MkDocs routes, architecture, onboarding, developer guide, punch list, task chain, release plan, and changelog agree and pass exact-head validation. |
| Local P0.2 | Complete file-level evidence and overlap inventory | Builder + Architect | P0.0-P0.1 | IN PROGRESS | Every relevant path is classified; provenance, ownership claims, conflicts, and missing evidence are recorded without selecting authority. |
| Local P1 | Approve dedicated ownership, retirement, or continued hold | Architect | P0.0-P0.2 | BLOCKED | One disposition, destination or archive, owner or vacancy, intended user, overlap resolution, license path, migration/retirement plan, and rollback owner are approved. |
| Local P2 | Establish a bounded validation candidate | Builder | Local P1 and explicit approval | BLOCKED | The approved destination contains reproducible dependencies, threat model, representative hardware matrix, trusted-baseline provenance, passive/dry-run defaults, adversarial fixtures, false-positive/false-negative characterization, SBOM/checksums, CI evidence, and rollback procedures. |
| Local P3 | Approve publication or release | Architect | Local P2 | BLOCKED | One immutable candidate is independently reviewed; documentation claims match evidence; Pages/package/image publication is explicitly approved; security, legal, licensing, provenance, accessibility, and operational gates pass. |
| Portfolio P4 | Resume general incubation intake | Architect | Local P0 | BLOCKED | The intake and exit contract is approved and future proposals cannot add implementation before classification. |

## Builder rules

Do not expand XYZ or add another experiment until Local P0 and Local P1 are resolved. Preserve existing code and evidence. Stop on unclear ownership, unlicensed dependencies or content, untrusted firmware baselines, credential requirements, privileged mutation, unsupported hardware claims, public disclosure risk, automatic publication without approval, undefined validation, inconsistent documentation, or missing rollback.

## Builder log

Record approvals, proposal IDs, source commits, commands/results, workflow and status-check URLs, environment and dependency versions, hardware and firmware sources, data/license classification, artifact hashes, limitations, ownership destination, publication decision, migration/retirement decision, and rollback evidence.

- 2026-07-16 — Initialized `Misc` as a documentation-first incubation repository at portfolio priority P4.
- 2026-07-16 — Detected a scope conflict after later commits added the XYZ/PhantomBlock prototype, packaging and image scripts, compliance and documentation assets, CI, and Pages deployment capability before the intake contract or experiment classification was approved.
- 2026-07-16 — Preserved the implementation as unaccepted prototype evidence, froze product promotion, and made dedicated-repository ownership or retirement the next approval decision.
- 2026-07-23 — Added a repository front door, incubation-status guide, accessible architecture, safe onboarding, developer guide, and punch list; documentation improvement does not alter the blocked release or deployment posture.

## FYSA-120 planning map

Applied categories: `CAT-012`, `CAT-013`, `CAT-017`, `CAT-019`, `CAT-031`, `CAT-040`, `CAT-052`, and `CAT-054`. Proposed subdivision `040-H` remains non-authoritative and covers incubation-to-ownership documentation, retirement evidence, and reversible repository handoff.
