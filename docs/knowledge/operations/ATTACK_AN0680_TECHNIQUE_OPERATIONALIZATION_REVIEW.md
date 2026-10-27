# Analytic 0680 Technique Operationalization Review

## Reference

- Technique: **AN0680 — Analytic 0680**

Unusual or excessive database/table exports from SaaS database platforms (e.g., Snowflake, Firebase, BigQuery, Airtable) by users or apps not in known analytics or dev groups. Defender observes access patterns outside baseline working hours or with new query templates, and correlates those with audit logs or file downloads.

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
- AN0680: https://attack.mitre.org/detectionstrategies/DET0242#AN0680
- Reviewed: 2026-10-27
