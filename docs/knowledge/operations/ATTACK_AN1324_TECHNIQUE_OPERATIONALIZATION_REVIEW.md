# Analytic 1324 Technique Operationalization Review

## Reference

- Technique: **AN1324 — Analytic 1324**

Detection of token duplication and impersonation attempts by correlating suspicious command-line executions (e.g., runas) with API calls to DuplicateToken, DuplicateTokenEx, ImpersonateLoggedOnUser, or SetThreadToken. The chain includes the initial command execution or in-memory API invocation → token handle duplication or thread token assignment → a new or existing process assuming the impersonated user's context.

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
- AN1324: https://attack.mitre.org/detectionstrategies/DET0482#AN1324
- Reviewed: 2026-10-27
