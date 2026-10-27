# Analytic 1495 Technique Platform Profile

## Reference

- Technique: **AN1495 — Analytic 1495**
- Platforms named in the source: Windows

Monitor registry modifications to `HKLM\SYSTEM\CurrentControlSet\Control\Lsa\Security Packages` or `...\OSConfig\Security Packages`, especially insertions of new DLL entries. Correlate this with subsequent DLL module loads into `lsass.exe`. Track unsigned or anomalous DLLs loading into LSASS using image load auditing. LSASS loads unsigned DLL due to AuditLevel=8 registry configuration or System reboot followed by DLL load into lsass.exe.

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
- AN1495: https://attack.mitre.org/detectionstrategies/DET0542#AN1495
- Reviewed: 2026-10-27
