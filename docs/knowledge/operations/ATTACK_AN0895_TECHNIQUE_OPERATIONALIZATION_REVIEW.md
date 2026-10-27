# Analytic 0895 Technique Operationalization Review

## Reference

- Technique: **AN0895 — Analytic 0895**

Processes such as PowerShell, Git, or curl initiating outbound HTTPS POST requests to known code repository APIs (e.g., github.com, gitlab.com) immediately following large file reads. Defender view: correlation between file access of sensitive directories (e.g., Documents, Finance) and abnormal data uploads to repository domains.

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
- AN0895: https://attack.mitre.org/detectionstrategies/DET0318#AN0895
- Reviewed: 2026-10-27
