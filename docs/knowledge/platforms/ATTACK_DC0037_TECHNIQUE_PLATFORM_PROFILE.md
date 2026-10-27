# Pod Enumeration Technique Platform Profile

## Reference

- Technique: **DC0037 — Pod Enumeration**
- Platforms named in the source: not stated

Extracting a list of running or existing pods within a containerized cluster environment. Pods are the smallest deployable units in a Kubernetes cluster and typically represent an application or workload. Enumeration of pods provides insight into the structure and state of applications running in the cluster, such as the names of pods, their namespaces, and their associated metadata. *Data Collection Measures:* - Kubernetes API Server Audit Logs: - Enable Audit Logging in Kubernetes to capture API requests, such as GET `/api/v1/pods`. - Container Runtime Logs: - Collect runtime-level logs from tools like CRI-O, containerd, or Docker, which might show relevant API calls for pod enumeration. - EDR and SIEM: - Endpoint Detection and Response (EDR) tools, if configured with cluster-level visibility, can monitor user commands like `kubectl get pods`. - SIEM platforms (e.g., Splunk) can ingest Kubernetes API logs to detect enumeration patterns. - Host-Based Monitoring: - Monitor processes and commands executed on nodes where `kubectl` is installed using tools like auditd, Sysmon for Linux, or kernel modules.

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
- DC0037: https://attack.mitre.org/datacomponents/DC0037
- Reviewed: 2026-10-27
