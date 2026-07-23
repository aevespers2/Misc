# Safe Onboarding

This guide is for documentation review, local development, and bounded laboratory evaluation. It is not authorization to assess systems you do not own or lack explicit permission to test.

## Before you begin

Confirm all of the following:

- the system, firmware, packet capture, and management interface are owned by you or covered by written authorization;
- no production credentials, customer data, proprietary firmware, or sensitive findings will enter the public repository, CI logs, issues, or artifacts;
- disruptive actions are disabled;
- the work is documentation, reproducibility, synthetic-fixture, or approved laboratory work;
- results will be treated as observations requiring corroboration, not forensic conclusions or certification evidence.

## Repository layout

| Path | Purpose | Authority boundary |
|---|---|---|
| `README.md` | Portfolio and repository front door | Describes status; grants no product authority |
| `taskchain.md` | Current work ordering | Planning only |
| `release.md` | Release and publication gates | Current status is blocked |
| `punchlist.md` | Bounded work and blockers | Completion does not imply release |
| `phantomblock/src/` | Prototype implementation | Preserved research code |
| `phantomblock/tests/` | Existing tests | Local behavior evidence only |
| `phantomblock/docs/` | Product and governance documentation | Intended behavior and limitations |
| `.github/workflows/` | CI and manual publication configuration | Workflow presence is not approval |

## Documentation-only setup

From the repository root:

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e 'phantomblock[docs]'
cd phantomblock
mkdocs build --strict
```

Windows PowerShell activation uses `.venv\Scripts\Activate.ps1`.

The strict build verifies that the documentation can be rendered. It does not publish Pages and does not validate detection claims.

## Development setup

For local source and test work:

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e 'phantomblock[dev,docs]'
cd phantomblock
ruff check .
pytest
mkdocs build --strict
```

Record the Python version, dependency resolution, exact commit, commands, results, and limitations. Do not interpret a clean lint or unit-test run as hardware validation, security approval, or release readiness.

## Safe first contribution

The safest first contribution is one of:

- correct a documentation contradiction;
- add an accessible prose alternative to a diagram;
- add a synthetic malformed-input fixture;
- improve deterministic validation without network or privileged access;
- inventory files, dependencies, evidence classes, or ownership gaps;
- document a rollback or retirement step.

## Prohibited onboarding shortcuts

Do not:

- run against third-party systems without written authorization;
- use real production credentials or private management interfaces;
- upload firmware images or packet captures with sensitive content;
- enable a switch, BMC, AMT, IPMI, Redfish, or isolation adapter against production infrastructure;
- publish Pages, packages, images, releases, or findings;
- describe a mismatch or heuristic as proof of compromise;
- represent compliance mappings as certification or an Authority to Operate.

## Reporting a finding

A useful report includes:

1. exact repository commit;
2. environment and dependency versions;
3. synthetic or authorized source classification;
4. command and expected behavior;
5. observed behavior and raw error;
6. security, privacy, and publication considerations;
7. whether the issue affects documentation, local behavior, evidence integrity, or authority boundaries;
8. a reversible proposed repair.

Keep sensitive details out of public issues. Record an explicit vacancy when no approved private reporting route exists.
