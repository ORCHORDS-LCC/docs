# AN0379 Analytic 0379 Outcome Lesson

## Authoritative description

- Technique: **AN0379 — Analytic 0379**
- Platforms: Windows

Detects unauthorized use of SMTP/IMAP/POP3 by suspicious binaries (e.g., PowerShell, rundll32) to exfiltrate data or beacon via email, often bypassing proxy or content filters.

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
- AN0379: https://attack.mitre.org/detectionstrategies/DET0135#AN0379
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
