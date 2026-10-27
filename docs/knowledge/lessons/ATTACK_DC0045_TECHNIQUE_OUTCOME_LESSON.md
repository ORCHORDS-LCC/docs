# DC0045 Windows Registry Key Deletion Outcome Lesson

## Authoritative description

- Technique: **DC0045 — Windows Registry Key Deletion**

The removal of a registry key within the Windows operating system. *Data Collection Measures:* - Windows Event Logs - Event ID 4658 - Registry Key Handle Closed: Captures when a handle to a registry key is closed, which may indicate deletion. - Event ID 4660 - Object Deleted: Logs when a registry key is deleted. - Sysmon (System Monitor) for Windows - Sysmon Event ID 12 - Registry Key Deleted: Logs when a registry key is removed. - Sysmon Event ID 13 - Registry Value Deleted: Captures removal of specific registry values. - Endpoint Detection and Response (EDR) Solutions - Monitor registry deletions for suspicious behavior.

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
- DC0045: https://attack.mitre.org/datacomponents/DC0045
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
