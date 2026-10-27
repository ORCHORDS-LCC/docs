# Container Service Technique Operationalization Review

## Reference

- Technique: **T1543.005 — Container Service**

Adversaries may create or modify container or container cluster management tools that run as daemons, agents, or services on individual hosts. These include software for creating and managing individual containers, such as Docker and Podman, as well as container cluster node-level agents such as kubelet. By modifying these services, an adversary may be able to achieve persistence or escalate their privileges on a host. For example, by using the `docker run` or `podman run` command with the `restart=always` directive, a container can be configured to persistently restart on the host. A user with access to the (rootful) docker command may also be able to escalate their privileges on the host. In Kubernetes environments, DaemonSets allow an adversary to persistently Deploy Containers on all nodes, including ones added later to the cluster. Pods can also be deployed to specific nodes using the `nodeSelector` or `nodeName` fields in the pod spec. Note that containers can also be configured to run as Systemd Services.

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
- T1543.005: https://attack.mitre.org/techniques/T1543/005
- Reviewed: 2026-10-27
