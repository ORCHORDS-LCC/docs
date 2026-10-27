# SUGARDUMP Technique Operationalization Review

## Reference

- Technique: **S1042 — SUGARDUMP**

SUGARDUMP is a proprietary browser credential harvesting tool that was used by UNC3890 during the C0010 campaign. The first known SUGARDUMP version was used since at least early 2021, a second SMTP C2 version was used from late 2021-early 2022, and a third HTTP C2 variant was used since at least April 2022.

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
- S1042: https://attack.mitre.org/software/S1042
- Reviewed: 2026-10-27
