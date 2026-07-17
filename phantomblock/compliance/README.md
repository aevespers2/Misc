# Compliance Preparation

This directory provides implementation evidence and mappings; it does **not** assert certification, an Authority to Operate, CMMC status, STIG approval, or Army authorization.

## Target references

- NIST SP 800-53 Rev. 5, including current release updates.
- NIST SP 800-53A Rev. 5 assessment procedures.
- NIST SP 800-171 Rev. 3 and SP 800-171A Rev. 3 for deployments handling CUI.
- NIST SP 800-218 SSDF Version 1.1; track the Version 1.2 draft without treating it as final.
- DoD Risk Management Framework and the applicable DISA Application Security and Development STIG/SRG.
- Army implementation overlays, mission-owner policies, and the system's eMASS/ATO package.

## Prepared evidence

- versioned report and extension API schemas
- conservative decision policy with no single-indicator compromise verdict
- read-only boot environment definition
- CI lint and unit tests
- standalone Linux binary build
- SHA-256 release checksum
- CycloneDX SBOM
- plugin mutation guardrails
- dry-run network isolation default
- initial control traceability matrix

## Remaining authorization work

Formal use requires boundary definition, FIPS impact analysis, threat model, data-flow diagrams, dependency vulnerability management, signed provenance, approved cryptographic modules where applicable, STIG checklist results, test evidence on representative hardware, incident-response procedures, configuration management, POA&M tracking, and assessment by the responsible authorizing organization.
