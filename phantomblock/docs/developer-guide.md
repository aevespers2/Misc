# Developer Guide

XYZ / PhantomBlock is preserved prototype work inside an incubation repository. Development must improve clarity, reproducibility, evidence integrity, or safe decision readiness without silently expanding product or operational scope.

## Change classes

| Class | Examples | Default disposition |
|---|---|---|
| Documentation | Clarifications, diagrams, onboarding, API descriptions | Allowed when claims remain evidence-bound |
| Validation | Deterministic tests, malformed-input fixtures, link checks | Allowed when synthetic and non-privileged |
| Evidence governance | Manifests, hashes, provenance, correction records | Allowed when no private data is published |
| Maintenance | Dependency or workflow safety fixes | Review for scope and supply-chain effects |
| Capability expansion | New detectors, adapters, collectors, services | Blocked pending ownership approval |
| Privileged or disruptive behavior | Credentials, flashing, isolation, production writes | Blocked pending separate authorization |
| Publication or release | Pages, packages, images, tags, findings | Blocked pending `release.md` approval |

## Architecture rules

1. **Collection is not conclusion.** Preserve raw observations and separate policy from evidence gathering.
2. **Passive is not disruptive.** Passive extensions and response adapters remain separate interfaces.
3. **A digest is not trust.** Baselines require approved source, custody, signing, update, and revocation rules.
4. **A passing test is not validation.** Unit and documentation checks do not establish hardware coverage or accuracy.
5. **A configured workflow is not authority.** CI and Pages definitions do not approve release or deployment.
6. **Rollback is a state transition.** Reverting code is insufficient when reports, caches, packages, images, or public claims have propagated.

## Documentation expectations

Every behavior-facing page should identify:

- status: implemented, configured, locally tested, proposed, blocked, withdrawn, or historical;
- intended users and authorized-use limits;
- inputs, outputs, assumptions, and unsupported cases;
- trust boundaries and sensitive-data handling;
- failure modes and uncertainty;
- correction, supersession, retirement, and rollback path;
- evidence required before stronger claims are made.

Every meaningful diagram requires equivalent prose. Do not rely on color, position, or icons as the only carrier of meaning.

## API and report documentation

Before an interface is treated as stable, document:

- namespace and version;
- canonical serialization, if any;
- required and optional fields;
- producer and consumer identities;
- ordering, retry, duplicate, replay, and conflict behavior;
- correction, revocation, retention, migration, and retirement semantics;
- privacy classification and redaction rules;
- supported and unsupported generations;
- rollback and consumer-rebinding requirements.

Current schemas and entry points are prototype interfaces. Package version `0.3.0` does not establish compatibility or release stability.

## Tests and evidence

Run from `phantomblock/` after installing development dependencies:

```bash
ruff check .
pytest
mkdocs build --strict
```

For each candidate, retain or report:

- exact commit SHA;
- Python and dependency versions;
- commands and exit status;
- deterministic input hashes where practical;
- generated reports outside the source tree;
- clean-tree verification after tests;
- limitations and skipped environments;
- artifact identity and expiration when CI retains evidence.

## Pull-request checklist

- [ ] The change has one bounded purpose.
- [ ] Product and operational scope did not expand, or explicit approval is linked.
- [ ] Documentation and implementation do not contradict each other.
- [ ] New diagrams include prose alternatives.
- [ ] Tests are synthetic or use explicitly authorized sources.
- [ ] No credentials, private findings, proprietary firmware, or sensitive packet data are included.
- [ ] Workflows use least privilege and do not persist credentials unnecessarily.
- [ ] `taskchain.md`, `release.md`, `punchlist.md`, and `changelog.md` remain aligned.
- [ ] Rollback or withdrawal consequences are documented.
- [ ] Passing CI is not described as release, certification, or operational approval.

## Migration and retirement

A migration must bind the source and destination commits, preserve history or an approved provenance manifest, classify every moved and omitted path, identify package and documentation redirects, name owners or vacancies, validate both candidate and resulting states, and prove rollback does not restore stale claims.

Retirement must preserve the last supported source identity, evidence and limitations, dependency and license notes, unresolved security considerations, replacement route if any, and an unmistakable non-current status.
