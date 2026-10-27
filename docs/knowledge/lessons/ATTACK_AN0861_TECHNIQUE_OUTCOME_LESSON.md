# AN0861 Analytic 0861 Outcome Lesson

## Authoritative description

- Technique: **AN0861 — Analytic 0861**
- Platforms: IaaS

Detection focuses on identifying unauthorized or anomalous changes to compute infrastructure components. Defender perspective: monitor for creation, deletion, or modification of instances, volumes, and snapshots outside of approved change management windows; correlate abnormal activity such as rapid snapshot creation followed by new instance mounts, or repeated infrastructure changes by rarely used accounts. Flagging activity linked to unusual geolocation, API client, or automation script is suspicious.

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
- AN0861: https://attack.mitre.org/detectionstrategies/DET0308#AN0861
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
