# ProLock Technique Operationalization Review

## Reference

- Technique: **S0654 — ProLock**

ProLock is a ransomware strain that has been used in Big Game Hunting (BGH) operations since at least 2020, often obtaining initial access with QakBot. ProLock is the successor to PwndLocker ransomware which was found to contain a bug allowing decryption without ransom payment in 2019.

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
- S0654: https://attack.mitre.org/software/S0654
- Reviewed: 2026-10-27
