# Task Chain

Architect owns intake, scope, promotion, and retirement decisions. Builders may preserve evidence and create bounded experiments only after a proposal is classified and assigned an explicit owner.

States: `PROPOSED` · `READY` · `IN PROGRESS` · `BLOCKED` · `REVIEW` · `DONE`

## Product directive

- **Next objective:** Define and approve a lightweight incubation contract for experimental security, verification, and systems work before this repository accumulates implementation.
- **User outcome:** A researcher can place an early proposal or isolated proof of concept in one clearly labeled location, understand that it is non-authoritative, and know the evidence required to promote it into a dedicated repository or retire it.
- **MVP scope:** documentation-only intake template; proposal metadata; owner and intended user; problem statement; relationship to existing repositories; evidence classification; data, privacy, license, credential, and network boundaries; resource and stop limits; experiment directory convention; promotion, migration, archival, and deletion criteria; rollback/provenance rules.
- **Priority:** Portfolio priority is `P4 — HOLDING / INCUBATION`. This repository does not supersede QSO-GENOMES acceptance, QuantumStateObjects reproducibility, or any existing repository's active P0. Its immediate local priority is preventing scope dumping and duplicate ownership.
- **Success criteria:** every future experiment has a unique identifier, named owner, non-overlapping purpose, explicit dependencies, bounded inputs/outputs, tests or falsification criteria, evidence state, license/data classification, stop condition, and documented destination or retirement rule; no artifact is presented as an accepted product capability from this repository alone.
- **Non-goals:** becoming a catch-all production monorepo; duplicating QSO, Bridge, VTX, Alistaire, AionUi, or temporal-invariant ownership; storing credentials or sensitive datasets; autonomous networking or deployment; publishing unreviewed packages; or using incubation status to bypass repository-specific product and security gates.
- **Release rationale:** A documentation-only incubation boundary preserves useful exploratory work while preventing ambiguous ownership, misleading capability claims, and permanent accumulation of unsupported experiments.

## Active chain

| Priority | Task | Owner | Depends on | Status | Acceptance criteria |
|---|---|---|---|---|---|
| P0 | Approve the incubation intake and exit contract | Architect | — | READY | Intake fields, evidence states, trust/data/license boundaries, repository-conflict check, promotion criteria, archive/retirement criteria, and rollback/provenance rules are documented. |
| P1 | Inventory and classify the first proposed experiment | Architect | P0 | PROPOSED | The proposal has a unique scope, named user outcome, existing-repository comparison, risk limits, validation plan, and disposition. |
| P2 | Run one bounded proof of concept | Builder | P1 and explicit approval | PROPOSED | Work is isolated, deterministic where practical, credential-free, reversible, and produces retained evidence without claiming production capability. |
| P3 | Promote, migrate, or retire the experiment | Architect | P2 | PROPOSED | Evidence and history move to an approved owning repository, or the experiment is archived with the reason and limitations preserved. |

## Builder rules

Do not add implementation until P0 and the specific experiment's P1 classification are approved. Stop on duplicate repository ownership, unclear data rights, credential requirements, remote mutation, undefined validation, or missing rollback.

## Builder log

Record approvals, proposal IDs, source commits, commands/results, environment and dependency versions, data/license classification, artifact hashes, limitations, destination/retirement decisions, and rollback evidence.
