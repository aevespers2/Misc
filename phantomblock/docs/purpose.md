# Why XYZ Exists

## The defensive gap

Most endpoint security products receive telemetry from the operating system they are protecting. That model works well for many threats, but it becomes weaker when persistence or communications occur below the OS in firmware, management controllers, device processors, or network paths the host cannot observe.

XYZ was built to reduce that blind spot by starting from independently booted, read-only media and collecting evidence before the installed operating system is trusted.

## Intended use

XYZ is intended for authorized:

- incident-response laboratories;
- firmware and platform-security research;
- high-assurance asset validation;
- hardware-baseline verification;
- defensive evaluation of out-of-band management exposure;
- fleet triage where below-OS persistence is a credible concern.

## Threats of interest

XYZ is designed to help investigate stealth persistence, unauthorized firmware changes, undocumented hardware, exposed management planes, unexpected device behavior, and communications that bypass conventional endpoint visibility. A userland process—including software written in .NET, C#, native code, scripts, or another runtime—may be relevant to an investigation, but XYZ does not assume that a particular language or framework proves the presence of a firmware implant.

## Non-goals

XYZ is not:

- an offensive exploitation framework;
- a firmware flashing utility;
- a credential-bypass tool;
- a universal malware detector;
- a substitute for vendor analysis or laboratory hardware forensics;
- proof that any specific nation-state, organization, or actor is responsible;
- automatically compliant with NIST, DoD, Army, CMMC, or DISA requirements.

## Design intent

The project prioritizes trust minimization, reproducibility, evidence provenance, conservative classification, extensibility, dry-run response, and clear authorization boundaries.
