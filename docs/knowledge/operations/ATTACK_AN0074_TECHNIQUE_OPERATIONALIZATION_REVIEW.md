# Analytic 0074 Technique Operationalization Review

## Reference

- Technique: **AN0074 — Analytic 0074**

Correlated registry modifications under Print Processors path, followed by DLL file creation within the system print processor directory, and DLL load by spoolsv.exe. Malicious execution often occurs during service restart or system boot, with SYSTEM-level privileges.

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
- AN0074: https://attack.mitre.org/detectionstrategies/DET0026#AN0074
- Reviewed: 2026-10-27
