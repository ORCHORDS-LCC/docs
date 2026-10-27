# Instance Modification Technique Platform Profile

## Reference

- Technique: **DC0073 — Instance Modification**
- Platforms named in the source: not stated

Changes made to a virtual machine (VM) or compute instance, including alterations to its configuration, metadata, attached policies, or operational state. Such modifications can include updating metadata, attaching or detaching resource policies, resizing instances, or modifying network configurations. Examples: - AWS: instance modifications include API actions like `ModifyInstanceAttribute`, `ModifyInstanceMetadataOptions`, or `RebootInstances`. - Azure: modifications can be tracked through operations like `Microsoft.Compute/virtualMachines/write`. - GCP: instance modification events include operations like `instances.setMetadata`, `instances.addResourcePolicies`, or `instances.resize`. *Data Collection Measures:* - AWS CloudTrail: Log Location: Stored in S3 or forwarded to CloudWatch. - Azure Activity Logs: Log Location: Accessible via Azure Monitor or exported to a storage account. - GCP Audit Logs: Log Location: Logs Explorer or BigQuery.

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
- DC0073: https://attack.mitre.org/datacomponents/DC0073
- Reviewed: 2026-10-27
