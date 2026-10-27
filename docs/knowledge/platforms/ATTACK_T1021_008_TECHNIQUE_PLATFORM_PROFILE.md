# Direct Cloud VM Connections Technique Platform Profile

## Reference

- Technique: **T1021.008 — Direct Cloud VM Connections**
- Platforms named in the source: IaaS

Adversaries may leverage Valid Accounts to log directly into accessible cloud hosted compute infrastructure through cloud native methods. Many cloud providers offer interactive connections to virtual infrastructure that can be accessed through the Cloud API, such as Azure Serial Console, AWS EC2 Instance Connect, and AWS System Manager.. Methods of authentication for these connections can include passwords, application access tokens, or SSH keys. These cloud native methods may, by default, allow for privileged access on the host with SYSTEM or root level access. Adversaries may utilize these cloud native methods to directly access virtual infrastructure and pivot through an environment. These connections typically provide direct console access to the VM rather than the execution of scripts (i.e., Cloud Administration Command).

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
- T1021.008: https://attack.mitre.org/techniques/T1021/008
- Reviewed: 2026-10-27
