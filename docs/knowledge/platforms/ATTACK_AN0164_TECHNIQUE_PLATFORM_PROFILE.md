# Analytic 0164 Technique Platform Profile

## Reference

- Technique: **AN0164 — Analytic 0164**
- Platforms named in the source: macOS

Detect manipulation of system or application files in `/Library`, `/System`, or user data directories using FSEvents and Unified Logs. Identify anomalous process execution modifying plist files, structured data, or logs outside expected update cycles.

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
- AN0164: https://attack.mitre.org/detectionstrategies/DET0059#AN0164
- Reviewed: 2026-10-27
