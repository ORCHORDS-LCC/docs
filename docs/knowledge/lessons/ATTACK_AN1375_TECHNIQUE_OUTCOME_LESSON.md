# AN1375 Analytic 1375 Outcome Lesson

## Authoritative description

- Technique: **AN1375 — Analytic 1375**
- Platforms: Windows

A process creates a brand‑new logon session/token (LogonUser*/LsaLogonUser) and then assigns/impersonates it (SetThreadToken/ImpersonateLoggedOnUser) to run actions under that freshly created security context. Chain: (1) suspicious command or script block (e.g., runas /netonly, PowerShell P/Invoke of LogonUser) → (2) ETW/API evidence of LogonUser*/SetThreadToken → (3) Security 4624 New Logon (often LogonType=9 NewCredentials or 2/3 from a non‑interactive parent) with no interactive desktop → (4) sysmon 1 process(es) executing with the new LogonId/SID different from the parent process → (5) optional privileged ops/lateral movement.

## Reusable lesson

This technique should be treated as an explicit review question when it is relevant to the system or organisation, rather than assumed to be covered by a generic control statement or by tooling that reports a related signal.

## Apply the lesson

1. Define the real scope before judging coverage.
2. Inspect current technical, process, governance, or operational evidence.
3. Separate documented intent from verified behaviour.
4. Record partial coverage and unresolved gaps instead of converting them into a pass.
5. Revisit when the underlying scope, threat environment, technology, suppliers, or mission materially changes.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- AN1375: https://attack.mitre.org/detectionstrategies/DET0498#AN1375
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
