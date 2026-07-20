# Obstruction and Gluing Analysis

## Purpose

This document evaluates whether the XYZ / PhantomBlock prototype can compose safely with the A.L.I.S.T.A.I.R.E. portfolio without allowing a temporary incubation repository to become an accidental authority. It treats repositories as bounded local sections and contracts as gluing maps. A successful integration requires compatible identities, schemas, authority, evidence, failure semantics, and rollback across every overlap.

This is an engineering compatibility analysis, not a claim that a formal homology computation has been completed.

## Proposed portfolio role

The lowest-overlap role for PhantomBlock is a **specialist host-firmware, kernel, management-plane, and offline-PCAP observation adapter** beneath Repository `0`'s portable first-install security workflow.

Under that proposal:

- PhantomBlock performs passive or explicitly authorized collection and bounded local analysis;
- Repository `0` owns bootstrap orchestration, host inventory composition, remediation planning, bounded execution, and resulting-state verification;
- Repository `1` owns candidate device identity, baseline-policy identity, proposal admission, capabilities, approvals, revocations, canonical receipts, and recovery checkpoints;
- Bridge may transport approved evidence envelopes but does not create trust or authority;
- QSO-STUDIO or AionUi may display reviewed evidence but do not approve or mutate device state by presentation alone;
- `Misc` remains a temporary evidence-preservation and review location until migration or retirement is approved.

This role is a recommendation only. It does not approve migration, operational use, credentials, privileged collection, remediation, networking, publication, or release.

## Active obstruction ledger

| ID | Class | Obstruction | Why gluing fails | Lowest-scope repair candidate | Status |
|---|---|---|---|---|---|
| PB-O01 | Identity | XYZ, PhantomBlock, `xyz-firmware-defense`, `xyz`, and `phantomblock` are overlapping names without one approved canonical identity. | Repository, package, CLI, schema, documentation, and release identities cannot be versioned coherently. | Select one product/repository identity after ownership approval; retain aliases only through an explicit migration map. | BLOCKED |
| PB-O02 | Ownership | `Misc` contains implementation, packaging, documentation, and workflows but is chartered only as an incubator. | Accumulated artifacts appear to imply product authority that the repository does not possess. | Migrate full history to a dedicated owner or retire/archive the prototype. | BLOCKED |
| PB-O03 | Device identity | Reports do not bind observations to a portfolio-approved device identity and ownership scope. | Repository `0` and Repository `1` cannot distinguish authorized target state, replacement devices, cloned reports, or stale hostnames reliably. | Wrap output in a versioned evidence envelope containing device identity, ownership scope, collector identity, and exact policy version. | PROPOSED |
| PB-O04 | Baseline identity | Trusted firmware manifests and heuristic expectations lack one independently governed baseline authority. | A host-derived or locally edited baseline can be mistaken for canonical trust state. | Repository `1` or another approved authority owns signed baseline identity, applicability, update, revocation, and provenance. | BLOCKED |
| PB-O05 | Evidence completeness | Collection completion, per-check status, skipped controls, privilege limitations, and unsupported platforms are not represented uniformly. | Missing evidence may be interpreted as a passing result. | Add per-check `PASS`, `FAIL`, `UNKNOWN`, `SKIPPED`, and `ERROR` states in an envelope without silently changing current prototype output. | PROPOSED |
| PB-O06 | Freshness and replay | Reports lack accepted freshness windows, nonce or request binding, and replay semantics. | Old or duplicated evidence can be admitted as current device state. | Repository `1` validates request identity, issued-at time, expiry, nonce, expected device, and prior receipt state. | PROPOSED |
| PB-O07 | Artifact binding | Machine-readable reports, logs, PCAP-derived results, manifests, and dashboard views are not bound through one immutable hash manifest. | Consumers cannot prove that displayed findings correspond to the retained source artifacts. | Produce an append-only evidence manifest with hashes, sizes, media types, redaction state, and collector/tool versions. | PROPOSED |
| PB-O08 | Result semantics | Firmware mismatch, suspicious heuristic, missing privilege, parser failure, and unsupported hardware can collapse into similar user-visible findings. | Repository `0` cannot safely decide whether to investigate, retry, quarantine, or propose remediation. | Define versioned finding classes, confidence, evidence references, limitations, and non-claims. | BLOCKED |
| PB-O09 | Authority | Prototype code contains a dry-run isolation seam while operational authority remains undefined. | Detection output could become coupled to disruptive response without an independent capability decision. | Preserve observation and response as separate contracts; any active response requires Repository `1` capability, allowlist, dry-run evidence, human approval, and rollback. | BLOCKED |
| PB-O10 | Credential boundary | BMC, Redfish, IPMI, switch, dashboard, or future vendor adapters may require secrets. | An observation adapter could become a secret store or general remote-administration agent. | Store no live credentials in `Misc`; use an approved external credential broker with device-, action-, destination-, and time-scoped capabilities. | BLOCKED |
| PB-O11 | Network boundary | Management-plane probes, dashboard exposure, update sources, and adapter calls lack one egress and destination policy. | Passive assessment can silently become network discovery or remote control. | Default to offline/local operation; require explicit destination allowlists and capability evidence for any network access. | BLOCKED |
| PB-O12 | Privacy | Hardware identifiers, PCAP metadata, firmware information, hostnames, interfaces, and findings may identify users, devices, and networks. | Public artifacts, Pages, CI, or shared reports could disclose sensitive operational data. | Define classification, minimization, redaction, retention, deletion, and publication rules before real evidence leaves the device. | BLOCKED |
| PB-O13 | Extension boundary | Passive extension registration exists without accepted signing, isolation, resource, or provenance requirements. | Third-party code can widen collection, execution, or exfiltration behavior. | Disable unreviewed extensions by default; require signed identity, declared permissions, bounded resources, deterministic fixtures, and revocation. | BLOCKED |
| PB-O14 | Platform semantics | Linux-oriented collectors and image definitions do not establish macOS, Windows, Android, iOS, firmware-vendor, or hardware coverage. | Repository `0`'s portable baseline cannot treat PhantomBlock as a universal device auditor. | Publish a precise support matrix; unsupported controls return `UNKNOWN` and route to platform-specific adapters. | BLOCKED |
| PB-O15 | Time and ordering | Host clocks, collection order, monotonicity, and event correlation are not governed across device, Repository `0`, Repository `1`, and downstream stores. | Evidence and revocation ordering can disagree during recovery or incident analysis. | Adopt portfolio temporal-envelope rules with source clock, receive time, uncertainty, ordering identity, and correction semantics. | BLOCKED |
| PB-O16 | Incident lifecycle | Quarantine, revocation, evidence preservation, correction, replacement-device enrollment, and bounded restart are not one shared sequence. | A finding can be displayed without reliably propagating freeze or recovery state through the portfolio. | Define one incident state machine owned by Repository `1`, with Repository `0` execution hooks and fail-closed downstream consumption. | BLOCKED |
| PB-O17 | Publication | Pages, dashboard, compliance mappings, and package metadata can look product-ready despite evidence holds. | Public representation may be mistaken for release, certification, or operational assurance. | Keep publication manual and fail-closed; publish only non-sensitive reviewed documentation after explicit approval. | CONTAINED |
| PB-O18 | Rollback and retirement | Migration, package withdrawal, baseline revocation, report correction, and prototype retirement do not share one evidence-preserving process. | Failed integration may leave conflicting identities, artifacts, or trust records. | Require migration/retirement manifests, redirect or archive notices, preserved commits, revocation records, and downstream cache invalidation. | BLOCKED |

