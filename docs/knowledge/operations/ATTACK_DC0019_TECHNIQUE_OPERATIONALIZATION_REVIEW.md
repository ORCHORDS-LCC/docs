# Pod Creation Technique Operationalization Review

## Reference

- Technique: **DC0019 — Pod Creation**

The initial deployment or instantiation of a new pod in a containerized environment. This includes creating a pod manually, through orchestration tools (Kubernetes), or via Infrastructure-as-Code (IaC) configurations. A Pod is the smallest deployable unit in Kubernetes, typically containing one or more containers. Creation methods include: - Direct pod deployment (`kubectl run`, `kubectl apply`) - Automated deployment via CI/CD pipelines (e.g., ArgoCD, Jenkins, GitOps) - Infrastructure-as-Code (IaC) templates (e.g., Terraform, Helm Charts) - API-based deployments via Kubernetes control plane (create_pod API calls) - Pods can be ephemeral (short-lived) or persistent (part of a StatefulSet or Deployment). *Data Collection Measures:* - Kubernetes Audit Logs - Captures all API requests, including pod `create` events. - Kube-api server Logs - Monitors API calls related to pod deployments and modifications. Related Events: `PodSandboxChanged`, `SyncLoop`, `Created pod` - Container Runtime Logs - Logs from CRI-O, containerd, or Docker capture pod creation events. Related Events: `container start`, `container create` - Cloud Provider Logs - GKE, EKS, AKS logs provide insights into Kubernetes API interactions. - SIEM & Log Aggregation - Integrates Kubernetes logs into SIEM solutions. - EDR/XDR Solutions - Monitors container-based activity for anomalous pod creations.

## Operationalization review

1. Record the operational scope: which services, environments, and data the technique could affect.
2. Record the runbook that would be executed, and its owner.
3. Record the telemetry the runbook depends on, and whether it is retained long enough to investigate.
4. Record the detection that would surface the technique before or after it has an effect.
5. Record the recovery path, and the evidence that recovery has been rehearsed.
6. Record the residual operational risk where the runbook depends on a manual step.

## Review evidence

- the runbook and its owner;
- the telemetry retention and coverage record;
- the detection mapping;
- the exercise or rehearsal record.

## Limitations

An operationalization review describes the runbook and the evidence around it. It does not claim the technique has been prevented or detected in a live environment.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- DC0019: https://attack.mitre.org/datacomponents/DC0019
- Reviewed: 2026-10-27
