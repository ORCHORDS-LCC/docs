# Cloud Service Disable Technique Platform Profile

## Reference

- Technique: **DC0090 — Cloud Service Disable**
- Platforms named in the source: not stated

This data component refers to monitoring actions that deactivate or stop a cloud service in a cloud control plane. Examples include disabling essential logging services like AWS CloudTrail (`StopLogging` API call), Microsoft Azure Monitor Logs, or Google Cloud's Operations Suite (formerly Stackdriver). Disabling such services can hinder visibility into adversary activities within the cloud environment. Examples: - AWS CloudTrail StopLogging: This action stops logging of API activity for a particular trail, effectively reducing the monitoring and visibility of AWS resources and activities. - Microsoft Azure Monitor Logs: Disabling these logs hinders the organization’s ability to detect anomalous activities and trace malicious actions. - Google Cloud Logging: Disabling cloud logging removes visibility into resource activity, preventing monitoring of service access or configuration changes. - SaaS Applications: Stopping logging removes visibility into user activities, such as email access or file downloads, enabling undetected malicious behavior.

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
- DC0090: https://attack.mitre.org/datacomponents/DC0090
- Reviewed: 2026-10-27
