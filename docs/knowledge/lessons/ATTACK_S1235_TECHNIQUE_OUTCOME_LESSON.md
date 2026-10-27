# S1235 CorKLOG Outcome Lesson

## Authoritative description

- Technique: **S1235 — CorKLOG**
- Platforms: Windows

CorKLOG is a keylogger known to be leveraged by Mustang Panda and was first observed utilized in 2024. CorKLOG is delivered through a RAR archive (e.g., src.rar), which contains two files: an executable (lcommute.exe) and the CorKLOG DLL (mscorsvc.dll). CorKLOG has established persistence on the system by creating services or with scheduled tasks.

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
- S1235: https://attack.mitre.org/software/S1235
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
