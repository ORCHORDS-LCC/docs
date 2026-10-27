# Analytic 0576 Technique Platform Profile

## Reference

- Technique: **AN0576 — Analytic 0576**
- Platforms named in the source: Windows

Cause→effect chain: (1) A user or service launches an indirection utility (e.g., forfiles.exe, pcalua.exe, wsl.exe, scriptrunner.exe, ssh.exe with -o ProxyCommand/LocalCommand). (2) That utility spawns a secondary program/command (PowerShell, cmd, msiexec, regsvr32, curl, arbitrary EXE) and/or opens outbound network connections. (3) Optional precursor modification of SSH config to persist LocalCommand/ProxyCommand. Correlate process creation, command/script content, file access to %USERPROFILE%\.ssh\config, and network connections from the utility or its child.

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
- AN0576: https://attack.mitre.org/detectionstrategies/DET0200#AN0576
- Reviewed: 2026-10-27
