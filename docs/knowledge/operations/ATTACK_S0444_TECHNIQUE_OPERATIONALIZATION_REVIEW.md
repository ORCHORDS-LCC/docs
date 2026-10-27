# ShimRat Technique Operationalization Review

## Reference

- Technique: **S0444 — ShimRat**

ShimRat has been used by the suspected China-based adversary Mofang in campaigns targeting multiple countries and sectors including government, military, critical infrastructure, automobile, and weapons development. The name "ShimRat" comes from the malware's extensive use of Windows Application Shimming to maintain persistence.

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
- S0444: https://attack.mitre.org/software/S0444
- Reviewed: 2026-10-27
