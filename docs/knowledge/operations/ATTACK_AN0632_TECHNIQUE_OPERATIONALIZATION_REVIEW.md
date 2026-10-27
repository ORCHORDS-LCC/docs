# Analytic 0632 Technique Operationalization Review

## Reference

- Technique: **AN0632 — Analytic 0632**

Detects binaries disguised as media or document types through extension-only masquerading or by modifying the file signature. Observes execution of files whose extension is not typically executable (.jpg, .txt), yet have valid Mach-O headers or execute via Terminal or launch services.

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
- AN0632: https://attack.mitre.org/detectionstrategies/DET0226#AN0632
- Reviewed: 2026-10-27
