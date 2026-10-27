# AN0645 Analytic 0645 Outcome Lesson

## Authoritative description

- Technique: **AN0645 — Analytic 0645**
- Platforms: Linux

Detects adversarial abuse of systemd timers by correlating file creation/modification of .timer and .service units in system directories with the execution of abnormal child processes launched by 'systemd' (PID 1), especially as root.

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
- AN0645: https://attack.mitre.org/detectionstrategies/DET0231#AN0645
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
