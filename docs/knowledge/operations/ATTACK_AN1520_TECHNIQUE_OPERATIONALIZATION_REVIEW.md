# Analytic 1520 Technique Operationalization Review

## Reference

- Technique: **AN1520 — Analytic 1520**

Anomalous high-volume access to customer records in CRM software by a non-CRM admin user account, especially following initial authentication from a rare location or device. Behavior includes abnormal access to PII fields or data exports within a short time window.

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
- AN1520: https://attack.mitre.org/detectionstrategies/DET0550#AN1520
- Reviewed: 2026-10-27
