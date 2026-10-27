# Analytic 0461 Technique Operationalization Review

## Reference

- Technique: **AN0461 — Analytic 0461**

Chain: (1) privileged CLI sessions run read-only commands that dump AAA/password policies (e.g., `show aaa`, `show password-policy`); (2) same account changes AAA or user DB shortly after. Use network device AAA/command accounting or syslog.

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
- AN0461: https://attack.mitre.org/detectionstrategies/DET0161#AN0461
- Reviewed: 2026-10-27
