# Analytic 1604 Technique Operationalization Review

## Reference

- Technique: **AN1604 — Analytic 1604**

Adversary uses built-in OS tools or API calls to create local or domain accounts for persistence or lateral movement. Tools such as 'net user', PowerShell, or MMC snap-ins may be used. Detection focuses on Event ID 4720 paired with process lineage and user context.

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
- AN1604: https://attack.mitre.org/detectionstrategies/DET0583#AN1604
- Reviewed: 2026-10-27
