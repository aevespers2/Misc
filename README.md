# Misc

`Misc` is a **non-authoritative incubation and evidence-preservation repository** for experimental security, verification, and systems work that has not yet been assigned a permanent owning repository.

The repository currently contains the **XYZ / PhantomBlock defensive firmware-assessment prototype** under `phantomblock/`. That prototype is preserved for review, but it is not an approved product, release candidate, certification, operational detector, or authorization to assess any system.

## Current status

- Portfolio priority: **P4 — holding / incubation**.
- Release status: **blocked** pending ownership, licensing, validation, security, publication, provenance, and approval decisions.
- GitHub Pages publication: manual-only and fail-closed unless `release.md` is explicitly marked `READY`.
- Implementation scope: frozen except for evidence-preserving corrections or work explicitly approved after architectural review.

See [`taskchain.md`](taskchain.md), [`release.md`](release.md), and [`changelog.md`](changelog.md) for the authoritative planning and release posture.

## Repository purpose

`Misc` exists to make experimental work reviewable without allowing an experiment to acquire production authority by accumulation. Each proposal must be classified, bounded, assigned an owner, and either:

1. promoted into a dedicated repository with an approved charter;
2. retained temporarily as bounded evidence; or
3. retired or archived with provenance and limitations preserved.

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

## Documentation

The Pages-ready documentation is stored in [`phantomblock/docs/`](phantomblock/docs/) and is built with [`phantomblock/mkdocs.yml`](phantomblock/mkdocs.yml).

Key guides:

- [Project status and scope](phantomblock/docs/index.md)
- [Repository boundaries](phantomblock/docs/repository-boundaries.md)
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

- migrate XYZ and its history into a dedicated, approved repository with a charter, owner, license, authorized-use policy, validation plan, and release controls; or
- retire/archive the prototype while preserving source history, evidence, limitations, and the reason for disposition.

Until that decision is recorded, `Misc` remains an incubation repository and the prototype remains unreleased.