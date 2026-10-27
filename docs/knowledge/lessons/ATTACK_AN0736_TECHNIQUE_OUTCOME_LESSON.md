# AN0736 Analytic 0736 Outcome Lesson

## Authoritative description

- Technique: **AN0736 — Analytic 0736**
- Platforms: macOS

Abuse of launchctl to execute or manage Launch Agents and Daemons. Defender perspective: correlation of suspicious plist file creation or modification in LaunchAgents/LaunchDaemons directories with subsequent execution of the launchctl command. Abnormal executable paths (e.g., /tmp, /Shared) or launchctl activity followed by network connections are highly suspicious.

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
- AN0736: https://attack.mitre.org/detectionstrategies/DET0265#AN0736
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
