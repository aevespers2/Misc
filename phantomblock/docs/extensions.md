# Extensions

XYZ is designed to grow without weakening its defensive purpose.

## Capability categories

Extensions may add passive:

- hardware inventory collectors;
- firmware verifiers;
- kernel or platform detectors;
- PCAP and telemetry analyzers;
- report enrichers;
- evidence exporters.

## Contract

Extensions implement the versioned `Capability` protocol and return a namespace, evidence, and findings. Entry points are registered under `phantomblock.capabilities` for compatibility with the internal package.

```python
class ExampleCapability:
    name = "example"
    api_version = "1"
    category = "detector"
    description = "Example passive detector"
    mutates_target = False

    def run(self, context):
        ...
```

## Guardrails

The general registry rejects duplicate names, unsupported API versions, protocol violations, and capabilities that declare target mutation. An extension must not exploit devices, bypass credentials, flash firmware, alter configuration, or perform isolation through the passive registry.

## Active integrations

Disruptive actions belong behind dedicated interfaces with explicit authorization. A production switch adapter should require:

- authenticated vendor APIs;
- pinned TLS identities where supported;
- least-privilege credentials;
- device and port allowlists;
- human approval or approved automation policy;
- immutable change logging;
- idempotent operation;
- rollback and state verification.

## Review checklist

Before accepting an extension, review its dependencies, permissions, network behavior, filesystem access, error handling, evidence schema, test coverage, licensing, vulnerability history, and behavior when data is unavailable or malformed.
