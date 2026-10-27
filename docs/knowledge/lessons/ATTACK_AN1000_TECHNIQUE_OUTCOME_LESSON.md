# AN1000 Analytic 1000 Outcome Lesson

## Authoritative description

- Technique: **AN1000 — Analytic 1000**
- Platforms: Windows

Detects unauthorized Kerberos ticket injection by correlating service ticket (TGS - 4769) requests with absent corresponding account logons (4624) and prior Ticket Granting Ticket (TGT - 4768) activity. Highlights anomalous service ticket generation chains involving unexpected users, hosts, or times, and suspicious injection of tickets via mimikatz-like tooling into LSASS memory. Behavior also includes network lateral movement using Kerberos authentication absent expected interactive logon patterns.

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
- AN1000: https://attack.mitre.org/detectionstrategies/DET0352#AN1000
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
