# Architecture

## Trust boundaries

XYZ separates the trusted scanner environment, target hardware, external network observation point, protected baseline store, reporting service, and optional response integrations.

```text
Verified read-only media
        |
        v
+-----------------------+
| XYZ trusted scanner   |
| inventory + detectors |
+-----------+-----------+
            |
   read-only evidence
            v
+-----------------------+       +----------------------+
| Target platform       |       | Protected baselines  |
| UEFI/NIC/BMC/SSD/PCI  |<----->| hashes + approvals   |
+-----------------------+       +----------------------+
            |
            | evidence reports
            v
+-----------------------+       +----------------------+
| XYZ report/dashboard  |<------| TAP/SPAN PCAP input  |
+-----------+-----------+       +----------------------+
            |
      reviewed action
            v
+-----------------------+
| Dry-run isolation API |
| vendor adapter seam   |
+-----------------------+
```

## Components

### Trusted boot image

A `mkosi` definition creates a bootable Linux environment with a read-only root and volatile runtime state. Operational deployments should add verified boot, signing, measured-boot evidence, approved media handling, and configuration control.

### Inventory engine

The engine gathers PCI, DMI, CPU, block, network, module, and firmware data using trusted-environment tools. Command outputs are retained as evidence instead of being normalized beyond recognition.

### Integrity verification

Readable firmware artifacts are hashed and compared with a protected manifest populated from independently verified vendor releases or approved organizational baselines.

### Detection modules

Kernel, management-plane, and traffic-analysis modules produce findings. Decision policy is separate from collection so thresholds can evolve without rewriting evidence gathering.

### Extension registry

Passive capabilities implement a versioned protocol and are loaded through entry points. The general registry rejects extensions that declare target mutation.

### Response boundary

Network isolation uses a separate adapter interface. The included adapter is dry-run only. Production adapters require authentication, allowlists, approval, audit logging, idempotency, and rollback verification.

### Reporting

Reports use a versioned JSON schema and feed a FastAPI service and simple fleet dashboard. Future sinks can include signed evidence bundles, SIEM integration, and eMASS-oriented artifact exports.
