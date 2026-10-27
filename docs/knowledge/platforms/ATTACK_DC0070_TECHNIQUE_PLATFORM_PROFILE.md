# Cloud Service Metadata Technique Platform Profile

## Reference

- Technique: **DC0070 — Cloud Service Metadata**
- Platforms named in the source: not stated

Cloud service metadata refers to the contextual and descriptive information about cloud services, including their name, type, purpose, configuration, and activity around them. This metadata is essential for understanding the roles and functions of cloud services, their operational status, and their potential misuse. Examples: - Azure Service Metadata: Metadata describing a resource in Azure, such as an Azure Storage Account or a Virtual Machine. - AWS Cloud Service Metadata: Metadata for an AWS EC2 instance collected using the `DescribeInstances` API call. - Google Cloud Service Metadata: Metadata for a Google Compute Engine instance collected using `gcloud compute instances describe`. - Office 365 Metadata: Metadata about an Office 365 SharePoint site.

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
- DC0070: https://attack.mitre.org/datacomponents/DC0070
- Reviewed: 2026-10-27
