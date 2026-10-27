# Container CLI/API Technique Response Playbook

## Target technique

**T1059.013 — Container CLI/API**

- Tactics: execution
- Platforms: Containers

Adversaries may abuse built-in CLI tools or API calls to execute malicious commands in containerized environments. The Docker CLI is used for managing containers via an exposed API point from the `dockerd` daemon. Some common examples of Docker CLI include Docker Desktop CLI and Docker Compose, but users are also able to use SDKs to interact with the API. For example, Docker SDK for Python can be used to run commands within a Python application. Adversaries may leverage the Docker CLI, API, or SDK to pull or build Docker images (i.e., Ingress Tool Transfer, Build Image on Host), run containers (i.e., Deploy Container), or execute commands inside running containers (i.e., Container Administration Command). In some cases, threat actors may pull legitimate images that include scripts or tools that they can leverage - for example, using an image that includes the `curl` command to download payloads. Adversaries may also utilize `docker inspect` and `docker ps` to scan for cloud environment variables and other running containers (i.e., Container and Resource Discovery). Kubernetes is responsible for the management and orchestration of containers across clusters. The Kubernetes control plane, which manages the state of the cluster and is responsible for scheduling, communication, and resource monitoring, can be invoked directly via the API or indirectly via CLI tools such as `kubectl`. It may also be accessed within client libraries such as Go or Python. By utilizing the API, administrators can interact with resources within the cluster such as listing or creating pods, which is a group of one or more containers. Adversaries call the API server via `curl` or other tools, allowing them to obtain further information about the environment such as pods, deployments, daemonsets, namespaces, or sysvars. They may also run various commands regarding resource management.

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
- T1059.013: https://attack.mitre.org/techniques/T1059/013
- Reviewed: 2026-10-27
