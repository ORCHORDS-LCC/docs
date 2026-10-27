# Spearphishing Link Mitigation Technique Operationalization Review

## Reference

- Technique: **T1192 — Spearphishing Link Mitigation**

Because this technique involves user interaction on the endpoint, it's difficult to fully mitigate. However, there are potential mitigations. Users can be trained to identify social engineering techniques and spearphishing emails with malicious links. Determine if certain websites that can be used for spearphishing are necessary for business operations and consider blocking access if activity cannot be monitored well or if it poses a significant risk. Other mitigations can take place as User Execution occurs.

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
- T1192: https://attack.mitre.org/mitigations/T1192
- Reviewed: 2026-10-27
