# Delay Execution Technique Platform Profile

## Reference

- Technique: **T1678 — Delay Execution**
- Platforms named in the source: Linux, macOS, Windows

Adversaries may employ various time-based methods to evade detection and analysis. These techniques often exploit system clocks, delays, or timing mechanisms to obscure malicious activity, blend in with benign activity, and avoid scrutiny. Adversaries can perform this behavior within virtualization/sandbox environments or natively on host systems. Adversaries may utilize programmatic `sleep` commands or native system scheduling functionality, for example Scheduled Task/Job. Benign commands or other operations may also be used to delay malware execution or ensure prior commands have had time to execute properly. Loops or otherwise needless repetitions of commands, such as `ping`, may be used to delay malware execution and potentially exceed time thresholds of automated analysis environments. Another variation, commonly referred to as API hammering, involves making various calls to Native API functions in order to delay execution (while also potentially overloading analysis environments with junk data).

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
- T1678: https://attack.mitre.org/techniques/T1678
- Reviewed: 2026-10-27
