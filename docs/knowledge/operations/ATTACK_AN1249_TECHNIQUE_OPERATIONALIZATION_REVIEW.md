# Analytic 1249 Technique Operationalization Review

## Reference

- Technique: **AN1249 — Analytic 1249**

Defenders may observe suspicious SNMP MIB enumeration through abnormal queries for large sets of OIDs, repeated SNMP GETBULK/GETNEXT requests, or queries originating from non-administrative IP addresses. Anomalous use of community strings, authentication failures, or enumeration activity outside maintenance windows may also indicate attempts to dump MIB contents. Correlation across syslog, NetFlow, and SNMP audit data can reveal chains of behavior such as repeated authentication failures followed by successful large-scale OID retrieval.

## Operationalization review

1. Record the operational scope: which services, environments, and data the technique could affect.
2. Record the runbook that would be executed, and its owner.
3. Record the telemetry the runbook depends on, and whether it is retained long enough to investigate.
4. Record the detection that would surface the technique before or after it has an effect.
5. Record the recovery path, and the evidence that recovery has been rehearsed.
6. Record the residual operational risk where the runbook depends on a manual step.

## Review evidence

- the runbook and its owner;
- the telemetry retention and coverage record;
- the detection mapping;
- the exercise or rehearsal record.

## Limitations

An operationalization review describes the runbook and the evidence around it. It does not claim the technique has been prevented or detected in a live environment.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- AN1249: https://attack.mitre.org/detectionstrategies/DET0453#AN1249
- Reviewed: 2026-10-27
