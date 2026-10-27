# Instance Enumeration Technique Engineering Review

## Reference

- Technique: **DC0075 — Instance Enumeration**

The process of retrieving or querying a list of virtual machine instances or compute instances within a cloud infrastructure. This activity provides a view of all available or running instances, typically including their associated metadata such as instance ID, name, state, and configuration details. Examples: - AWS: instance enumeration involves the `DescribeInstances` API call, which retrieves information about running or stopped EC2 instances. - Azure: VM enumeration can be monitored via the `Microsoft.Compute/virtualMachines/read` operation. - GCP: instance enumeration is logged as an `instance.list` operation within GCP Audit Logs. *Data Collection Measures:* - AWS CloudTrail: CloudTrail logs stored in S3 or forwarded to CloudWatch. - Azure Activity Logs: Accessible via Azure Monitor or exported to a storage account. - GCP Audit Logs: Logs Explorer or BigQuery.

## Engineering review

1. Identify the engineering boundary where the technique would apply: the component, the service, or the deployment.
2. Review the design decision that would prevent the technique, and record the alternative considered.
3. Review the implementation evidence for the preventive control.
4. Review the test coverage that would fail if the control regressed.
5. Review the observability: which signal would show the control is not operating.
6. Record the residual risk where prevention is not achievable, and the detection that compensates.

## Review evidence

- the design record for the preventive decision;
- the implementation or configuration evidence;
- the test record showing the control is exercised;
- the observability mapping.

## Limitations

An engineering review describes what the design and the implementation evidence show. It does not claim the technique has been addressed in production.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- DC0075: https://attack.mitre.org/datacomponents/DC0075
- Reviewed: 2026-10-27
