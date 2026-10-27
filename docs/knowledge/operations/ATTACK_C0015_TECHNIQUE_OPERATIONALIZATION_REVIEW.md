# C0015 Technique Operationalization Review

## Reference

- Technique: **C0015 — C0015**

C0015 was a ransomware intrusion during which the unidentified attackers used Bazar, Cobalt Strike, and Conti, along with other tools, over a 5 day period. Security researchers assessed the actors likely used the widely-circulated Conti ransomware playbook based on the observed pattern of activity and operator errors.

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
- C0015: https://attack.mitre.org/campaigns/C0015
- Reviewed: 2026-10-27
