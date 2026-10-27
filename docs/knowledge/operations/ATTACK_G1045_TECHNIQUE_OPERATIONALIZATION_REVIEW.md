# Salt Typhoon Technique Operationalization Review

## Reference

- Technique: **G1045 — Salt Typhoon**

Salt Typhoon is a People's Republic of China (PRC) state-backed actor that has been active since at least 2019 and responsible for numerous compromises of network infrastructure at major U.S. telecommunication and internet service providers (ISP). Salt Typhoon has targeted and leveraged public facing network edge devices to gain access to victim environments. Salt Typhoon has been publicly associated with activities resembling other security industry reported activity groups to include OPERATOR PANDA, RedMike, GhostEmperor, and UNC5807.

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
- G1045: https://attack.mitre.org/groups/G1045
- Reviewed: 2026-10-27
