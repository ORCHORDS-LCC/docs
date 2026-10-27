# Analytic 0785 Technique Platform Profile

## Reference

- Technique: **AN0785 — Analytic 0785**
- Platforms named in the source: Windows

Detection focuses on identifying anomalous regsvr32.exe executions that deviate from normal administrative or system use. Defenders may observe regsvr32.exe loading scriptlets or DLLs from unusual paths (especially temporary directories or remote URLs), command-line arguments invoking /i or /u with suspicious file references, network connections initiated by regsvr32.exe, and unsigned or untrusted DLLs being loaded shortly after regsvr32.exe invocation. Correlated sequences include regsvr32.exe process creation, module load of DLL/scriptlet, and optional outbound network traffic.

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
- AN0785: https://attack.mitre.org/detectionstrategies/DET0282#AN0785
- Reviewed: 2026-10-27
