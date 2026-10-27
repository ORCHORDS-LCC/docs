# Pod Creation Technique Engineering Review

## Reference

- Technique: **DC0019 — Pod Creation**

The initial deployment or instantiation of a new pod in a containerized environment. This includes creating a pod manually, through orchestration tools (Kubernetes), or via Infrastructure-as-Code (IaC) configurations. A Pod is the smallest deployable unit in Kubernetes, typically containing one or more containers. Creation methods include: - Direct pod deployment (`kubectl run`, `kubectl apply`) - Automated deployment via CI/CD pipelines (e.g., ArgoCD, Jenkins, GitOps) - Infrastructure-as-Code (IaC) templates (e.g., Terraform, Helm Charts) - API-based deployments via Kubernetes control plane (create_pod API calls) - Pods can be ephemeral (short-lived) or persistent (part of a StatefulSet or Deployment). *Data Collection Measures:* - Kubernetes Audit Logs - Captures all API requests, including pod `create` events. - Kube-api server Logs - Monitors API calls related to pod deployments and modifications. Related Events: `PodSandboxChanged`, `SyncLoop`, `Created pod` - Container Runtime Logs - Logs from CRI-O, containerd, or Docker capture pod creation events. Related Events: `container start`, `container create` - Cloud Provider Logs - GKE, EKS, AKS logs provide insights into Kubernetes API interactions. - SIEM & Log Aggregation - Integrates Kubernetes logs into SIEM solutions. - EDR/XDR Solutions - Monitors container-based activity for anomalous pod creations.

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
- DC0019: https://attack.mitre.org/datacomponents/DC0019
- Reviewed: 2026-10-27
