# AN1502 Analytic 1502 Outcome Lesson

## Authoritative description

- Technique: **AN1502 — Analytic 1502**
- Platforms: IaaS

Monitor for suspicious use of cloud-native administrative command services (e.g., AWS Systems Manager Run Command, Azure RunCommand, GCP OS Config) to execute code inside VMs. Detect anomalies such as commands/scripts executed by unexpected users, execution outside of maintenance windows, or commands initiated by service accounts not normally tied to administration. Correlate cloud control-plane activity logs with host-level execution (process creation, script execution) to validate if commands materialized inside the guest OS.

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
- AN1502: https://attack.mitre.org/detectionstrategies/DET0545#AN1502
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
