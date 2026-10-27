# AN0071 Analytic 0071 Outcome Lesson

## Authoritative description

- Technique: **AN0071 — Analytic 0071**
- Platforms: Windows

Abuse of trusted Electron apps (Teams, Slack, Chrome) to spawn child processes or execute payloads via malicious command-line arguments (e.g., --gpu-launcher) and modified app resources (.asar). Behavior chain: suspicious parent process (Electron app) → unusual command-line args → child process creation → optional DLL/network artifacts.

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
- AN0071: https://attack.mitre.org/detectionstrategies/DET0025#AN0071
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
