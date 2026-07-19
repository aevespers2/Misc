# Contributing

## Repository posture

`Misc` is a non-authoritative incubation repository. The XYZ / PhantomBlock subtree is preserved as an implemented but unaccepted prototype, and release remains blocked. Contributions must improve clarity, evidence quality, reproducibility, safety, or disposition without expanding implementation scope by default.

Read `taskchain.md`, `release.md`, `changelog.md`, `punchlist.md`, and the documentation under `phantomblock/docs/` before proposing changes.

## Appropriate contributions

Appropriate work includes:

- correcting inaccurate or overstated documentation;
- improving architecture, trust-boundary, data-flow, and lifecycle diagrams;
- recording reproducible local checks and exact environments;
- adding synthetic, minimized, non-sensitive fixtures;
- improving error visibility or fail-closed behavior without adding capability;
- documenting interfaces and unsupported states;
- clarifying licensing, provenance, data, security, and privacy questions;
- preparing a history-preserving migration or retirement plan;
- fixing broken links, strict MkDocs failures, and accessibility defects.

## Work requiring architectural approval

Do not add or promote the following while ownership is unresolved:

- new collectors, heuristics, integrations, targets, or supported platforms;
- privileged execution, credential handling, or management-plane access;
- active isolation, remediation, firmware writes, or target mutation;
- remote or multi-user dashboard operation;
- real incident, customer, firmware, credential, or PCAP data;
- package, image, Pages, service, or deployment promotion;
- certification, compliance, operational-readiness, or detection-assurance claims;
- a permanent product identity owned by `Misc`.

## Branches and commits

Use a focused branch. Keep commits narrow and descriptive, for example:

- `docs: clarify prototype evidence classification`
- `docs: add extension trust-boundary diagram`
- `test: add synthetic malformed manifest fixture`
- `fix: report unsupported collector state explicitly`

Do not mix a documentation milestone with unrelated implementation changes.

## Pull-request requirements

A pull request should state:

1. the problem being addressed;
2. the exact scope and non-goals;
3. files and contracts affected;
4. whether each change is documentation, implementation, configuration, test evidence, or proposal;
5. commands and results tied to the head commit;
6. security, privacy, privilege, network, data, and licensing effects;
7. compatibility and migration effects;
8. known limitations and unsupported environments;
9. rollback instructions;
10. confirmation that release status and implementation authority were not widened.

## Local checks

From `phantomblock/`:

```bash
python3.11 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[dev,docs]'
ruff check .
pytest
mkdocs build --strict
```

Record exact versions and results. Passing checks are development evidence only; they do not approve release or operational use.

## Documentation standards

Documentation must:

- distinguish implemented, configured, tested, proposed, validated, and approved states;
- keep claims within retained evidence;
- link back to authoritative planning and release records;
- state authorization and safety boundaries prominently;
- use diagrams that describe responsibilities without implying validation;
- avoid unexplained acronyms and compliance theater;
- include limitations, non-goals, and rollback implications;
- pass `mkdocs build --strict` when Pages content changes.

## Security and sensitive information

Never commit credentials, keys, tokens, proprietary firmware, real device identifiers, customer or third-party captures, unredacted findings, or sensitive incident material. Use synthetic examples.

Do not test against systems that you do not own or lack explicit authorization to assess. Do not publish exploit details or operational instructions that are unnecessary for defensive review.

## Review outcome

A contribution may be accepted as prototype evidence without becoming release evidence. Promotion requires a dedicated owning repository, approved charter, complete validation, security and licensing review, provenance, rollback, and explicit authorization.