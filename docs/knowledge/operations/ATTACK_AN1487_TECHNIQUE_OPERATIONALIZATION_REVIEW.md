# Analytic 1487 Technique Operationalization Review

## Reference

- Technique: **AN1487 — Analytic 1487**

Detects suspicious OAuth application integrations within Office 365 or Google Workspace environments, such as new app registrations, unexpected consent grants, or privilege assignments. Defenders should correlate between application creation/modification events and associated user or service principal activity to identify persistence via app integrations.

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
- AN1487: https://attack.mitre.org/detectionstrategies/DET0539#AN1487
- Reviewed: 2026-10-27
