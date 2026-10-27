# Analytic 0691 Technique Operationalization Review

## Reference

- Technique: **AN0691 — Analytic 0691**

CONTAINERS (Docker/K8s/containerd): A user pulls an untrusted image from a public/unknown registry and then creates/starts a container from that image. Shortly after start, the container spawns unexpected utilities (e.g., curl/wget/bash/python), or makes outbound network connections atypical for the namespace/workload. The analytic correlates Image Creation/Download → Container Creation → Container Start → Command Execution/Network activity within a short window and with a consistent image digest.

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
- AN0691: https://attack.mitre.org/detectionstrategies/DET0248#AN0691
- Reviewed: 2026-10-27
