# AN1605 Analytic 1605 Outcome Lesson

## Authoritative description

- Technique: **AN1605 — Analytic 1605**
- Platforms: Linux

Adversary invokes 'useradd', 'adduser', or equivalent system commands or scripts to create local users. Detection focuses on command execution and audit trail of passwd/shadow file modifications.

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
- AN1605: https://attack.mitre.org/detectionstrategies/DET0583#AN1605
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
