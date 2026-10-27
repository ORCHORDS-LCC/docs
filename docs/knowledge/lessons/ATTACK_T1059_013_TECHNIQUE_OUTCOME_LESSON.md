# T1059.013 Container CLI/API Outcome Lesson

## Authoritative description

- Technique: **T1059.013 — Container CLI/API**
- Tactics: execution
- Platforms: Containers

Adversaries may abuse built-in CLI tools or API calls to execute malicious commands in containerized environments. The Docker CLI is used for managing containers via an exposed API point from the `dockerd` daemon. Some common examples of Docker CLI include Docker Desktop CLI and Docker Compose, but users are also able to use SDKs to interact with the API. For example, Docker SDK for Python can be used to run commands within a Python application. Adversaries may leverage the Docker CLI, API, or SDK to pull or build Docker images (i.e., Ingress Tool Transfer, Build Image on Host), run containers (i.e., Deploy Container), or execute commands inside running containers (i.e., Container Administration Command). In some cases, threat actors may pull legitimate images that include scripts or tools that they can leverage - for example, using an image that includes the `curl` command to download payloads. Adversaries may also utilize `docker inspect` and `docker ps` to scan for cloud environment variables and other running containers (i.e., Container and Resource Discovery). Kubernetes is responsible for the management and orchestration of containers across clusters. The Kubernetes control plane, which manages the state of the cluster and is responsible for scheduling, communication, and resource monitoring, can be invoked directly via the API or indirectly via CLI tools such as `kubectl`. It may also be accessed within client libraries such as Go or Python. By utilizing the API, administrators can interact with resources within the cluster such as listing or creating pods, which is a group of one or more containers. Adversaries call the API server via `curl` or other tools, allowing them to obtain further information about the environment such as pods, deployments, daemonsets, namespaces, or sysvars. They may also run various commands regarding resource management.

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
- T1059.013: https://attack.mitre.org/techniques/T1059/013
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
