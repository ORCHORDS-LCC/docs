# T1220 XSL Script Processing Mitigation Outcome Lesson

## Authoritative description

- Technique: **T1220 — XSL Script Processing Mitigation**

Windows Management Instrumentation and/or msxsl.exe may or may not be used within a given environment. Disabling WMI may cause system instability and should be evaluated to assess the impact to a network. If msxsl.exe is unnecessary, then block its execution to prevent abuse by adversaries.

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
- T1220: https://attack.mitre.org/mitigations/T1220
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
