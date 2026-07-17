# Threat Model

## Assets

XYZ protects the integrity of assessment evidence, trusted baselines, scanner media, reports, extension code, release artifacts, switch credentials, and operator decisions.

## Adversary capabilities considered

- persistence below the host operating system;
- modification of firmware or device configuration;
- concealment from endpoint telemetry;
- abuse of BMC, AMT, IPMI, Redfish, or related channels;
- manipulation of local logs or installed tools;
- tampering with scanner media or known-good baselines;
- malicious or vulnerable extensions;
- forged reports or unauthorized isolation requests.

## Primary mitigations

- boot from independently verified read-only media;
- preserve raw command evidence;
- protect known-good manifests outside the assessed host;
- separate evidence collection from classification;
- require corroboration before a compromised verdict;
- reject mutating general-purpose extensions;
- default response actions to dry-run;
- generate checksums and an SBOM for binary releases;
- restrict dashboard binding to localhost by default;
- document authorization and human-review requirements.

## Residual risks

XYZ cannot guarantee visibility into every firmware region or device processor. Vendor interfaces may not expose complete firmware images. A compromised platform may interfere with collection even when booted externally. Hash equality does not prove absence of design-level backdoors, and a hash mismatch does not prove malicious modification. Network encryption can conceal payload content, and unavailable baselines can limit confidence.

## Required operational controls

Operational deployments should use signed scanner media, controlled baseline ingestion, write-protected evidence storage, time synchronization, chain-of-custody procedures, role-based access, approved cryptography, vulnerability monitoring, extension review, secure release provenance, and independent verification on representative hardware.
