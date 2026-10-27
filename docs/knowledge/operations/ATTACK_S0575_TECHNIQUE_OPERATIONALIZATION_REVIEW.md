# Conti Technique Operationalization Review

## Reference

- Technique: **S0575 — Conti**

Conti is a Ransomware-as-a-Service (RaaS) that was first observed in December 2019. Conti has been deployed via TrickBot and used against major corporations and government agencies, particularly those in North America. As with other ransomware families, actors using Conti steal sensitive files and information from compromised networks, and threaten to publish this data unless the ransom is paid.

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
- S0575: https://attack.mitre.org/software/S0575
- Reviewed: 2026-10-27
