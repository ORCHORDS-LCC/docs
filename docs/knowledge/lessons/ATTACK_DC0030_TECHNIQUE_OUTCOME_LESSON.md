# DC0030 Pod Modification Outcome Lesson

## Authoritative description

- Technique: **DC0030 — Pod Modification**

Changes made to a pod’s configuration or control data within a containerized cluster. This can include updating settings such as resource limits, environment variables, annotations, labels, or even the containers running within the pod. Pod modifications are often executed using commands like kubectl set, kubectl patch, or kubectl edit. *Data Collection Measures:* - Kubernetes API Server Audit Logs: - Capture all API calls related to pod modification, such as PATCH, PUT, or UPDATE methods on v1/pods. - Runtime Security Tools: - Tools like Falco, Sysdig, and Kube-bench can monitor pod modifications at runtime and alert on policy violations. - Container Orchestration Logs: - Monitor events logged by Kubernetes itself (e.g., `kubectl logs -n kube-system kube-controller-manager`). - SIEM and EDR Solutions: - Use SIEM platforms (e.g., Splunk) to aggregate API server logs and detect patterns of unauthorized or suspicious pod modifications. - Endpoint Detection and Response (EDR) tools configured with container visibility can monitor commands like `kubectl` set or `kubectl patch`. - Host-Based Monitoring: - Collect and analyze logs for processes executing `kubectl` commands or interacting with Kubernetes configuration files (e.g., `.kube/config`).

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
- DC0030: https://attack.mitre.org/datacomponents/DC0030
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
