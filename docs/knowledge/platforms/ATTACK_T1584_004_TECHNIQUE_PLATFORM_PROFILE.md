# Server Technique Platform Profile

## Reference

- Technique: **T1584.004 — Server**
- Platforms named in the source: PRE

Adversaries may compromise third-party servers that can be used during targeting. Use of servers allows an adversary to stage, launch, and execute an operation. During post-compromise activity, adversaries may utilize servers for various tasks, including for Command and Control. Instead of purchasing a Server or Virtual Private Server, adversaries may compromise third-party servers in support of operations. Adversaries may also compromise web servers to support watering hole operations, as in Drive-by Compromise, or email servers to support Phishing operations.

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
- T1584.004: https://attack.mitre.org/techniques/T1584/004
- Reviewed: 2026-10-27
