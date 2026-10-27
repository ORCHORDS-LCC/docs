# Analytic 0094 Technique Platform Profile

## Reference

- Technique: **AN0094 — Analytic 0094**
- Platforms named in the source: Windows

Defenders can observe suspicious replacement or tampering of system accessibility binaries (e.g., utilman.exe, sethc.exe, osk.exe) and anomalous modifications to registry keys used to redirect accessibility programs (such as IFEO keys). Additionally, execution of cmd.exe or other suspicious binaries triggered from the login screen by SYSTEM can be correlated as part of a behavior chain.

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
- AN0094: https://attack.mitre.org/detectionstrategies/DET0033#AN0094
- Reviewed: 2026-10-27
