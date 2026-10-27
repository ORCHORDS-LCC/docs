# Analytic 1305 Technique Platform Profile

## Reference

- Technique: **AN1305 — Analytic 1305**
- Platforms named in the source: Windows

Windows-specific environmental keying behavioral chain: (1) Rapid system information discovery through multiple techniques (WMI queries, registry enumeration, network share discovery, hostname/domain checks), (2) Target validation through specific environmental artifact collection (AD domain membership, network topology, installed software versions), (3) Cryptographic operation correlation indicating payload decryption based on collected environmental values, (4) Subsequent malicious code execution following successful environmental validation, (5) Temporal clustering of discovery activities suggesting automated environmental assessment.

## Platform profile

1. Record the platforms in scope and the versions actually deployed.
2. Compare the deployed platform surface against the platforms the source names.
3. Record where the platform provides a native control for the technique, and where it does not.
4. Record the configuration evidence for the native control, where one exists.
5. Record the gap where the platform provides no native control, and the compensating detection.
6. Record the platform version, because platform behaviour changes between versions.

## Evidence

- the platform and version inventory for the scoped estate;
- the configuration export or screenshot for the native control;
- the detection evidence where the platform provides none.

## Limitations

A technique entry describes a class of abuse across platforms. The platform-specific exposure is a property of the deployment, established only by inventory and configuration evidence.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- AN1305: https://attack.mitre.org/detectionstrategies/DET0474#AN1305
- Reviewed: 2026-10-27
