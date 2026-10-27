# AN0138 Analytic 0138 Outcome Lesson

## Authoritative description

- Technique: **AN0138 — Analytic 0138**
- Platforms: Office Suite

Malicious Office add-ins loaded via VSTO, COM, or VBA auto-load paths. Upon launch of Word/Excel/Outlook, the add-in executes code without user action. Add-in resides in trusted directory or registered via Office COM/VBE subsystem. Behavior includes unsigned add-in execution, anomalous load context, or add-in spawning interpreter process.

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
- AN0138: https://attack.mitre.org/detectionstrategies/DET0050#AN0138
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
