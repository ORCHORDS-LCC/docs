# Container Creation Technique Platform Profile

## Reference

- Technique: **DC0072 — Container Creation**
- Platforms named in the source: not stated

"Container Creation" data component captures details about the initial construction of a container in a containerized environment. This includes events where a new container is instantiated, such as through Docker, Kubernetes, or other container orchestration platforms. Monitoring these events helps detect unauthorized or potentially malicious container creation. Examples: - Docker Example: `docker create my-container`, `docker run --name=my-container nginx:latest` - Kubernetes Example: `kubectl run my-pod --image=nginx`, `kubectl create deployment my-deployment --image=nginx` - Cloud Container Services Example - AWS ECS: Task or service creation (`RunTask` or `CreateService`). - Azure Container Instances: Deployment of a container group. - Google Kubernetes Engine (GKE): Creation of new pods via GCP APIs.

## Platform profile

1. Record the platforms in scope and the versions actually deployed.
2. Compare the deployed platform surface against the platforms the source names.
3. Record where the platform provides a native control for the technique, and where it does not.
4. Record the configuration evidence for the native control, where one exists.
5. Record the gap where the platform provides no native control, and the compensating detection.
6. Record the platform version, because platform behaviour changes between versions.

## Evidence

- the platform and version inventory for the scoped estate;
- the configuration export or screenshot for the native control;
- the detection evidence where the platform provides none.

## Limitations

A technique entry describes a class of abuse across platforms. The platform-specific exposure is a property of the deployment, established only by inventory and configuration evidence.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- DC0072: https://attack.mitre.org/datacomponents/DC0072
- Reviewed: 2026-10-27