## Pairwise gluing contracts

| Edge | Producer responsibility | Consumer responsibility | Required witness |
|---|---|---|---|
| Device → PhantomBlock | Present locally observable hardware, firmware, kernel, management-plane, and authorized PCAP state. | Record collection scope, privilege, completion, platform limits, and raw-evidence references without promoting trust. | Synthetic and representative-device collection fixture with explicit unsupported and privilege-limited cases. |
| PhantomBlock → Repository `0` | Emit a versioned, integrity-bound evidence envelope and findings with limitations. | Validate schema and provenance, compose with other host adapters, and prepare a non-authoritative proposal. | Positive, malformed, incomplete, tampered-artifact, unsupported-version, and privacy-redaction fixtures. |
| Repository `0` → Repository `1` | Submit device-bound proposal, expected pre-state, requested operation, evidence manifest, and rollback plan. | Admit to quarantine; validate identity, policy, freshness, replay, capability, and human-approval requirements. | Accepted, stale, replayed, wrong-device, wrong-baseline, expected-head mismatch, and revoked-capability fixtures. |
| Repository `1` → Repository `0` | Issue narrow capability or rejection tied to exact device, operation, resources, time, and policy. | Execute only permitted action, preserve pre-state, verify post-state, and return a receipt. | Expiry, revocation, partial failure, idempotency, rollback, and unauthorized-action fixtures. |
| Evidence → Bridge | Supply approved transport envelope with classification and destination policy. | Preserve identity, hashes, provenance, and correction/revocation state without creating authority. | Round-trip integrity, unsupported schema, duplicate, correction, revocation, and destination-denial fixtures. |
| Bridge → QSO-STUDIO / AionUi | Deliver reviewed, minimized, non-secret evidence and canonical status. | Render evidence, uncertainty, limitations, and approval state without implying action authority. | Display fixture proving `UNKNOWN`, rejected, revoked, corrected, and superseded states remain visible and non-actionable. |

