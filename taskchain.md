# Task Chain

Architect owns intake, scope, promotion, and retirement decisions. Builders preserve evidence and may continue bounded implementation only after the proposal is classified, assigned an explicit owner, and approved against repository, security, publication, and release boundaries.

States: `PROPOSED` · `READY` · `IN PROGRESS` · `BLOCKED` · `REVIEW` · `DONE`

## Product directive

- **Next objective:** Contain and classify the newly added XYZ defensive firmware-assessment prototype, then obtain an Architect decision to migrate it into a dedicated owning repository or retire/archive it before additional capability, packaging, publication, or deployment work proceeds.
- **User outcome:** A defensive researcher can evaluate one clearly labeled prototype without mistaking repository code, documentation, package metadata, compliance mappings, or deployment workflows for independently validated detection capability, certification, operational readiness, or authorization to assess systems.
- **MVP scope:** preserve the current prototype and commit history; inventory implemented collectors, firmware/hash checks, kernel and management-channel heuristics, PCAP analysis, dashboard/API, extension interface, dry-run isolation abstraction, image/packaging scripts, tests, CI, documentation, and compliance mappings; define the intended user and authorized-use boundary; compare ownership with existing security, Bridge, AionUi, verification, and QSO repositories; select a dedicated destination or retirement path; choose a license; document data, firmware, credential, network, privilege, hardware, evidence, false-positive, publication, and rollback boundaries; establish representative validation and adversarial fixtures; and prohibit release or deployment until evidence and approvals are complete.
- **Priority:** Portfolio priority remains `P4 — HOLDING / INCUBATION`; this does not supersede QSO-GENOMES acceptance or any existing repository P0. A local containment task is `P0` only because implementation and an automatic Pages publication workflow were added before the approved incubation contract, creating a documented scope conflict.
- **Success criteria:** the prototype has one approved owner and destination or a recorded retirement decision; every claimed capability is classified as implemented code, configured workflow, locally tested behavior, unverified proposal, or accepted evidence; repository overlap is resolved; no license, data-rights, credential, firmware, hardware, networking, or publication ambiguity remains; the Pages and release posture is explicitly approved or disabled; representative and adversarial tests quantify supported platforms and limitations; reproducible status-check evidence is retained; and no operational, certification, DoD/Army authorization, or detection-assurance claim exceeds the evidence.
- **Non-goals:** treating `Misc` as the permanent production repository; continuing feature expansion while ownership is unresolved; scanning systems without explicit authorization; exploiting management interfaces; flashing firmware; enabling disruptive isolation by default; storing customer data, credentials, firmware images, or sensitive findings; claiming comprehensive implant detection, CMMC status, STIG approval, Army authorization, or an ATO; or allowing documentation publication to imply product release.
- **Release rationale:** Preserving the prototype while freezing promotion protects useful research evidence without rewarding a bypass of the repository intake contract. A dedicated, approved owner is required before a privileged defensive assessment tool can be packaged, publicly represented, deployed, or integrated.

## Scope-conflict finding

The repository's approved documentation stated that implementation and deployment were prohibited until the incubation contract was accepted. Fifteen subsequent commits added a Python package branded XYZ under `phantomblock/`, version `0.3.0`, source and tests, live-image and binary-build scripts, compliance mappings, CI, extensive documentation, and a GitHub Pages workflow with `pages: write` and `id-token: write`. These artifacts are preserved as prototype implementation and configured automation; they are not accepted release, deployment, detection, certification, or authorization evidence.

## Active chain

| Priority | Task | Owner | Depends on | Status | Acceptance criteria |
|---|---|---|---|---|---|
| Local P0 | Freeze promotion and reconcile the XYZ prototype with the incubation boundary | Architect | — | REVIEW | Current files and commits are preserved; no additional feature, package, release, or deployment claim proceeds; automatic publication and workflow authority are reviewed; implemented behavior is separated from documentation claims and missing evidence. |
| Local P1 | Approve dedicated ownership or retirement | Architect | Local P0 | BLOCKED | One destination repository, owner, intended user, overlap disposition, license path, authorized-use policy, and migration/retirement plan are approved. |
| Local P2 | Establish a bounded validation candidate | Builder | Local P1 and explicit approval | BLOCKED | The approved destination contains reproducible dependencies, threat model, representative hardware matrix, trusted-baseline provenance, passive/dry-run defaults, adversarial fixtures, false-positive/false-negative characterization, SBOM/checksums, CI evidence, and rollback procedures. |
| Local P3 | Approve publication or release | Architect | Local P2 | BLOCKED | One immutable candidate is independently reviewed; documentation claims match evidence; Pages/package/image publication is explicitly approved; security, legal, licensing, provenance, and operational gates pass. |
| Portfolio P4 | Resume general incubation intake | Architect | Local P0 | BLOCKED | The intake and exit contract is approved and future proposals cannot add implementation before classification. |

## Builder rules

Do not expand XYZ or add another experiment until Local P0 and Local P1 are resolved. Preserve all existing code and evidence. Stop on unclear ownership, unlicensed dependencies or content, untrusted firmware baselines, credential requirements, privileged mutation, unsupported hardware claims, public disclosure risk, automatic publication without approval, undefined validation, or missing rollback.

## Builder log

Record approvals, proposal IDs, source commits, commands/results, workflow and status-check URLs, environment and dependency versions, hardware and firmware sources, data/license classification, artifact hashes, limitations, ownership destination, publication decision, migration/retirement decision, and rollback evidence.

- 2026-07-16 — Initialized `Misc` as a documentation-first incubation repository at portfolio priority P4.
- 2026-07-16 — Detected a scope conflict after fifteen commits added the XYZ/PhantomBlock prototype, packaging and image scripts, compliance and documentation assets, CI, and automatic GitHub Pages deployment before the intake contract or experiment classification was approved.
- 2026-07-16 — Preserved the implementation as unaccepted prototype evidence, froze product promotion, and made dedicated-repository ownership or retirement the next approval decision without changing the portfolio priority of active repositories.
