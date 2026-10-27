# Pod Modification Technique Response Playbook

## Target technique

**DC0030 — Pod Modification**


Changes made to a pod’s configuration or control data within a containerized cluster. This can include updating settings such as resource limits, environment variables, annotations, labels, or even the containers running within the pod. Pod modifications are often executed using commands like kubectl set, kubectl patch, or kubectl edit. *Data Collection Measures:* - Kubernetes API Server Audit Logs: - Capture all API calls related to pod modification, such as PATCH, PUT, or UPDATE methods on v1/pods. - Runtime Security Tools: - Tools like Falco, Sysdig, and Kube-bench can monitor pod modifications at runtime and alert on policy violations. - Container Orchestration Logs: - Monitor events logged by Kubernetes itself (e.g., `kubectl logs -n kube-system kube-controller-manager`). - SIEM and EDR Solutions: - Use SIEM platforms (e.g., Splunk) to aggregate API server logs and detect patterns of unauthorized or suspicious pod modifications. - Endpoint Detection and Response (EDR) tools configured with container visibility can monitor commands like `kubectl` set or `kubectl patch`. - Host-Based Monitoring: - Collect and analyze logs for processes executing `kubectl` commands or interacting with Kubernetes configuration files (e.g., `.kube/config`).

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
- DC0030: https://attack.mitre.org/datacomponents/DC0030
- Reviewed: 2026-10-27
