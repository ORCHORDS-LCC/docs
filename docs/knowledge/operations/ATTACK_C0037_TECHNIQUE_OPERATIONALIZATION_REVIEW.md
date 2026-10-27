# Water Curupira Pikabot Distribution Technique Operationalization Review

## Reference

- Technique: **C0037 — Water Curupira Pikabot Distribution**

Pikabot was distributed in Water Curupira Pikabot Distribution throughout 2023 by an entity linked to BlackBasta ransomware deployment via email attachments. This activity followed the take-down of QakBot, with several technical overlaps and similarities with QakBot, indicating a possible connection. The identified activity led to the deployment of tools such as Cobalt Strike, while coinciding with campaigns delivering DarkGate and IcedID en route to ransomware deployment.

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
- C0037: https://attack.mitre.org/campaigns/C0037
- Reviewed: 2026-10-27
