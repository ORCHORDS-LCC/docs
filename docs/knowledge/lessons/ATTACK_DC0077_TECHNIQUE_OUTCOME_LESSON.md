# DC0077 Container Start Outcome Lesson

## Authoritative description

- Technique: **DC0077 — Container Start**

"Container Start" data component captures events related to the activation or invocation of a container within a containerized environment. This includes starting a previously stopped container, restarting an existing container, or initializing a container for runtime. Monitoring these activities is critical for identifying unauthorized or unexpected container activations, which may indicate potential adversarial activity or misconfigurations. Examples: - Docker Example: `docker start <container_name>`, `docker restart <container_name>` - Kubernetes Example: Kubernetes automatically restarts containers as part of pod lifecycle management (e.g., due to health checks or configuration changes). - Cloud-Native Example - AWS ECS: API Call: StartTask to activate a stopped ECS task. - Azure Container Instances: Command to restart a container group instance. - GCP Kubernetes Engine: Automatic restarts as part of node or pod management. This data component can be collected through the following measures: - Docker Audit Logging: Enable Docker logging to capture start and restart events. Use tools like auditd to monitor terminal activity involving container lifecycle commands. - Kubernetes Audit Logs: Enable Kubernetes API server audit logging. - Cloud Provider Logs - AWS CloudTrail: Capture StartTask or related API calls for ECS. - Azure Monitor: Track activity in container groups that indicate start or restart events. - GCP Cloud Logging: Record logs related to pod restarts or scaling events in Kubernetes Engine. - SIEM Integration: Collect logs from Docker, Kubernetes, and cloud services to correlate container start events.

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
- DC0077: https://attack.mitre.org/datacomponents/DC0077
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
