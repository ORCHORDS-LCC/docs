# Defacement Mitigation Technique Operationalization Review

## Reference

- Technique: **T1491 — Defacement Mitigation**

Implementing best practices for websites such as defending against Exploit Public-Facing Application . Consider implementing IT disaster recovery plans that contain procedures for taking regular data backups that can be used to restore organizational data. (Ready.gov IT DRP) Ensure backups are stored off system and is protected from common methods adversaries may use to gain access and destroy the backups to prevent recovery.

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
- T1491: https://attack.mitre.org/mitigations/T1491
- Reviewed: 2026-10-27
