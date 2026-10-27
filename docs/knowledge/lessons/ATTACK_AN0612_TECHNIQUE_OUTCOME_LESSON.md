# AN0612 Analytic 0612 Outcome Lesson

## Authoritative description

- Technique: **AN0612 — Analytic 0612**
- Platforms: Containers

Detection of container escape attempts via bind mounts, privileged containers, or abuse of docker.sock. Defenders may observe anomalous volume mount configurations (e.g., hostPath to / or /proc), unexpected privileged container launches, or use of container administration commands to access host resources. These events typically correlate with subsequent process execution on the host outside of normal container isolation.

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
- AN0612: https://attack.mitre.org/detectionstrategies/DET0219#AN0612
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
