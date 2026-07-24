# Misc

`Misc` is a **non-authoritative incubation and evidence-preservation repository** for experimental security, verification, and systems work that has not yet been assigned a permanent owning repository.

The repository currently contains the **XYZ / PhantomBlock defensive firmware-assessment prototype** under `phantomblock/`. That prototype is preserved for review, but it is not an approved product, release candidate, certification, operational detector, or authorization to assess any system.

## Current status

- Portfolio priority: **P4 — holding / incubation**.
- Release status: **blocked** pending ownership, licensing, validation, security, publication, provenance, and approval decisions.
- GitHub Pages publication: manual-only and fail-closed unless `release.md` is explicitly marked `READY`.
- Implementation scope: frozen except for evidence-preserving corrections or work explicitly approved after architectural review.
- Incubation exit status: `INCUBATION_EXIT_DOCUMENTED_DISPOSITION_UNAPPROVED`.

See [`taskchain.md`](taskchain.md), [`release.md`](release.md), [`punchlist.md`](punchlist.md), and [`changelog.md`](changelog.md) for the authoritative planning and release posture.

## Repository purpose

`Misc` exists to make experimental work reviewable without allowing an experiment to acquire production authority by accumulation. Each proposal must be classified, bounded, assigned an owner, and either:

1. promoted into a dedicated repository with an approved charter;
2. consolidated as an approved module under a named owner;
3. retained temporarily as bounded evidence; or
4. retired or archived with provenance and limitations preserved.

`Misc` is not intended to become the permanent home of production packages, deployment workflows, credentials, customer data, firmware images, sensitive findings, or privileged operational tooling.

## Current prototype: XYZ / PhantomBlock

The `phantomblock/` subtree contains an implemented Python prototype with:

- a command-line interface;
- hardware, firmware, kernel, and management-plane evidence collection;
- offline PCAP inspection;
- a read-only reporting API and dashboard;
- passive extension registration;
- a dry-run switch-isolation adapter seam;
- tests and CI configuration;
- live-image and standalone-build definitions;
- MkDocs documentation and compliance-oriented planning material.

These artifacts demonstrate a prototype shape only. They do **not** establish representative hardware support, detection accuracy, trusted firmware provenance, production isolation safety, certification, an Authority to Operate, or operational readiness.

## Proposed A.L.I.S.T.A.I.R.E. relationship

The lowest-overlap integration candidate is to treat PhantomBlock as a **specialist host-firmware, kernel, management-plane, and offline-PCAP observation adapter** beneath Repository `0`'s portable first-install security workflow.

Under that proposal:

- PhantomBlock collects and classifies bounded evidence;
- Repository `0` composes host observations, prepares proposals, and performs only separately authorized remediation;
- Repository `1` owns candidate device identity, baseline identity, proposal admission, capabilities, revocations, canonical receipts, and recovery checkpoints;
- Bridge may transport approved envelopes without creating trust;
- QSO-STUDIO or AionUi may display reviewed results without gaining approval or mutation authority;
- `Misc` retains no permanent operational authority.

JusticeForMe and PhantomBlock currently overlap as Linux host-observation prototypes. The documentation proposes a low-coupling split in which JusticeForMe owns general operating-system, account, package, service, persistence, and network-configuration audit surfaces, while PhantomBlock owns specialist hardware, firmware, kernel-integrity, management-plane, and explicitly supplied offline-PCAP evidence. Shared fields require one canonical observation envelope, deduplication rule, conflict model, privacy policy, and Repository `0` / Repository `1` gluing contract.

This is a documentation recommendation only. It does not approve migration, privileged collection, credentials, network access, active response, publication, release, or deployment.

## Documentation

The Pages-ready documentation is stored in [`phantomblock/docs/`](phantomblock/docs/) and is built with [`phantomblock/mkdocs.yml`](phantomblock/mkdocs.yml).

Key guides:

- [Project status and scope](phantomblock/docs/index.md)
- [Repository boundaries](phantomblock/docs/repository-boundaries.md)
- [Portable host-observation role](phantomblock/docs/portable-host-observation.md)
- [JusticeForMe and PhantomBlock overlap](phantomblock/docs/host-observation-overlap.md)
- [Obstruction and gluing analysis](phantomblock/docs/obstruction-and-gluing.md)
- [Incubation exit and migration playbook](phantomblock/docs/incubation-exit-and-migration.md)
- [Architecture](phantomblock/docs/architecture.md)
- [Design contracts](phantomblock/docs/design-contracts.md)
- [Developer onboarding](phantomblock/docs/developer-onboarding.md)
- [Ownership and release decision](phantomblock/docs/ownership-and-release.md)
- [Threat model](phantomblock/docs/threat-model.md)
- [Validation roadmap](phantomblock/docs/validation.md)

## Safe local review

Local review should remain passive and use synthetic or explicitly authorized inputs.

```bash
cd phantomblock
python -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[dev,docs]'
ruff check .
pytest
mkdocs build --strict
```

Do not run privileged collection, inspect third-party systems, load untrusted extensions, use real credentials, publish findings, or connect a non-dry-run isolation adapter without explicit authorization and an approved owning repository.

## Contribution boundary

Before contributing, read [`CONTRIBUTING.md`](CONTRIBUTING.md). Documentation, evidence classification, reproducibility improvements, and clearly bounded corrective work are appropriate. Feature expansion, packaging promotion, automatic publication, privileged integrations, or release claims are not appropriate while ownership remains unresolved.

## Architectural decision required

The next substantive decision is to either:

- migrate XYZ and its history into a dedicated, approved security-adapter repository with a charter, owner, license, authorized-use policy, device and evidence contracts, validation plan, and release controls;
- consolidate the approved observation subset with JusticeForMe under one shared contract and preserved histories;
- retire/archive the prototype while preserving source history, evidence, limitations, and the reason for disposition; or
- explicitly retain it frozen in incubation while recording the unresolved blockers.

The [incubation exit and migration playbook](phantomblock/docs/incubation-exit-and-migration.md) defines the component ledger, source-to-target manifest, history preservation, gluing review, rollback, and independent evidence required for any of those outcomes. It does not select or authorize one.

If migration or consolidation is selected, the Architect must also approve the Repository `0` and Repository `1` gluing contracts for device identity, baseline identity, evidence envelopes, canonical fields, deduplication, conflict resolution, capabilities, receipts, revocations, temporal semantics, privacy, incident handling, and rollback.

Until those decisions are recorded, `Misc` remains an incubation repository and the prototype remains unreleased.
