# Compliance Center

XYZ includes a starting point for security-control traceability and authorization evidence. It does not claim certification, CMMC status, STIG approval, DoD or Army approval, or an Authority to Operate.

## Reference frameworks

The project is being prepared for alignment with:

- NIST SP 800-53 Rev. 5 security and privacy controls;
- NIST SP 800-53A Rev. 5 assessment procedures;
- NIST SP 800-171 Rev. 3 and SP 800-171A Rev. 3 for CUI environments;
- NIST SP 800-218 Secure Software Development Framework;
- DoD Risk Management Framework processes;
- applicable DISA Application Security and Development STIG/SRG requirements;
- Army overlays, mission-owner policies, eMASS evidence, and ATO processes.

## Existing evidence

- read-only live-image definition;
- versioned JSON report schema;
- versioned passive-extension API;
- conservative classification policy;
- dry-run isolation boundary;
- unit tests and CI checks;
- standalone binary build definition;
- SHA-256 checksum generation;
- CycloneDX SBOM generation;
- initial control-to-evidence mapping in `compliance/control-mapping.yml`.

## Required package for formal review

A formal review will normally require:

- system description and mission context;
- information types and security categorization;
- authorization boundary and network diagrams;
- data-flow diagrams and interface inventory;
- hardware and software bill of materials;
- control selection, tailoring, inheritance, and implementation statements;
- STIG checklists and scan evidence;
- cryptographic and FIPS impact analysis;
- threat model and risk assessment;
- secure development and supply-chain evidence;
- vulnerability-management and patch procedures;
- incident-response, continuity, backup, and recovery procedures;
- configuration-management plan;
- test plan, test results, and representative hardware evidence;
- POA&M items with ownership and milestones;
- continuous-monitoring strategy.

## Evidence discipline

Every mapped control should identify the responsible component, implementation statement, configuration, test method, expected result, actual evidence, assessor status, and remediation owner. A control reference by itself is not evidence of implementation.

## Army and DoD tailoring

The final requirements depend on mission, hosting environment, information type, impact level, acquisition path, network connection, and authorizing organization. XYZ should therefore be presented initially as a defensive research prototype and assessment capability, with mappings tailored only after the intended system boundary and deployment context are defined.
