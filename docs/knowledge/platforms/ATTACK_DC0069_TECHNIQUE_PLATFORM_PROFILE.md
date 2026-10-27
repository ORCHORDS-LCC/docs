# Cloud Service Modification Technique Platform Profile

## Reference

- Technique: **DC0069 — Cloud Service Modification**
- Platforms named in the source: not stated

Cloud service modification refers to changes made to the configuration, settings, or data of a cloud service. These modifications can include administrative changes such as enabling or disabling features, altering permissions, or deleting critical components. Monitoring these changes is critical to detect potential misconfigurations or malicious activity. Examples: - AWS Cloud Service Modifications: A user disables AWS CloudTrail logging (StopLogging) or deletes a CloudWatch configuration rule (DeleteConfigRule). - Azure Cloud Service Modifications: Changes to Azure Role-Based Access Control (RBAC) roles, such as adding a new Contributor role to a sensitive resource. - Google Cloud Service Modifications: Deletion of a Google Cloud Storage bucket or disabling a Google Cloud Function. - Office 365 Cloud Service Modifications: Altering mailbox permissions or disabling auditing in Microsoft 365.

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
- DC0069: https://attack.mitre.org/datacomponents/DC0069
- Reviewed: 2026-10-27
