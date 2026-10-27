# Analytic 0502 Technique Operationalization Review

## Reference

- Technique: **AN0502 — Analytic 0502**

Adversary uses a tool like Ruler to configure a malicious Outlook folder Home Page that loads a remote or embedded HTML payload upon folder interaction. Execution chain begins with Outlook launching, a specific folder being accessed, and a suspicious child process being spawned or COM-based execution invoked.

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
- AN0502: https://attack.mitre.org/detectionstrategies/DET0177#AN0502
- Reviewed: 2026-10-27
