# AN1249 Analytic 1249 Outcome Lesson

## Authoritative description

- Technique: **AN1249 — Analytic 1249**
- Platforms: Network Devices

Defenders may observe suspicious SNMP MIB enumeration through abnormal queries for large sets of OIDs, repeated SNMP GETBULK/GETNEXT requests, or queries originating from non-administrative IP addresses. Anomalous use of community strings, authentication failures, or enumeration activity outside maintenance windows may also indicate attempts to dump MIB contents. Correlation across syslog, NetFlow, and SNMP audit data can reveal chains of behavior such as repeated authentication failures followed by successful large-scale OID retrieval.

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
- AN1249: https://attack.mitre.org/detectionstrategies/DET0453#AN1249
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
