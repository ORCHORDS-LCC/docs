# Analytic 2029 Technique Platform Profile

## Reference

- Technique: **AN2029 — Analytic 2029**
- Platforms named in the source: Windows

Process execution without GUI context (e.g., powershell.exe, wscript.exe) generates HTTP traffic with a spoofed User-Agent mimicking a legitimate browser. No corresponding UI application (e.g., msedge.exe) is active or in parent lineage. The User-Agent deviates from known enterprise baselines or contains spoofed platform indicators. User-Agent strings can be gathered with API calls such as `ShellExecuteW` to open the default browser on a socket to receive an HTTP reply, or by hard coding the User-Agent string for a specific browser.

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
- AN2029: https://attack.mitre.org/detectionstrategies/DET0898#AN2029
- Reviewed: 2026-10-27
