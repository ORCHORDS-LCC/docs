# Analytic 0694 Technique Platform Profile

## Reference

- Technique: **AN0694 — Analytic 0694**
- Platforms named in the source: Windows

Defenders observe command-line executions or API-based registry reads targeting sensitive paths like HKLM or HKCU with keyword filters such as 'password', 'cred', or 'logon'. Typically performed by Reg.exe, PowerShell, custom binaries, or offensive tools such as Cobalt Strike. Correlation with process ancestry and command-line arguments indicates suspicious credential discovery activity.

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
- AN0694: https://attack.mitre.org/detectionstrategies/DET0250#AN0694
- Reviewed: 2026-10-27
