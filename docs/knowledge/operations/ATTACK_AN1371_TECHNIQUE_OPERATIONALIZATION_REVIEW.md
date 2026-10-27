# Analytic 1371 Technique Operationalization Review

## Reference

- Technique: **AN1371 — Analytic 1371**

Detection of adversary disabling endpoint security tools by unloading launch agents/daemons, modifying configuration profiles, or disabling Gatekeeper/XProtect/logging settings, or removing endpoint agents followed by telemetry loss.

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
- AN1371: https://attack.mitre.org/detectionstrategies/DET0497#AN1371
- Reviewed: 2026-10-27
