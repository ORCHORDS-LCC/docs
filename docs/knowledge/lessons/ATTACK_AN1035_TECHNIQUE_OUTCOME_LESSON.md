# AN1035 Analytic 1035 Outcome Lesson

## Authoritative description

- Technique: **AN1035 — Analytic 1035**
- Platforms: Windows

Detects tampered hardware or firmware via anomalous host status telemetry. Behavioral chain: (1) Pre-OS or firmware components exhibit unexpected version changes, signature failures, or modified boot paths; (2) System management/firmware tools log hardware inventory drift; (3) Sensor health telemetry or boot attestation events fail baseline checks; (4) Follow-on process execution from altered firmware or unknown drivers after boot.

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
- AN1035: https://attack.mitre.org/detectionstrategies/DET0368#AN1035
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
