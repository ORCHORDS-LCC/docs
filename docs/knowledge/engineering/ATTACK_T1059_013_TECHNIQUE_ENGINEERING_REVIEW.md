# Container CLI/API Technique Engineering Review

## Reference

- Technique: **T1059.013 — Container CLI/API**

Adversaries may abuse built-in CLI tools or API calls to execute malicious commands in containerized environments. The Docker CLI is used for managing containers via an exposed API point from the `dockerd` daemon. Some common examples of Docker CLI include Docker Desktop CLI and Docker Compose, but users are also able to use SDKs to interact with the API. For example, Docker SDK for Python can be used to run commands within a Python application. Adversaries may leverage the Docker CLI, API, or SDK to pull or build Docker images (i.e., Ingress Tool Transfer, Build Image on Host), run containers (i.e., Deploy Container), or execute commands inside running containers (i.e., Container Administration Command). In some cases, threat actors may pull legitimate images that include scripts or tools that they can leverage - for example, using an image that includes the `curl` command to download payloads. Adversaries may also utilize `docker inspect` and `docker ps` to scan for cloud environment variables and other running containers (i.e., Container and Resource Discovery). Kubernetes is responsible for the management and orchestration of containers across clusters. The Kubernetes control plane, which manages the state of the cluster and is responsible for scheduling, communication, and resource monitoring, can be invoked directly via the API or indirectly via CLI tools such as `kubectl`. It may also be accessed within client libraries such as Go or Python. By utilizing the API, administrators can interact with resources within the cluster such as listing or creating pods, which is a group of one or more containers. Adversaries call the API server via `curl` or other tools, allowing them to obtain further information about the environment such as pods, deployments, daemonsets, namespaces, or sysvars. They may also run various commands regarding resource management.

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
- T1059.013: https://attack.mitre.org/techniques/T1059/013
- Reviewed: 2026-10-27
