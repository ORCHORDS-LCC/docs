# Pod Modification Technique Platform Profile

## Reference

- Technique: **DC0030 — Pod Modification**
- Platforms named in the source: not stated

Changes made to a pod’s configuration or control data within a containerized cluster. This can include updating settings such as resource limits, environment variables, annotations, labels, or even the containers running within the pod. Pod modifications are often executed using commands like kubectl set, kubectl patch, or kubectl edit. *Data Collection Measures:* - Kubernetes API Server Audit Logs: - Capture all API calls related to pod modification, such as PATCH, PUT, or UPDATE methods on v1/pods. - Runtime Security Tools: - Tools like Falco, Sysdig, and Kube-bench can monitor pod modifications at runtime and alert on policy violations. - Container Orchestration Logs: - Monitor events logged by Kubernetes itself (e.g., `kubectl logs -n kube-system kube-controller-manager`). - SIEM and EDR Solutions: - Use SIEM platforms (e.g., Splunk) to aggregate API server logs and detect patterns of unauthorized or suspicious pod modifications. - Endpoint Detection and Response (EDR) tools configured with container visibility can monitor commands like `kubectl` set or `kubectl patch`. - Host-Based Monitoring: - Collect and analyze logs for processes executing `kubectl` commands or interacting with Kubernetes configuration files (e.g., `.kube/config`).

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
- DC0030: https://attack.mitre.org/datacomponents/DC0030
- Reviewed: 2026-10-27
