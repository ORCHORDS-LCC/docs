# AN0747 Analytic 0747 Outcome Lesson

## Authoritative description

- Technique: **AN0747 — Analytic 0747**
- Platforms: Windows

Detects adversarial archiving using libraries (zlib, zip APIs) invoked by scripts or binaries. Correlates process executions of Python, PowerShell, or custom .NET binaries with DLL/module loads linked to compression libraries, followed by archive file creation.

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
- AN0747: https://attack.mitre.org/detectionstrategies/DET0268#AN0747
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
