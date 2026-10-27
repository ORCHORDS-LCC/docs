# AN0177 Analytic 0177 Outcome Lesson

## Authoritative description

- Technique: **AN0177 — Analytic 0177**
- Platforms: Containers

Defenders may detect abuse of container administration commands by observing anomalous use of management utilities (`docker exec`, `kubectl exec`, or API calls to kubelet) correlated with unexpected process creation inside containers. Behavioral chains include unauthorized API requests followed by command execution within running pods or containers, often originating from unusual user accounts, automation scripts, or IP addresses outside the expected cluster management plane.

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
- AN0177: https://attack.mitre.org/detectionstrategies/DET0065#AN0177
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
