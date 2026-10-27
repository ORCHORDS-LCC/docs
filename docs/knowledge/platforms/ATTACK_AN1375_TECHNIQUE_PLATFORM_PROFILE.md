# Analytic 1375 Technique Platform Profile

## Reference

- Technique: **AN1375 — Analytic 1375**
- Platforms named in the source: Windows

A process creates a brand‑new logon session/token (LogonUser*/LsaLogonUser) and then assigns/impersonates it (SetThreadToken/ImpersonateLoggedOnUser) to run actions under that freshly created security context. Chain: (1) suspicious command or script block (e.g., runas /netonly, PowerShell P/Invoke of LogonUser) → (2) ETW/API evidence of LogonUser*/SetThreadToken → (3) Security 4624 New Logon (often LogonType=9 NewCredentials or 2/3 from a non‑interactive parent) with no interactive desktop → (4) sysmon 1 process(es) executing with the new LogonId/SID different from the parent process → (5) optional privileged ops/lateral movement.

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
- AN1375: https://attack.mitre.org/detectionstrategies/DET0498#AN1375
- Reviewed: 2026-10-27
