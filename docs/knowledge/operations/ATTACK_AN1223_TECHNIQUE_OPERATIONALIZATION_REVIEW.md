# Analytic 1223 Technique Operationalization Review

## Reference

- Technique: **AN1223 — Analytic 1223**

Detects anomalous process execution patterns where a process's parent terminates quickly after process creation or is re-parented to 'init' (PID 1), often indicating double-fork or daemon-style detachment. These behaviors sever the parent-child relationship and obscure the execution origin in process tree analysis.

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
- AN1223: https://attack.mitre.org/detectionstrategies/DET0443#AN1223
- Reviewed: 2026-10-27
