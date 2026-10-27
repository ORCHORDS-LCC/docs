# Analytic 0543 Technique Platform Profile

## Reference

- Technique: **AN0543 — Analytic 0543**
- Platforms named in the source: Windows

Detects registry and Group Policy modifications that disable or weaken MFA, suspicious PowerShell usage modifying MFA-related attributes, and anomalous login sessions succeeding without expected MFA challenge.

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
- AN0543: https://attack.mitre.org/detectionstrategies/DET0190#AN0543
- Reviewed: 2026-10-27
