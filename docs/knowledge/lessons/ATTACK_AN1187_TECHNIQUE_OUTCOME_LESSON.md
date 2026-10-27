# AN1187 Analytic 1187 Outcome Lesson

## Authoritative description

- Technique: **AN1187 — Analytic 1187**
- Platforms: IaaS

Detection focuses on correlating snapshot creation events with subsequent instance creation and mounting activities. From a defender perspective, suspicious sequences include snapshot creation by unexpected or newly created IAM users, snapshots created from sensitive volumes without preceding change-control activity, or snapshots immediately followed by mounting to unauthorized instances. Cross-referencing with user behavior, IP geolocation, and automation context helps distinguish benign backup operations from adversary-driven snapshot exploitation.

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
- AN1187: https://attack.mitre.org/detectionstrategies/DET0423#AN1187
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
