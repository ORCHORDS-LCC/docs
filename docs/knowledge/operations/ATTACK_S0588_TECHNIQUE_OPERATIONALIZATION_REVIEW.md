# GoldMax Technique Operationalization Review

## Reference

- Technique: **S0588 — GoldMax**

GoldMax is a second-stage C2 backdoor written in Go with Windows and Linux variants that are nearly identical in functionality. GoldMax was discovered in early 2021 during the investigation into the SolarWinds Compromise, and has likely been used by APT29 since at least mid-2019. GoldMax uses multiple defense evasion techniques, including avoiding virtualization execution and masking malicious traffic.

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
- S0588: https://attack.mitre.org/software/S0588
- Reviewed: 2026-10-27
