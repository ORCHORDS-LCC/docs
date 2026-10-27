# Analytic 0240 Technique Platform Profile

## Reference

- Technique: **AN0240 — Analytic 0240**
- Platforms named in the source: Windows

Defender observes execution of commands like `tasklist`, `sc query`, `reg query`, or PowerShell WMI/Registry queries targeting known backup products (e.g., Veeam, Acronis, CrashPlan). Behavior often includes parent-child lineage involving PowerShell or cmd.exe with discovery syntax, and enumeration of services, directories, or registry paths tied to backup software.

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
- AN0240: https://attack.mitre.org/detectionstrategies/DET0088#AN0240
- Reviewed: 2026-10-27
