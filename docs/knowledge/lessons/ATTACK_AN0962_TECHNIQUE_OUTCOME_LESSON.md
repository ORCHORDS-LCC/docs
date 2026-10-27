# AN0962 Analytic 0962 Outcome Lesson

## Authoritative description

- Technique: **AN0962 — Analytic 0962**
- Platforms: Windows

A user is socially engineered (web page, email, document) to open Run/PowerShell/CMD and paste an obfuscated one-liner. The chain is: (1) user context active in a browser/email/office app → (2) process creation of a command interpreter with suspicious arguments (base64/Invoke-Expression/web download/pipeline to shell) → (3) optional file drop in %TEMP% or %APPDATA% → (4) outbound network connection to an external domain. Events are correlated within a short window and with consistent user/session.

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
- AN0962: https://attack.mitre.org/detectionstrategies/DET0340#AN0962
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
