# Compiled HTML File Mitigation Technique Operationalization Review

## Reference

- Technique: **T1223 — Compiled HTML File Mitigation**

Consider blocking download/transfer and execution of potentially uncommon file types known to be used in adversary campaigns, such as CHM files. Also consider using application whitelisting to prevent execution of hh.exe if it is not required for a given system or network to prevent potential misuse by adversaries.

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
- T1223: https://attack.mitre.org/mitigations/T1223
- Reviewed: 2026-10-27
