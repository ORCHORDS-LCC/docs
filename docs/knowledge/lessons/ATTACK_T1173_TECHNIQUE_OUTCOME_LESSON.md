# T1173 Dynamic Data Exchange Mitigation Outcome Lesson

## Authoritative description

- Technique: **T1173 — Dynamic Data Exchange Mitigation**

Registry keys specific to Microsoft Office feature control security can be set to disable automatic DDE/OLE execution. Microsoft also created, and enabled by default, Registry keys to completely disable DDE execution in Word and Excel. Ensure Protected View is enabled and consider disabling embedded files in Office programs, such as OneNote, not enrolled in Protected View. On Windows 10, enable Attack Surface Reduction (ASR) rules to prevent DDE attacks and spawning of child processes from Office programs.

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
- T1173: https://attack.mitre.org/mitigations/T1173
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
