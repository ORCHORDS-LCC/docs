# AN0941 Analytic 0941 Outcome Lesson

## Authoritative description

- Technique: **AN0941 — Analytic 0941**
- Platforms: Windows

Detects the use of message-based injection by monitoring for sequences involving FindWindow (EnumWindows or EnumChildWindows), VirtualAllocEx or related API calls, combined with suspicious PostMessage/SendMessage (e.g., LVM_SETITEMPOSITION) use to SysListView32 controls, followed by LVM_SORTITEMS invocation instead of WriteProcessMemory.

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
- AN0941: https://attack.mitre.org/detectionstrategies/DET0331#AN0941
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
