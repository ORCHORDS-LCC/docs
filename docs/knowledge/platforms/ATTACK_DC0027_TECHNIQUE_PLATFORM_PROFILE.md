# Cloud Storage Metadata Technique Platform Profile

## Reference

- Technique: **DC0027 — Cloud Storage Metadata**
- Platforms named in the source: not stated

Cloud Storage Metadata provides contextual information about cloud storage infrastructure and its associated activity. This data may include attributes such as storage name, size, owner, permissions, creation date, region, and activity metadata. It is essential for monitoring, auditing, and identifying anomalies in cloud storage environments. Examples: - AWS S3 Bucket Metadata: Metadata about an S3 bucket includes the bucket name, region, creation date, owner, storage class, and permissions. - Azure Blob Storage Metadata: Metadata for an Azure Blob container includes container name, access level (e.g., private or public), size, and tags. - Google Cloud Storage Metadata: Metadata includes bucket name, storage class, location, labels, lifecycle policies, and versioning status. - OpenStack Swift Metadata: Metadata for a Swift container includes name, access level, quota, and custom attributes.

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
- DC0027: https://attack.mitre.org/datacomponents/DC0027
- Reviewed: 2026-10-27