## Triple-overlap witnesses

Pairwise compatibility is insufficient. The following compositions must produce equivalent meaning across all paths.

### Device → PhantomBlock → Repository `0`

A device observation must preserve the same device identity, collection scope, unsupported controls, privilege limitations, artifact hashes, and finding semantics after Repository `0` composes it with other host-security adapters.

### PhantomBlock → Repository `0` → Repository `1`

A proposal admitted to Repository `1` must refer to the exact evidence envelope produced by PhantomBlock and reviewed by Repository `0`. Repository `0` may add orchestration context but must not rewrite evidence identity, suppress failures, or promote a finding into authority.

### Repository `0` → Repository `1` → response adapter

The response adapter must be unable to execute unless Repository `1` issued a valid, unexpired, device- and action-specific capability. Successful execution returns a receipt but does not automatically update canonical state until reconciliation succeeds.

### PhantomBlock → Bridge → review interface

A displayed finding must remain tied to the same minimized evidence, classification, uncertainty, correction, and revocation state transported by Bridge. The interface must not expose secrets or convert a visual approval gesture into an unversioned privileged action.

### Incident authority → Repository `1` → all downstream consumers

A freeze, device loss, baseline revocation, evidence correction, or recovery decision must invalidate active capabilities and stale caches consistently across Repository `0`, Bridge, interfaces, and adapters.

## Proposed evidence-envelope minimum

A future wrapper around current prototype output should include at least:

```yaml
schema_id: alistaire.host-observation-envelope
schema_version: 0.1-proposal
observation_id: immutable identifier
device_id: approved device identity
ownership_scope: explicit authorization reference
collector:
  repository: dedicated owner after approval
  commit: exact source identity
  package_version: prototype or accepted version
  toolchain: recorded versions
request:
  request_id: Repository 0 request identity
  issued_at: timestamp
  expires_at: timestamp
  nonce: replay-resistant value
policy:
  baseline_id: Repository 1 baseline identity
  baseline_version: immutable version
collection:
  started_at: timestamp
  completed_at: timestamp
  privilege: observed privilege class
  platform_profile: exact support profile
  checks:
    - check_id: stable identifier
      status: PASS | FAIL | UNKNOWN | SKIPPED | ERROR
      evidence_refs: [artifact references]
      limitations: [explicit limitations]
artifacts:
  - path_or_id: local or approved store reference
    sha256: digest
    size: bytes
    media_type: type
    classification: public | internal | sensitive | restricted
findings:
  - finding_id: stable identifier
    class: versioned finding class
    confidence: bounded value or category
    evidence_refs: [artifact references]
    non_claims: [what the result does not establish]
signatures_or_attestations: []
```

The schema above is a documentation proposal. It does not change the current package or establish a trusted signing system.

## Migration or retirement decision

### Migration candidate

If retained, move PhantomBlock with full history into a dedicated security-adapter repository whose charter limits it to evidence collection and bounded analysis. The new repository must define identity, licensing, supported platforms, authorized use, baseline contracts, envelope ownership, security contact, vulnerability response, validation, release, and retirement.

### Retirement candidate

If overlap, risk, licensing, or validation cost outweighs utility, archive the prototype with:

- source and commit history preserved;
- publication disabled;
- package and image artifacts withdrawn or clearly marked unaccepted;
- limitations and unresolved findings retained;
- no trusted-baseline or operational recommendation implied;
- downstream references updated to prevent stale integration assumptions.

## Acceptance criteria

The gluing obstruction is materially reduced only when:

1. a dedicated owner or retirement decision is approved;
2. product, repository, package, CLI, schema, and version identities are reconciled;
3. Repository `0` and Repository `1` approve the device, baseline, proposal, capability, receipt, revocation, and checkpoint contracts;
4. evidence completeness, freshness, replay, privacy, temporal, correction, and artifact-binding rules are versioned;
5. observation and response remain separately authorized;
6. pairwise and triple-overlap fixtures fail closed and are retained at immutable commits;
7. lost-device, compromise, rollback, migration, and retirement exercises preserve evidence and revoke stale authority;
8. public documentation claims match accepted evidence.

Until then, PhantomBlock remains a preserved prototype under bounded review rather than an operational component of the portable first-install security system.
