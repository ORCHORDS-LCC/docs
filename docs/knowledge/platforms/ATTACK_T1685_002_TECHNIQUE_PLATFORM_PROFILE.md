# Disable or Modify Cloud Log Technique Platform Profile

## Reference

- Technique: **T1685.002 — Disable or Modify Cloud Log**
- Platforms named in the source: IaaS, SaaS, Identity Provider, Office Suite

An adversary may disable or modify cloud logging capabilities and integrations to limit what data is collected on their activities and avoid detection. Cloud environments allow for collection and analysis of audit and application logs that provide insight into what activities a user does within the environment. If an adversary has sufficient permissions, they can disable or modify logging to avoid detection of their activities. For example, in AWS an adversary may disable CloudWatch/CloudTrail integrations prior to conducting further malicious activity. They may alternatively tamper with logging functionality, for example, by removing any associated SNS topics, disabling multi-region logging, or disabling settings that validate and/or encrypt log files. In Office 365, an adversary may disable logging on mail collection activities for specific users by using the Set-MailboxAuditBypassAssociation cmdlet, by disabling M365 Advanced Auditing for the user, or by downgrading the user’s license from an Enterprise E5 to an Enterprise E3 license.

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
- T1685.002: https://attack.mitre.org/techniques/T1685/002
- Reviewed: 2026-10-27
