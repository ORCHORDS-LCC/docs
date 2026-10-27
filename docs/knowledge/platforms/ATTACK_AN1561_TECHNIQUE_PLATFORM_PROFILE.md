# Analytic 1561 Technique Platform Profile

## Reference

- Technique: **AN1561 — Analytic 1561**
- Platforms named in the source: Windows

Registry access to system language keys (e.g., HKLM\SYSTEM\CurrentControlSet\Control\Nls\Language) or suspicious processes invoking locale-related APIs (e.g., GetUserDefaultUILanguage, GetSystemDefaultUILanguage, GetKeyboardLayoutList). Defender visibility focuses on anomalous or non-standard processes issuing these queries, especially when run by unknown binaries or scripts.

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
- AN1561: https://attack.mitre.org/detectionstrategies/DET0565#AN1561
- Reviewed: 2026-10-27
