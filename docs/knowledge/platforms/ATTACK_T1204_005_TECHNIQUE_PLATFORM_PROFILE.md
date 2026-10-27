# Malicious Library Technique Platform Profile

## Reference

- Technique: **T1204.005 — Malicious Library**
- Platforms named in the source: Linux, macOS, Windows

Adversaries may rely on a user installing a malicious library to facilitate execution. Threat actors may Upload Malware to package managers such as NPM and PyPi, as well as to public code repositories such as GitHub. User may install libraries without realizing they are malicious, thus bypassing techniques that specifically achieve Initial Access. This can lead to the execution of malicious code, such as code that establishes persistence, steals data, or mines cryptocurrency. In some cases, threat actors may compromise and backdoor existing popular libraries (i.e., Compromise Software Dependencies and Development Tools). Alternatively, they may create entirely new packages and leverage behaviors such as typosquatting to encourage users to install them.

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
- T1204.005: https://attack.mitre.org/techniques/T1204/005
- Reviewed: 2026-10-27
