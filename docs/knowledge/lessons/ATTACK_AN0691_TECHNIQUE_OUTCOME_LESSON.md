# AN0691 Analytic 0691 Outcome Lesson

## Authoritative description

- Technique: **AN0691 — Analytic 0691**
- Platforms: Linux

CONTAINERS (Docker/K8s/containerd): A user pulls an untrusted image from a public/unknown registry and then creates/starts a container from that image. Shortly after start, the container spawns unexpected utilities (e.g., curl/wget/bash/python), or makes outbound network connections atypical for the namespace/workload. The analytic correlates Image Creation/Download → Container Creation → Container Start → Command Execution/Network activity within a short window and with a consistent image digest.

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
- AN0691: https://attack.mitre.org/detectionstrategies/DET0248#AN0691
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
