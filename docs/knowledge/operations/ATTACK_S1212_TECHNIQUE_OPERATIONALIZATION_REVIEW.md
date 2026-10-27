# RansomHub Technique Operationalization Review

## Reference

- Technique: **S1212 — RansomHub**

RansomHub is a ransomware-as-a-service (RaaS) offering with Windows, ESXi, Linux, and FreeBSD versions that has been in use since at least 2024 to target organizations in multiple sectors globally. RansomHub operators may have purchased and rebranded resources from Knight (formerly Cyclops) Ransomware which shares infrastructure, feature, and code overlaps with RansomHub.

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
- S1212: https://attack.mitre.org/software/S1212
- Reviewed: 2026-10-27
