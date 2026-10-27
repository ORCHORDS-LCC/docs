# AN0015 Analytic 0015 Outcome Lesson

## Authoritative description

- Technique: **AN0015 — Analytic 0015**
- Platforms: Network Devices

From a defender’s perspective, suspicious bridging is observed when network devices begin allowing traffic that contradicts existing segmentation or access policies. Observable behaviors include sudden modifications to ACLs or firewall rules, unusual cross-boundary traffic flows (e.g., east-west communications across separated VLANs), or simultaneous ingress/egress anomalies. Multi-event correlation is key: configuration changes on a router/firewall followed by unexpected traffic patterns, especially from unusual sources, is a strong indicator of compromise.

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
- AN0015: https://attack.mitre.org/detectionstrategies/DET0006#AN0015
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
