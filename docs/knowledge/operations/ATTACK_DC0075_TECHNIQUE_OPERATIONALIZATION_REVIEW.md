# Instance Enumeration Technique Operationalization Review

## Reference

- Technique: **DC0075 — Instance Enumeration**

The process of retrieving or querying a list of virtual machine instances or compute instances within a cloud infrastructure. This activity provides a view of all available or running instances, typically including their associated metadata such as instance ID, name, state, and configuration details. Examples: - AWS: instance enumeration involves the `DescribeInstances` API call, which retrieves information about running or stopped EC2 instances. - Azure: VM enumeration can be monitored via the `Microsoft.Compute/virtualMachines/read` operation. - GCP: instance enumeration is logged as an `instance.list` operation within GCP Audit Logs. *Data Collection Measures:* - AWS CloudTrail: CloudTrail logs stored in S3 or forwarded to CloudWatch. - Azure Activity Logs: Accessible via Azure Monitor or exported to a storage account. - GCP Audit Logs: Logs Explorer or BigQuery.

## Operationalization review

1. Record the operational scope: which services, environments, and data the technique could affect.
2. Record the runbook that would be executed, and its owner.
3. Record the telemetry the runbook depends on, and whether it is retained long enough to investigate.
4. Record the detection that would surface the technique before or after it has an effect.
5. Record the recovery path, and the evidence that recovery has been rehearsed.
6. Record the residual operational risk where the runbook depends on a manual step.

## Review evidence

- the runbook and its owner;
- the telemetry retention and coverage record;
- the detection mapping;
- the exercise or rehearsal record.

## Limitations

An operationalization review describes the runbook and the evidence around it. It does not claim the technique has been prevented or detected in a live environment.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- DC0075: https://attack.mitre.org/datacomponents/DC0075
- Reviewed: 2026-10-27
