# Container Start Technique Platform Profile

## Reference

- Technique: **DC0077 — Container Start**
- Platforms named in the source: not stated

"Container Start" data component captures events related to the activation or invocation of a container within a containerized environment. This includes starting a previously stopped container, restarting an existing container, or initializing a container for runtime. Monitoring these activities is critical for identifying unauthorized or unexpected container activations, which may indicate potential adversarial activity or misconfigurations. Examples: - Docker Example: `docker start <container_name>`, `docker restart <container_name>` - Kubernetes Example: Kubernetes automatically restarts containers as part of pod lifecycle management (e.g., due to health checks or configuration changes). - Cloud-Native Example - AWS ECS: API Call: StartTask to activate a stopped ECS task. - Azure Container Instances: Command to restart a container group instance. - GCP Kubernetes Engine: Automatic restarts as part of node or pod management. This data component can be collected through the following measures: - Docker Audit Logging: Enable Docker logging to capture start and restart events. Use tools like auditd to monitor terminal activity involving container lifecycle commands. - Kubernetes Audit Logs: Enable Kubernetes API server audit logging. - Cloud Provider Logs - AWS CloudTrail: Capture StartTask or related API calls for ECS. - Azure Monitor: Track activity in container groups that indicate start or restart events. - GCP Cloud Logging: Record logs related to pod restarts or scaling events in Kubernetes Engine. - SIEM Integration: Collect logs from Docker, Kubernetes, and cloud services to correlate container start events.

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
- DC0077: https://attack.mitre.org/datacomponents/DC0077
- Reviewed: 2026-10-27
