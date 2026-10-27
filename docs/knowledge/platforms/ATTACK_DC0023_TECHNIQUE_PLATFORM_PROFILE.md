# Cloud Storage Modification Technique Platform Profile

## Reference

- Technique: **DC0023 — Cloud Storage Modification**
- Platforms named in the source: not stated

Cloud Storage Modification involves tracking changes made to cloud storage infrastructure, including updates to settings, permissions, or stored data. Examples include modifying object access control lists (ACLs), uploading new objects, or updating bucket policies. Examples: AWS S3: An object is uploaded or its ACL is modified. - Azure Blob Storage: A blob's metadata or permissions are updated. - Google Cloud Storage: An object's lifecycle policy is updated, or a bucket policy is changed. - OpenStack Swift: Modifications to container settings or uploading of new objects.

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
- DC0023: https://attack.mitre.org/datacomponents/DC0023
- Reviewed: 2026-10-27
