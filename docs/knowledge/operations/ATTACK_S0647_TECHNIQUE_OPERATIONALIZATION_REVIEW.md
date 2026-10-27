# Turian Technique Operationalization Review

## Reference

- Technique: **S0647 — Turian**

Turian is a backdoor that has been used by BackdoorDiplomacy to target Ministries of Foreign Affairs, telecommunication companies, and charities in Africa, Europe, the Middle East, and Asia. First reported in 2021, Turian is likely related to Quarian, an older backdoor that was last observed being used in 2013 against diplomatic targets in Syria and the United States.

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
- S0647: https://attack.mitre.org/software/S0647
- Reviewed: 2026-10-27
