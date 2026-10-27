# DC0075 Instance Enumeration Outcome Lesson

## Authoritative description

- Technique: **DC0075 — Instance Enumeration**

The process of retrieving or querying a list of virtual machine instances or compute instances within a cloud infrastructure. This activity provides a view of all available or running instances, typically including their associated metadata such as instance ID, name, state, and configuration details. Examples: - AWS: instance enumeration involves the `DescribeInstances` API call, which retrieves information about running or stopped EC2 instances. - Azure: VM enumeration can be monitored via the `Microsoft.Compute/virtualMachines/read` operation. - GCP: instance enumeration is logged as an `instance.list` operation within GCP Audit Logs. *Data Collection Measures:* - AWS CloudTrail: CloudTrail logs stored in S3 or forwarded to CloudWatch. - Azure Activity Logs: Accessible via Azure Monitor or exported to a storage account. - GCP Audit Logs: Logs Explorer or BigQuery.

## Reusable lesson

This technique should be treated as an explicit review question when it is relevant to the system or organisation, rather than assumed to be covered by a generic control statement or by tooling that reports a related signal.

## Apply the lesson

1. Define the real scope before judging coverage.
2. Inspect current technical, process, governance, or operational evidence.
3. Separate documented intent from verified behaviour.
4. Record partial coverage and unresolved gaps instead of converting them into a pass.
5. Revisit when the underlying scope, threat environment, technology, suppliers, or mission materially changes.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- DC0075: https://attack.mitre.org/datacomponents/DC0075
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
