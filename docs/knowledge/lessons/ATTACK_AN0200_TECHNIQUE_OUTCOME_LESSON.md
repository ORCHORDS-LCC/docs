# AN0200 Analytic 0200 Outcome Lesson

## Authoritative description

- Technique: **AN0200 — Analytic 0200**
- Platforms: Linux

Abuse of systemctl to execute commands or manage systemd services. Defender perspective: correlate suspicious service creation or modification with execution of systemctl subcommands such as start, enable, or status. Detect cases where systemctl is used to load services from unusual locations (e.g., /tmp, /dev/shm) or where new service units are created outside of expected administrative workflows.

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
- AN0200: https://attack.mitre.org/detectionstrategies/DET0073#AN0200
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
