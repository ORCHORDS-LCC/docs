# Analytic 1178 Technique Operationalization Review

## Reference

- Technique: **AN1178 — Analytic 1178**

Correlate DNS queries that generate domains with high entropy or gibberish patterns, combined with short-lived connections from unusual processes. Monitor Sysmon DNS events and Windows Security logs for abnormal query rates and failed lookups.

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
- AN1178: https://attack.mitre.org/detectionstrategies/DET0419#AN1178
- Reviewed: 2026-10-27
