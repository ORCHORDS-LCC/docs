# AN0693 Analytic 0693 Outcome Lesson

## Authoritative description

- Technique: **AN0693 — Analytic 0693**
- Platforms: Containers

Remote/API driven creation **and** start of a container whose image is not on an allow‑list (or is tagged `latest`), executed by a non-admin principal, and/or started with risky runtime attributes (e.g., `--privileged`, host PID/NET namespaces, sensitive host path mounts, capability adds). Correlates *create* ➜ *start* ➜ first network/process actions from that container within a short time window.

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
- AN0693: https://attack.mitre.org/detectionstrategies/DET0249#AN0693
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
