# Pod Creation Technique Response Playbook

## Target technique

**DC0019 — Pod Creation**


The initial deployment or instantiation of a new pod in a containerized environment. This includes creating a pod manually, through orchestration tools (Kubernetes), or via Infrastructure-as-Code (IaC) configurations. A Pod is the smallest deployable unit in Kubernetes, typically containing one or more containers. Creation methods include: - Direct pod deployment (`kubectl run`, `kubectl apply`) - Automated deployment via CI/CD pipelines (e.g., ArgoCD, Jenkins, GitOps) - Infrastructure-as-Code (IaC) templates (e.g., Terraform, Helm Charts) - API-based deployments via Kubernetes control plane (create_pod API calls) - Pods can be ephemeral (short-lived) or persistent (part of a StatefulSet or Deployment). *Data Collection Measures:* - Kubernetes Audit Logs - Captures all API requests, including pod `create` events. - Kube-api server Logs - Monitors API calls related to pod deployments and modifications. Related Events: `PodSandboxChanged`, `SyncLoop`, `Created pod` - Container Runtime Logs - Logs from CRI-O, containerd, or Docker capture pod creation events. Related Events: `container start`, `container create` - Cloud Provider Logs - GKE, EKS, AKS logs provide insights into Kubernetes API interactions. - SIEM & Log Aggregation - Integrates Kubernetes logs into SIEM solutions. - EDR/XDR Solutions - Monitors container-based activity for anomalous pod creations.

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
- DC0019: https://attack.mitre.org/datacomponents/DC0019
- Reviewed: 2026-10-27
