# AN1261 Analytic 1261 Outcome Lesson

## Authoritative description

- Technique: **AN1261 — Analytic 1261**
- Platforms: Containers

Detection of container image build activity directly on the host using Docker or Kubernetes APIs. Defenders may observe Docker build requests, anomalous Dockerfile instructions (such as downloading code from unknown IPs), or creation of new images followed by immediate deployment. This behavior chain typically consists of an unexpected image creation event correlated with outbound network communication to non-standard or untrusted destinations.

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
- AN1261: https://attack.mitre.org/detectionstrategies/DET0459#AN1261
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
