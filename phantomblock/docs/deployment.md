# Deployment

## Laboratory installation

```bash
cd phantomblock
python -m venv .venv
. .venv/bin/activate
python -m pip install -e '.[dev]'
xyz collect --output state/report.json
xyz dashboard --state-dir state
```

The dashboard binds to `127.0.0.1` by default. Do not expose it to a network without authentication, TLS termination, access control, and deployment review.

## Standalone binary

```bash
./packaging/build-binary.sh
```

The build produces the `xyz` executable, a SHA-256 checksum, and a CycloneDX SBOM. Operational releases should also be signed, accompanied by provenance, scanned for vulnerabilities, and built in a controlled reproducible environment.

## Live image

```bash
sudo ./image/build.sh
```

Before field use:

1. pin and review all package sources;
2. build in a controlled environment;
3. sign the image and publish its checksum;
4. validate Secure Boot and measured-boot behavior;
5. test supported hardware classes;
6. write the image to controlled read-only or write-protected media;
7. document evidence handling and chain of custody.

## Assessment procedure

1. Record asset identity, operator, date, location, and authorization.
2. Verify scanner-media signature and checksum.
3. Disconnect or control network access as the procedure requires.
4. Boot XYZ instead of the installed operating system.
5. mount evidence storage according to the approved procedure;
6. load the protected known-good manifest;
7. run collection and save the JSON report;
8. obtain external TAP/SPAN traffic where authorized;
9. review evidence before making an isolation decision;
10. preserve reports, hashes, logs, and analyst notes.

## Production hardening

Production deployments need authentication, encrypted evidence transport, role separation, signed reports, immutable logs, key management, backup and recovery, vulnerability-response procedures, release approval, configuration baselines, and platform-specific validation.
