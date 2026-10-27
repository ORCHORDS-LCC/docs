# Container Creation Technique Operationalization Review

## Reference

- Technique: **DC0072 — Container Creation**

"Container Creation" data component captures details about the initial construction of a container in a containerized environment. This includes events where a new container is instantiated, such as through Docker, Kubernetes, or other container orchestration platforms. Monitoring these events helps detect unauthorized or potentially malicious container creation. Examples: - Docker Example: `docker create my-container`, `docker run --name=my-container nginx:latest` - Kubernetes Example: `kubectl run my-pod --image=nginx`, `kubectl create deployment my-deployment --image=nginx` - Cloud Container Services Example - AWS ECS: Task or service creation (`RunTask` or `CreateService`). - Azure Container Instances: Deployment of a container group. - Google Kubernetes Engine (GKE): Creation of new pods via GCP APIs.

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
- DC0072: https://attack.mitre.org/datacomponents/DC0072
- Reviewed: 2026-10-27
