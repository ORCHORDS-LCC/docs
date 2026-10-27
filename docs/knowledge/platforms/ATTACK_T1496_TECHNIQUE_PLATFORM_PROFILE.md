# Resource Hijacking Technique Platform Profile

## Reference

- Technique: **T1496 — Resource Hijacking**
- Platforms named in the source: Windows, IaaS, Linux, macOS, Containers, SaaS

Adversaries may leverage the resources of co-opted systems to complete resource-intensive tasks, which may impact system and/or hosted service availability. Resource hijacking may take a number of different forms. For example, adversaries may: * Leverage compute resources in order to mine cryptocurrency * Sell network bandwidth to proxy networks * Generate SMS traffic for profit * Abuse cloud-based messaging services to send large quantities of spam messages In some cases, adversaries may leverage multiple types of Resource Hijacking at once.

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
- T1496: https://attack.mitre.org/techniques/T1496
- Reviewed: 2026-10-27
