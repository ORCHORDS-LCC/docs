# Instance Enumeration Technique Platform Profile

## Reference

- Technique: **DC0075 — Instance Enumeration**
- Platforms named in the source: not stated

The process of retrieving or querying a list of virtual machine instances or compute instances within a cloud infrastructure. This activity provides a view of all available or running instances, typically including their associated metadata such as instance ID, name, state, and configuration details. Examples: - AWS: instance enumeration involves the `DescribeInstances` API call, which retrieves information about running or stopped EC2 instances. - Azure: VM enumeration can be monitored via the `Microsoft.Compute/virtualMachines/read` operation. - GCP: instance enumeration is logged as an `instance.list` operation within GCP Audit Logs. *Data Collection Measures:* - AWS CloudTrail: CloudTrail logs stored in S3 or forwarded to CloudWatch. - Azure Activity Logs: Accessible via Azure Monitor or exported to a storage account. - GCP Audit Logs: Logs Explorer or BigQuery.

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
- DC0075: https://attack.mitre.org/datacomponents/DC0075
- Reviewed: 2026-10-27
