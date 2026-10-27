# Analytic 1196 Technique Operationalization Review

## Reference

- Technique: **AN1196 — Analytic 1196**

Abuse of bind mounts to obscure process directories. Defender perspective: detecting anomalous mount operations where a process’s /proc entry is remapped to another directory, often hiding malicious activity from native utilities (ps, top). Behavior chain includes: (1) execution of `mount` with `-o bind` or `-B` flags, (2) modification of /proc entries inconsistent with expected process lineage, and (3) subsequent anomalous activity from processes whose metadata no longer matches execution context.

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
- AN1196: https://attack.mitre.org/detectionstrategies/DET0428#AN1196
- Reviewed: 2026-10-27
