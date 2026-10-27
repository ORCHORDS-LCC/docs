# Resource Hijacking Technique Operationalization Review

## Reference

- Technique: **T1496 — Resource Hijacking**

Adversaries may leverage the resources of co-opted systems to complete resource-intensive tasks, which may impact system and/or hosted service availability. Resource hijacking may take a number of different forms. For example, adversaries may: * Leverage compute resources in order to mine cryptocurrency * Sell network bandwidth to proxy networks * Generate SMS traffic for profit * Abuse cloud-based messaging services to send large quantities of spam messages In some cases, adversaries may leverage multiple types of Resource Hijacking at once.

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
- T1496: https://attack.mitre.org/techniques/T1496
- Reviewed: 2026-10-27
