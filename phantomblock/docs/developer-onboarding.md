# Developer Onboarding

## Read this first

XYZ is preserved in `Misc` as an implemented but unaccepted prototype. Local development must remain passive, evidence-oriented, and bounded by the repository's blocked release posture.

Before changing code or documentation, read:

1. root [`taskchain.md`](../../taskchain.md);
2. root [`release.md`](../../release.md);
3. root [`changelog.md`](../../changelog.md);
4. [Repository boundaries](repository-boundaries.md);
5. [Threat model](threat-model.md);
6. [Design contracts](design-contracts.md).

## Supported review environment

The package metadata currently requires Python 3.11 or later. The repository configures development dependencies for Pytest and Ruff, and documentation dependencies for MkDocs Material.

A local setup suitable for source review is:

```bash
cd phantomblock
python3.11 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[dev,docs]'
```

On Windows PowerShell, activate with:

```powershell
.venv\Scripts\Activate.ps1
```

Do not install the prototype globally or into an environment that contains production credentials or sensitive incident data.

## Verify the baseline

Run the bounded quality checks from `phantomblock/`:

```bash
ruff check .
pytest
mkdocs build --strict
```

Record the exact commit, Python version, dependency resolution, operating system, commands, and results. A passing local run is useful development evidence but does not satisfy release validation.

## Repository map

```text
Misc/
├── README.md                  Repository status and entry point
├── taskchain.md               Authoritative work sequence and ownership hold
├── release.md                 Release gates and evidence posture
├── changelog.md               Product and documentation history
├── punchlist.md               Documentation and repository-health checklist
├── CONTRIBUTING.md            Contribution rules
├── .github/workflows/         CI and fail-closed manual Pages workflow
└── phantomblock/
    ├── pyproject.toml          Prototype package and tool configuration
    ├── mkdocs.yml              Pages navigation and documentation build
    ├── docs/                   Project, architecture, security, and review guides
    ├── src/phantomblock/       Prototype implementation
    ├── tests/                  Unit-test source
    └── ...                    Build/image and example configuration artifacts
```

The ellipsis indicates retained prototype artifacts not exhaustively documented here. Inspect source and commit history rather than assuming this map is complete.

## Safe development modes

### Documentation and evidence review

Appropriate tasks include:

- clarifying status, limitations, interfaces, and trust boundaries;
- fixing broken documentation links or build errors;
- recording exact reproduction steps and results;
- improving synthetic fixtures;
- separating implemented behavior from proposals;
- identifying unsupported platforms or unsafe assumptions;
- creating migration or retirement records.

### Source correction

A source correction may be appropriate when it is narrowly bounded and does not expand capability, such as:

- fixing a deterministic defect exposed by an existing synthetic test;
- making an error state explicit rather than silently ignored;
- reducing privilege or network exposure;
- preserving data without changing interpretation;
- correcting documentation-code mismatch.

Record why the change is evidence-preserving rather than scope-expanding.

### Work that requires prior approval

Do not proceed without an approved owning repository and explicit authorization for:

- new collectors, detectors, heuristics, or supported platforms;
- real device or fleet testing;
- privileged execution or credential handling;
- active management-plane access;
- production switch adapters or remediation;
- remote dashboard exposure or multi-user access;
- packaging, images, release artifacts, signatures, or public deployment;
- third-party extension execution;
- customer, incident, firmware, or PCAP data ingestion;
- certification, compliance, or operational claims.

## CLI review

The current CLI source defines four command families:

```bash
xyz collect
xyz inspect-pcap
xyz dashboard
xyz isolate
```

These commands are prototype interfaces, not a supported public API. Use synthetic inputs and unprivileged environments. The `isolate` path is expected to remain dry-run only.

Use help output to inspect arguments without performing collection:

```bash
xyz --help
xyz collect --help
xyz inspect-pcap --help
xyz dashboard --help
xyz isolate --help
```

## Documentation workflow

Preview documentation locally:

```bash
mkdocs serve
```

Build with strict checking before committing:

```bash
mkdocs build --strict
```

The GitHub Pages workflow is intentionally manual-only and guarded by the root release status. Documentation quality checks do not authorize deployment.

## Branch and pull-request discipline

Use a focused branch and keep each pull request bounded. The description should include:

- purpose and scope;
- files and contracts affected;
- implementation/proposal/evidence classification;
- commands and results;
- security or privacy effects;
- compatibility and migration effects;
- known limitations;
- confirmation that release status was not advanced;
- rollback method.

Do not mix documentation clarification with feature development.

## Handling findings and sensitive data

Do not commit:

- real firmware dumps or proprietary vendor images;
- credentials, tokens, keys, or management-plane secrets;
- customer or third-party PCAPs;
- device serial numbers or unique identifiers from real systems;
- unredacted incident reports;
- exploit details that create unnecessary operational risk;
- conclusions attributing activity to a person, organization, or nation without independently reviewable evidence.

Use synthetic, minimized, and clearly labeled fixtures.

## When to stop

Stop and escalate for architectural review when:

- the correct owning repository is unclear;
- a task would add capability rather than clarify existing behavior;
- authorization to inspect a system is not explicit;
- a baseline or dependency lacks provenance or licensing clarity;
- credentials, privilege, networking, firmware access, or target mutation are required;
- documentation could imply certification, deployment, or release;
- rollback is undefined;
- test evidence cannot be retained and tied to an immutable commit.

The repository's present success condition is accurate containment and review, not feature velocity.