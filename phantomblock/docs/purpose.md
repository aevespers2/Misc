# Why the Prototype Exists

## Research motivation

Conventional endpoint security commonly receives telemetry from the operating system it protects. That model is useful for many threats, but it may provide incomplete visibility when relevant state resides in firmware, management controllers, device processors, privileged kernel paths, or external network observation points.

XYZ / PhantomBlock is a research prototype exploring whether a separately controlled review environment can collect and organize evidence from those areas without treating the installed operating system as the sole root of trust.

This is a research motivation, not a claim that the prototype currently detects implants, establishes a trustworthy scanner, supports representative hardware, or is suitable for operational deployment.

## Intended bounded evaluation

Subject to explicit authorization and an approved owning repository, the prototype may be useful for evaluating design questions related to:

- incident-response laboratory workflows;
- firmware and platform-security evidence collection;
- hardware inventory and baseline comparison;
- out-of-band management exposure review;
- offline analysis of externally captured network traffic;
- conservative aggregation of low-level observations;
- separation of passive collection from disruptive response.

The current repository does not approve real-system assessment, production use, or expansion into additional platforms and integrations.

## Threats and anomalies of interest

The design considers evidence associated with:

- unexpected firmware or device-version differences;
- undocumented or unexpected hardware inventory;
- exposed management-plane interfaces;
- kernel modules, taint, hooks, or low-level indicators requiring review;
- network behavior visible from a TAP, SPAN, or mirror source;
- persistence or communication paths that may not be fully represented in ordinary endpoint telemetry.

An observation is not attribution or proof of compromise. A language, runtime, process, port, hash mismatch, or heuristic signal must not be treated as dispositive without an approved corroboration policy and independently reviewable evidence.

## Design values

The prototype is organized around these values:

1. **Authorization first** — assessment authority is external and must be explicit.
2. **Evidence before conclusions** — observations and limitations remain reviewable.
3. **Independent baseline governance** — a target does not certify itself.
4. **Conservative interpretation** — unsupported and ambiguous states stay visible.
5. **Passive defaults** — collection should avoid mutation.
6. **Separated response authority** — disruptive action requires additional approval and controls.
7. **Reproducibility** — results are tied to exact source, tools, environment, and inputs.
8. **Claims discipline** — implementation, configuration, testing, validation, and approval are distinct states.
9. **Reversibility** — migration, rollback, and retirement remain available.

## Non-goals

XYZ is not:

- an offensive exploitation framework;
- a credential-bypass or persistence mechanism;
- a firmware-flashing utility;
- a universal malware or implant detector;
- an autonomous scanner or remediation service;
- a substitute for vendor analysis or laboratory hardware forensics;
- proof that any person, organization, or nation is responsible for an observation;
- automatically compliant with NIST, DoD, Army, CMMC, DISA, or other requirements;
- certified, authorized, production-ready, or released;
- a permanent product owned by `Misc`.

## Why the current hold matters

The repository accumulated implementation, packaging, and Pages artifacts before a dedicated owner and incubation contract were approved. Preserving that work is useful, but allowing it to continue expanding in `Misc` would make ownership and authority ambiguous.

The correct next step is therefore architectural review: assign the prototype to a dedicated approved repository with a charter, or retire/archive it with provenance and limitations preserved.