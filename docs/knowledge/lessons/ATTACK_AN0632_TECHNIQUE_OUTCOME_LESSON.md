# AN0632 Analytic 0632 Outcome Lesson

## Authoritative description

- Technique: **AN0632 — Analytic 0632**
- Platforms: macOS

Detects binaries disguised as media or document types through extension-only masquerading or by modifying the file signature. Observes execution of files whose extension is not typically executable (.jpg, .txt), yet have valid Mach-O headers or execute via Terminal or launch services.

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
- AN0632: https://attack.mitre.org/detectionstrategies/DET0226#AN0632
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
