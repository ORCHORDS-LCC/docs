# AN1351 Analytic 1351 Outcome Lesson

## Authoritative description

- Technique: **AN1351 — Analytic 1351**
- Platforms: Windows

A process explicitly forges its parent using EXTENDED_STARTUPINFO + PROC_THREAD_ATTRIBUTE_PARENT_PROCESS (UpdateProcThreadAttribute → CreateProcess[A/W]/CreateProcessAsUserW) or other Native API paths, resulting in **mismatched/implausible lineage** across ETW EventHeader ProcessId, Security 4688 Creator Process ID/Name, and sysmon ParentProcessGuid. Often paired with privilege escalation when the chosen parent runs as SYSTEM.

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
- AN1351: https://attack.mitre.org/detectionstrategies/DET0489#AN1351
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
