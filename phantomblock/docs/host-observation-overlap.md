# Host-Observation Overlap: PhantomBlock and JusticeForMe

## Decision problem

JusticeForMe and XYZ / PhantomBlock both produce Linux host-security observations that could feed Repository `0` during portable first-install inspection. Without an explicit boundary, the portfolio risks duplicate collection, conflicting semantics, false corroboration, inconsistent privacy handling, and two competing evidence contracts.

This page defines a **lowest-coupling candidate split**. It is a documentation proposal only and does not approve migration, installation, privileged collection, network access, remediation, release, or deployment.

## Candidate domain split

| Domain | JusticeForMe candidate responsibility | PhantomBlock candidate responsibility | Shared contract requirement |
|---|---|---|---|
| Accounts and privilege | Local accounts, groups, sudo/admin posture, login policy | No primary ownership | Common device and collection identity |
| Packages and software sources | Installed packages, repositories, package-manager configuration, update posture | Firmware artifact manifests and low-level component identity | Distinct package versus firmware-baseline namespaces |
| Startup and persistence | Services, scheduled jobs, shell initialization, startup agents, persistence indicators | Kernel module, taint, firmware, management-controller, and low-level boot evidence where supported | Canonical persistence and kernel field identities |
| Network configuration | Interfaces, routes, DNS, proxy, VPN, firewall, hotspot/tethering, sharing configuration | Management-plane exposure and explicitly supplied offline PCAP evidence | One network-interface identity and privacy policy |
| Bluetooth and local sharing | Configuration and paired-device inventory where platform support exists | No primary ownership unless a dedicated hardware collector is approved | Device and interface identity reuse |
| Hardware inventory | Basic host/platform metadata needed to interpret OS findings | PCI, DMI, CPU, block, NIC, firmware, and management hardware evidence | One platform-profile identity |
| Kernel integrity | General kernel version/configuration and OS-visible state | Bounded taint, symbol, log, firmware, and management-plane heuristics | Shared status, confidence, limitation, and evidence vocabulary |
| Firmware trust | No primary ownership beyond reporting OS-exposed versions | Firmware artifact comparison against independently governed baselines | Repository `1` baseline identity, applicability, expiry, and revocation |
| Offline traffic evidence | No primary ownership unless separately chartered | Explicitly supplied offline PCAP inspection | Authorization, minimization, parser limits, retention, and artifact binding |
| Remediation | No self-authorized remediation | Dry-run seam only; no active response authority | Repository `1` capability and Repository `0` execution route |

## Canonical evidence rule

Each physical or logical observation must have one canonical field identity. Multiple collectors may contribute evidence to the same field, but they must not create duplicate facts merely because two tools emitted similar records.

A consumer should distinguish:

- **same fact, same evidence source** — duplicate; retain one canonical observation and provenance aliases;
- **same fact, independent evidence sources** — corroborating only when independence is demonstrated;
- **same field, conflicting values** — conflict requiring resolution or `UNKNOWN`;
- **different fields with related meaning** — preserve separately and link explicitly;
- **unsupported or missing collection** — `UNKNOWN`, never implicit pass.

## Shared envelope requirements

Both adapters should eventually emit or be wrapped by the same portfolio host-observation envelope containing:

- device identity and ownership-scope reference;
- request and policy identity;
- collector repository, commit, package, configuration, and toolchain;
- start/end times, clock source, and uncertainty;
- platform profile and privilege class;
- per-check status: `PASS`, `FAIL`, `UNKNOWN`, `SKIPPED`, or `ERROR`;
- canonical field identifiers and typed values;
- finding class, confidence, limitations, and non-claims;
- artifact references, hashes, sizes, media types, redaction, and classification;
- freshness, nonce, replay protection, correlation, correction, and revocation state.

Neither tool should own the canonical envelope by accumulation. Ownership should reside in a dedicated versioned contract package approved by Repository `0`, Repository `1`, and the adapter owners.

## Conflict-resolution order

When JusticeForMe and PhantomBlock disagree:

1. verify device identity, request identity, collection time, and platform profile;
2. verify whether both collectors observed the same canonical field;
3. compare privilege, completeness, errors, unsupported controls, and artifact integrity;
4. prefer neither tool solely because it is newer, more privileged, or more alarming;
5. preserve both source observations and produce a conflict record;
6. resolve only through an approved deterministic rule or human review;
7. keep canonical device state unchanged until Repository `1` accepts a reconciliation receipt.

## Required gluing fixtures

### Duplicate observation

Both tools report the same interface, route, service, kernel version, or device identifier from the same underlying source. Repository `0` must deduplicate without counting two independent confirmations.

### Independent corroboration

The tools report the same canonical fact from demonstrably independent evidence artifacts. Repository `0` may record corroboration while preserving source independence and confidence limits.

### Conflicting observation

The tools report different values for the same field. The result must become a conflict or `UNKNOWN`; no automatic majority or severity rule may silently select a value.

### Partial collection

One tool completes and the other is skipped, unsupported, privilege-limited, interrupted, or errors. Missing output must not be treated as agreement.

### Stale or replayed report

A valid older report must not override a newer accepted device state or bypass a lost-device or baseline revocation.

### Wrong-device binding

A report from a previous, cloned, replaced, or similarly named host must fail device-identity validation.

### Privacy disagreement

One tool emits a field or artifact at a higher classification than the other. The stricter classification and retention rule applies until an approved redaction decision exists.

### Response proposal

A finding from either adapter may inform a Repository `0` proposal, but it cannot create a Repository `1` capability or authorize remediation directly.

## Migration options

### Option A — separate adapters

Keep JusticeForMe and PhantomBlock in separate dedicated repositories with non-overlapping charters and one shared envelope package. This is the lowest-coupling option when hardware/firmware validation requires different maintainers, privileges, dependencies, or release cadence.

### Option B — one host-observation suite

Merge them only if one owner can accept the larger privilege, platform, privacy, validation, packaging, incident, and support surface without weakening isolation. Preserve full histories and keep collectors modular and independently disableable.

### Option C — retain JusticeForMe and retire PhantomBlock

Choose this when PhantomBlock's specialist evidence does not justify its maintenance, baseline-governance, hardware-lab, extension, PCAP, or active-response risk. Preserve the prototype as archived research evidence.

## Decision gates

Before either adapter is promoted:

1. approve separate or combined ownership;
2. select the canonical envelope and field-vocabulary owner;
3. document supported platform and privilege matrices;
4. define device, baseline, artifact, finding, correction, and revocation identities;
5. approve privacy, authorization, retention, incident, emergency-stop, and recovery policies;
6. pass duplicate, conflict, partial, stale, replay, wrong-device, privacy, and response-boundary fixtures;
7. prove that Repository `0` can compose both without changing source evidence;
8. prove that Repository `1` remains the only candidate canonical-state and capability authority;
9. preserve retirement and rollback as valid outcomes.
