# DC0091 Container Enumeration Outcome Lesson

## Authoritative description

- Technique: **DC0091 — Container Enumeration**

"Container Enumeration" data component captures events and actions related to listing and identifying active or available containers within a containerized environment. This includes information about running, stopped, or configured containers, such as their names, IDs, statuses, or associated images. Monitoring this activity is crucial for detecting unauthorized discovery or reconnaissance efforts. Examples: - Docker Example: `docker ps`, `docker ps -a` - Kubernetes Example: `kubectl get pods`, `kubectl get deployments` - Cloud Container Services Example - AWS ECS: API Call: ListTasks or ListContainers - Azure Kubernetes Service: API Call: List pod or container instances. - Google Kubernetes Engine (GKE): API Call: Retrieve deployments and their associated containers.

## Reusable lesson

This technique should be treated as an explicit review question when it is relevant to the system or organisation, rather than assumed to be covered by a generic control statement or by tooling that reports a related signal.

## Apply the lesson

1. Define the real scope before judging coverage.
2. Inspect current technical, process, governance, or operational evidence.
3. Separate documented intent from verified behaviour.
4. Record partial coverage and unresolved gaps instead of converting them into a pass.
5. Revisit when the underlying scope, threat environment, technology, suppliers, or mission materially changes.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- DC0091: https://attack.mitre.org/datacomponents/DC0091
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
