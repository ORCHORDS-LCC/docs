# AN0799 Analytic 0799 Outcome Lesson

## Authoritative description

- Technique: **AN0799 — Analytic 0799**
- Platforms: macOS

Cause→effect chain: (1) App crash/abnormal termination in unified logs for Safari/Chrome/Office/Preview, (2) new files/scripts in ~/Library, ~/Downloads, /private/var/folders/*, (3) unexpected child (osascript, zsh, bash, curl) spawned by those apps, (4) new outbound connections.

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
- AN0799: https://attack.mitre.org/detectionstrategies/DET0287#AN0799
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
