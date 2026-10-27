# Analytic 1562 Technique Operationalization Review

## Reference

- Technique: **AN1562 — Analytic 1562**

Processes executing commands to query system locale and language settings, such as 'locale', 'echo $LANG', or parsing environment variables. Suspicious activity is indicated by these commands being run by unusual users, automation scripts, or non-administrative processes.

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
- AN1562: https://attack.mitre.org/detectionstrategies/DET0565#AN1562
- Reviewed: 2026-10-27
