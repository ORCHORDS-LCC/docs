# Container Enumeration Technique Response Playbook

## Target technique

**DC0091 — Container Enumeration**


"Container Enumeration" data component captures events and actions related to listing and identifying active or available containers within a containerized environment. This includes information about running, stopped, or configured containers, such as their names, IDs, statuses, or associated images. Monitoring this activity is crucial for detecting unauthorized discovery or reconnaissance efforts. Examples: - Docker Example: `docker ps`, `docker ps -a` - Kubernetes Example: `kubectl get pods`, `kubectl get deployments` - Cloud Container Services Example - AWS ECS: API Call: ListTasks or ListContainers - Azure Kubernetes Service: API Call: List pod or container instances. - Google Kubernetes Engine (GKE): API Call: Retrieve deployments and their associated containers.

## Preconditions

- the estate in scope is identified, with the systems the technique could apply to;
- an owner is accountable for detection and response;
- current telemetry and configuration can be inspected;
- the technique is applicable or requires an applicability decision.

## Procedure

1. Confirm the scope and owner.
2. Read the current technique description and the associated detection guidance.
3. Inventory the telemetry that would carry the technique's indicators.
4. Inspect whether the indicators are present in the environment.
5. Exercise the detection path and confirm it produces the expected signal.
6. Record gaps in detection coverage and assign remediation owners.
7. Record justified non-applicability or accepted detection gaps separately.
8. Set the next event-driven or periodic verification trigger.

## Failure handling

If the detection path does not produce the expected signal, treat the coverage as unverified, preserve the test evidence, and route the gap through the appropriate remediation or risk process.

## Completion evidence

Scope, owner, source version, telemetry inspected, tests performed, findings, exceptions, remediation links, reviewer, and next trigger.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- DC0091: https://attack.mitre.org/datacomponents/DC0091
- Reviewed: 2026-10-27
