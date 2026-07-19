# Design Contracts

This document records the prototype's intended contracts without converting proposals into implementation claims. Source code remains the authority for present behavior; `taskchain.md` and `release.md` remain the authority for scope and release status.

## Contract 1: authorization before assessment

Every assessment must have a recorded authorization boundary covering the system, operator, data, time window, collection methods, network access, credentials, and permitted response actions.

The prototype does not provide legal authority, ownership proof, consent, or organizational approval. A successful command execution is never evidence that an assessment was authorized.

## Contract 2: collection is not trust

Collected output is evidence from an untrusted or partially trusted subject. The collection environment may reduce dependence on the installed operating system, but it does not automatically make tools, firmware readers, device interfaces, or returned data trustworthy.

Collectors should:

- retain raw command output or source metadata when practical;
- record command, version, environment, timestamp, and failure state;
- avoid destructive writes;
- fail visibly rather than silently substituting guessed values;
- distinguish unavailable, unsupported, denied, malformed, and mismatched results.

## Contract 3: baselines are independently governed

A baseline must not be derived solely from the system being assessed. A valid baseline record should identify:

- artifact identity and version;
- device and platform applicability;
- source and retrieval method;
- cryptographic digest and algorithm;
- approval status and approver;
- license or redistribution restrictions;
- validity interval and revocation state;
- known exceptions and superseding records.

A hash mismatch means **different from the supplied baseline**, not automatically compromised.

## Contract 4: findings remain explainable

A finding should include enough information for an independent reviewer to understand:

- the observation;
- the source evidence;
- the rule or comparison that produced the finding;
- confidence and severity;
- limitations and alternative explanations;
- recommended next review step;
- whether corroboration exists.

No single open port, taint flag, firmware mismatch, kernel hook indicator, or traffic heuristic should be promoted to a definitive compromise conclusion without approved corroboration policy.

## Contract 5: output is immutable evidence, not mutable state

Reports should be written as append-only evidence artifacts whenever practical. A future accepted schema should include:

```yaml
schema_version: "proposed-1"
assessment_id: "stable identifier"
created_at: "RFC 3339 timestamp"
source_commit: "immutable repository commit"
environment:
  operating_system: "collector environment"
  python: "runtime version"
  tools: []
authorization:
  reference: "external approval reference"
  scope_digest: "digest of approved scope"
inputs:
  manifests: []
  pcaps: []
  extensions: []
observations: []
findings: []
limitations: []
errors: []
provenance:
  digest_algorithm: "sha256"
  report_digest: "computed after canonicalization"
  signature: null
```

This is a design target, not a claim that the present JSON output implements every field.

## Contract 6: extensions are untrusted

Entry-point discovery provides extensibility, not safety. Third-party extensions may execute code in the host process and therefore require review, provenance, version pinning, isolation strategy, and an allowlist before use.

Passive extension requirements should include:

- no target mutation;
- no implicit credential use;
- no unrestricted network access;
- deterministic input/output where feasible;
- bounded execution time and resource use;
- explicit failure reporting;
- schema validation;
- provenance and version recording.

A future production-grade extension model may require process isolation or a more restrictive protocol. That boundary is not established by the current registry alone.

## Contract 7: disruptive response is separate

Collection and interpretation must not confer response authority. Isolation or remediation requires a separately approved interface with:

- authenticated operator and target identity;
- explicit allowlists;
- human confirmation;
- dry-run output;
- idempotency;
- audit logging;
- precondition checks;
- rollback or restoration procedure;
- post-action verification;
- clear failure and partial-failure states.

The included switch adapter is dry-run only and must remain classified that way.

## Contract 8: dashboard exposure is opt-in

The dashboard defaults to loopback and should remain read-only. Any non-loopback binding, remote access, authentication, TLS termination, multi-user operation, or retention of real findings requires a separate security and privacy design.

A report directory should be treated as sensitive. It may disclose device identifiers, firmware versions, network details, kernel state, and investigative hypotheses.

## Contract 9: reproducibility is candidate-specific

Evidence must identify the exact commit, dependencies, environment, commands, inputs, and artifacts. A prior passing workflow cannot certify a later source or documentation head.

A release candidate requires one immutable source commit with:

- clean-environment installation evidence;
- lint and test results;
- representative and adversarial fixtures;
- retained build artifacts where applicable;
- SBOM and checksums;
- vulnerability review;
- signed provenance where approved;
- independent review and rollback evidence.

## Contract 10: claims cannot outrun evidence

Use the following language discipline:

| Evidence state | Allowed wording |
|---|---|
| Source exists | "The prototype implements…" |
| Workflow exists | "The repository configures…" |
| One bounded run passed | "A recorded run at commit X demonstrated…" |
| Representative validation passed | "The reviewed candidate supports… within the tested matrix." |
| Formal approval granted | "The named authority approved… under the recorded conditions." |

Avoid claims such as "secure," "trusted," "certified," "compliant," "Army approved," "production ready," or "detects implants" unless the required evidence and authority are explicitly recorded.

## Contract review checklist

Before changing a contract, record:

1. the problem and affected users;
2. present behavior and evidence;
3. the proposed change;
4. compatibility and migration effects;
5. threat-model changes;
6. test and validation requirements;
7. documentation and release effects;
8. approving owner;
9. rollback or retirement path.

While XYZ remains in `Misc`, contract changes should clarify or constrain the prototype rather than widen its capability.