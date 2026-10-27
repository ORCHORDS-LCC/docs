# FrostyGoop Incident Technique Operationalization Review

## Reference

- Technique: **C0041 — FrostyGoop Incident**

FrostyGoop Incident took place in January 2024 against a municipal district heating company in Ukraine. Following initial access via likely exploitation of external facing services, FrostyGoop was used to manipulate ENCO control systems via legitimate Modbus commands to impact the delivery of heating services to Ukrainian civilians.

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
- C0041: https://attack.mitre.org/campaigns/C0041
- Reviewed: 2026-10-27
