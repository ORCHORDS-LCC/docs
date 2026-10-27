# Cloud Accounts Technique Platform Profile

## Reference

- Technique: **T1585.003 — Cloud Accounts**
- Platforms named in the source: PRE

Adversaries may create accounts with cloud providers that can be used during targeting. Adversaries can use cloud accounts to further their operations, including leveraging cloud storage services such as Dropbox, MEGA, Microsoft OneDrive, or AWS S3 buckets for Exfiltration to Cloud Storage or to Upload Tools. Cloud accounts can also be used in the acquisition of infrastructure, such as Virtual Private Servers or Serverless infrastructure. Establishing cloud accounts may allow adversaries to develop sophisticated capabilities without managing their own servers. Creating Cloud Accounts may also require adversaries to establish Email Accounts to register with the cloud provider.

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
- T1585.003: https://attack.mitre.org/techniques/T1585/003
- Reviewed: 2026-10-27
