# AN0571 Analytic 0571 Outcome Lesson

## Authoritative description

- Technique: **AN0571 — Analytic 0571**
- Platforms: Containers

Detection correlates anomalous Docker or Kubernetes API requests with access to logs, secrets, or service accounts. Observes unauthorized use of `docker logs`, `kubectl get secrets`, or direct API calls to Kubernetes API server endpoints. Identifies behavioral patterns where adversaries escalate from basic pod/container interaction to privileged API calls exposing sensitive credential material.

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
- AN0571: https://attack.mitre.org/detectionstrategies/DET0198#AN0571
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
