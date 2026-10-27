# ShrinkLocker Technique Operationalization Review

## Reference

- Technique: **S1178 — ShrinkLocker**

ShrinkLocker is a VBS-based malicious script that leverages the legitimate Bitlocker application to encrypt files on victim systems for ransom. ShrinkLocker functions by using Bitlocker to encrypt files, then renames impacted drives to the adversary’s contact email address to facilitate communication for the ransom payment.

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
- S1178: https://attack.mitre.org/software/S1178
- Reviewed: 2026-10-27
