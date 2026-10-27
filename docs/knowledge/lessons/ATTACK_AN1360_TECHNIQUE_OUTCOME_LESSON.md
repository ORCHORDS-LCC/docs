# AN1360 Analytic 1360 Outcome Lesson

## Authoritative description

- Technique: **AN1360 — Analytic 1360**
- Platforms: Network Devices

Defenders may observe attempts to disable dedicated crypto hardware on network devices, often visible through anomalous CLI commands, unexpected firmware or configuration updates, and degraded encryption performance. Suspicious indicators include commands that alter hardware acceleration settings (e.g., disabling AES-NI or crypto engines), modification of system image files, or logs showing fallback from hardware to software encryption. Network traffic analysis may also reveal a sudden downgrade in throughput or cipher negotiation behavior consistent with the absence of hardware acceleration.

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
- AN1360: https://attack.mitre.org/detectionstrategies/DET0494#AN1360
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
