# HeartCrypt Technique Operationalization Review

## Reference

- Technique: **S9018 — HeartCrypt**

HeartCrypt is a packer-as-a-service (PaaS) used to protect malware that has been available since at least 2024. HeartCrypt has been used to pack a variety of malware including Lumma Stealer, Remcos, and Rhadamanthys. In the HeartCrypt PaaS model, customers submit malware via private messaging services and it is then packed and returned by the operator as a new binary.

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
- S9018: https://attack.mitre.org/software/S9018
- Reviewed: 2026-10-27
