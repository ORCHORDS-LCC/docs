# Container API Technique Operationalization Review

## Reference

- Technique: **T1552.007 — Container API**

Adversaries may gather credentials via APIs within a containers environment. APIs in these environments, such as the Docker API and Kubernetes APIs, allow a user to remotely manage their container resources and cluster components. An adversary may access the Docker API to collect logs that contain credentials to cloud, container, and various other resources in the environment. An adversary with sufficient permissions, such as via a pod's service account, may also use the Kubernetes API to retrieve credentials from the Kubernetes API server. These credentials may include those needed for Docker API authentication or secrets from Kubernetes cluster components.

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
- T1552.007: https://attack.mitre.org/techniques/T1552/007
- Reviewed: 2026-10-27
