# AN0297 Analytic 0297 Outcome Lesson

## Authoritative description

- Technique: **AN0297 — Analytic 0297**
- Platforms: Windows

Detects PE injection through a behavioral sequence where one process opens (OpenProcess) a handle to another, allocates remote memory (VirtualAllocEx), writes a PE header (MZ) or shellcode (WriteProcessMemory), then initiates a new thread (CreateRemoteThread or NtCreateThreadEx) in that process—executing injected code in memory without touching disk. Optional: injects a trampoline or shellcode that unpacks/reflectively maps the payload.

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
- AN0297: https://attack.mitre.org/detectionstrategies/DET0106#AN0297
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
