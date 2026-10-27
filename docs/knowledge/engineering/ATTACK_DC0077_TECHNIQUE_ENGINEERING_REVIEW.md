# Container Start Technique Engineering Review

## Reference

- Technique: **DC0077 — Container Start**

"Container Start" data component captures events related to the activation or invocation of a container within a containerized environment. This includes starting a previously stopped container, restarting an existing container, or initializing a container for runtime. Monitoring these activities is critical for identifying unauthorized or unexpected container activations, which may indicate potential adversarial activity or misconfigurations. Examples: - Docker Example: `docker start <container_name>`, `docker restart <container_name>` - Kubernetes Example: Kubernetes automatically restarts containers as part of pod lifecycle management (e.g., due to health checks or configuration changes). - Cloud-Native Example - AWS ECS: API Call: StartTask to activate a stopped ECS task. - Azure Container Instances: Command to restart a container group instance. - GCP Kubernetes Engine: Automatic restarts as part of node or pod management. This data component can be collected through the following measures: - Docker Audit Logging: Enable Docker logging to capture start and restart events. Use tools like auditd to monitor terminal activity involving container lifecycle commands. - Kubernetes Audit Logs: Enable Kubernetes API server audit logging. - Cloud Provider Logs - AWS CloudTrail: Capture StartTask or related API calls for ECS. - Azure Monitor: Track activity in container groups that indicate start or restart events. - GCP Cloud Logging: Record logs related to pod restarts or scaling events in Kubernetes Engine. - SIEM Integration: Collect logs from Docker, Kubernetes, and cloud services to correlate container start events.

## Engineering review

1. Identify the engineering boundary where the technique would apply: the component, the service, or the deployment.
2. Review the design decision that would prevent the technique, and record the alternative considered.
3. Review the implementation evidence for the preventive control.
4. Review the test coverage that would fail if the control regressed.
5. Review the observability: which signal would show the control is not operating.
6. Record the residual risk where prevention is not achievable, and the detection that compensates.

## Review evidence

- the design record for the preventive decision;
- the implementation or configuration evidence;
- the test record showing the control is exercised;
- the observability mapping.

## Limitations

An engineering review describes what the design and the implementation evidence show. It does not claim the technique has been addressed in production.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- DC0077: https://attack.mitre.org/datacomponents/DC0077
- Reviewed: 2026-10-27
