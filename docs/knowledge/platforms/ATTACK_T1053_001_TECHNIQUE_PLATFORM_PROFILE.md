# At (Linux) Technique Platform Profile

## Reference

- Technique: **T1053.001 — At (Linux)**
- Platforms named in the source: Linux

Adversaries may abuse the at utility to perform task scheduling for initial, recurring, or future execution of malicious code. The at command within Linux operating systems enables administrators to schedule tasks. An adversary may use at in Linux environments to execute programs at system startup or on a scheduled basis for persistence. at can also be abused to conduct remote Execution as part of Lateral Movement and or to run a process under the context of a specified account. Adversaries may also abuse at to break out of restricted environments by using a task to spawn an interactive system shell or to run system commands. Similarly, at may also be used for Privilege Escalation if the binary is allowed to run as superuser via <code>sudo</code>.

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
- T1053.001: https://attack.mitre.org/techniques/T1053/001
- Reviewed: 2026-10-27
