# AN0383 Analytic 0383 Outcome Lesson

## Authoritative description

- Technique: **AN0383 — Analytic 0383**
- Platforms: Windows

Detection of unauthorized modification of Active Directory SID-History attributes to escalate privileges. This chain involves: (1) privileged operations or API calls to DsAddSidHistory or related AD modification functions, (2) observed attribute changes in SID-History (Event ID 5136), (3) new logon sessions where the token includes unexpected or privileged SID-History values, and (4) follow-on resource access using elevated privileges derived from SID-History injection.

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
- AN0383: https://attack.mitre.org/detectionstrategies/DET0136#AN0383
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
