# AN1177 Analytic 1177 Outcome Lesson

## Authoritative description

- Technique: **AN1177 — Analytic 1177**
- Platforms: Windows

Multi-stage Windows DACL manipulation behavioral chain: (1) Process creation of permission-modifying utilities (icacls.exe, takeown.exe, attrib.exe, cacls.exe) or PowerShell ACL cmdlets, (2) Command-line analysis revealing privilege escalation intent through suspicious parameters (/grant, /takeown, /T, Set-Acl), (3) DACL modification events (4670) correlating with process execution, (4) Subsequent file access attempts (4663) indicating successful permission bypass, (5) Potential follow-on persistence or lateral movement activities.

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
- AN1177: https://attack.mitre.org/detectionstrategies/DET0418#AN1177
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
