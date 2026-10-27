# MiniBus Technique Operationalization Review

## Reference

- Technique: **S9060 — MiniBus**

MiniBus is a custom backdoor used for command execution, data discovery, gathering, and exfiltration. MiniBus has utilized Azure Cloud Infrastructure and unique adversary-controlled domains for command and control. MiniBus is an updated platform to its predecessor MiniBike and was first observed in August 2023. MiniBus has been affiliated with the cyber espionage threat group NIMBUS MANTICORE.

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
- S9060: https://attack.mitre.org/software/S9060
- Reviewed: 2026-10-27
