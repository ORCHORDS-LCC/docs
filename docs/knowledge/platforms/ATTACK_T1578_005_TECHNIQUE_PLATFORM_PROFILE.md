# Modify Cloud Compute Configurations Technique Platform Profile

## Reference

- Technique: **T1578.005 — Modify Cloud Compute Configurations**
- Platforms named in the source: IaaS

Adversaries may modify settings that directly affect the size, locations, and resources available to cloud compute infrastructure in order to evade defenses. These settings may include service quotas, subscription associations, tenant-wide policies, or other configurations that impact available compute. Such modifications may allow adversaries to abuse the victim’s compute resources to achieve their goals, potentially without affecting the execution of running instances and/or revealing their activities to the victim. For example, cloud providers often limit customer usage of compute resources via quotas. Customers may request adjustments to these quotas to support increased computing needs, though these adjustments may require approval from the cloud provider. Adversaries who compromise a cloud environment may similarly request quota adjustments in order to support their activities, such as enabling additional Resource Hijacking without raising suspicion by using up a victim’s entire quota. Adversaries may also increase allowed resource usage by modifying any tenant-wide policies that limit the sizes of deployed virtual machines. Adversaries may also modify settings that affect where cloud resources can be deployed, such as enabling Unused/Unsupported Cloud Regions.

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
- T1578.005: https://attack.mitre.org/techniques/T1578/005
- Reviewed: 2026-10-27
