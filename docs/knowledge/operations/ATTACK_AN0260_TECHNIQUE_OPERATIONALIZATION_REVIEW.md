# Analytic 0260 Technique Operationalization Review

## Reference

- Technique: **AN0260 — Analytic 0260**

Detects creation or alteration of LaunchAgents or LaunchDaemons with corresponding plist modification followed by execution of associated binaries.

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
- AN0260: https://attack.mitre.org/detectionstrategies/DET0094#AN0260
- Reviewed: 2026-10-27
