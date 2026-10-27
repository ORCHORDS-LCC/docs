# Container Enumeration Technique Platform Profile

## Reference

- Technique: **DC0091 — Container Enumeration**
- Platforms named in the source: not stated

"Container Enumeration" data component captures events and actions related to listing and identifying active or available containers within a containerized environment. This includes information about running, stopped, or configured containers, such as their names, IDs, statuses, or associated images. Monitoring this activity is crucial for detecting unauthorized discovery or reconnaissance efforts. Examples: - Docker Example: `docker ps`, `docker ps -a` - Kubernetes Example: `kubectl get pods`, `kubectl get deployments` - Cloud Container Services Example - AWS ECS: API Call: ListTasks or ListContainers - Azure Kubernetes Service: API Call: List pod or container instances. - Google Kubernetes Engine (GKE): API Call: Retrieve deployments and their associated containers.

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
- DC0091: https://attack.mitre.org/datacomponents/DC0091
- Reviewed: 2026-10-27
