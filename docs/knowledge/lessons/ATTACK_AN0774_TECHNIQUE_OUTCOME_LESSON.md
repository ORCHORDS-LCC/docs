# AN0774 Analytic 0774 Outcome Lesson

## Authoritative description

- Technique: **AN0774 — Analytic 0774**
- Platforms: Windows

Unusual modification of boot records (MBR, VBR) or EFI partitions not associated with legitimate patch cycles or OS upgrades. Registry or WMI events associated with firmware update tools executed from unexpected parent processes. API calls (e.g., DeviceIoControl) writing directly to raw disk sectors. Subsequent abnormal boot configuration changes followed by unsigned driver loads.

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
- AN0774: https://attack.mitre.org/detectionstrategies/DET0278#AN0774
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
