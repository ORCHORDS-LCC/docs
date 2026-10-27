# Analytic 1375 Technique Engineering Review

## Reference

- Technique: **AN1375 — Analytic 1375**

A process creates a brand‑new logon session/token (LogonUser*/LsaLogonUser) and then assigns/impersonates it (SetThreadToken/ImpersonateLoggedOnUser) to run actions under that freshly created security context. Chain: (1) suspicious command or script block (e.g., runas /netonly, PowerShell P/Invoke of LogonUser) → (2) ETW/API evidence of LogonUser*/SetThreadToken → (3) Security 4624 New Logon (often LogonType=9 NewCredentials or 2/3 from a non‑interactive parent) with no interactive desktop → (4) sysmon 1 process(es) executing with the new LogonId/SID different from the parent process → (5) optional privileged ops/lateral movement.

## Engineering review

1. Identify the engineering boundary where the technique would apply: the component, the service, or the deployment.
2. Review the design decision that would prevent the technique, and record the alternative considered.
3. Review the implementation evidence for the preventive control.
4. Review the test coverage that would fail if the control regressed.
5. Review the observability: which signal would show the control is not operating.
6. Record the residual risk where prevention is not achievable, and the detection that compensates.

## Review evidence

- the design record for the preventive decision;
- the implementation or configuration evidence;
- the test record showing the control is exercised;
- the observability mapping.

## Limitations

An engineering review describes what the design and the implementation evidence show. It does not claim the technique has been addressed in production.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- AN1375: https://attack.mitre.org/detectionstrategies/DET0498#AN1375
- Reviewed: 2026-10-27
