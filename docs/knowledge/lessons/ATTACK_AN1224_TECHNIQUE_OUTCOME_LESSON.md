# AN1224 Analytic 1224 Outcome Lesson

## Authoritative description

- Technique: **AN1224 — Analytic 1224**
- Platforms: macOS

Detects execution patterns where a child process is detached from its original parent, often showing up under 'launchd' (PID 1) with no parent lineage. These breakages in the process tree are indicative of evasive techniques using `daemon()`, `fork()` or background execution flags.

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
- AN1224: https://attack.mitre.org/detectionstrategies/DET0443#AN1224
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
