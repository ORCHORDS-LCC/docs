# Instance Modification Technique Operationalization Review

## Reference

- Technique: **DC0073 — Instance Modification**

Changes made to a virtual machine (VM) or compute instance, including alterations to its configuration, metadata, attached policies, or operational state. Such modifications can include updating metadata, attaching or detaching resource policies, resizing instances, or modifying network configurations. Examples: - AWS: instance modifications include API actions like `ModifyInstanceAttribute`, `ModifyInstanceMetadataOptions`, or `RebootInstances`. - Azure: modifications can be tracked through operations like `Microsoft.Compute/virtualMachines/write`. - GCP: instance modification events include operations like `instances.setMetadata`, `instances.addResourcePolicies`, or `instances.resize`. *Data Collection Measures:* - AWS CloudTrail: Log Location: Stored in S3 or forwarded to CloudWatch. - Azure Activity Logs: Log Location: Accessible via Azure Monitor or exported to a storage account. - GCP Audit Logs: Log Location: Logs Explorer or BigQuery.

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
- DC0073: https://attack.mitre.org/datacomponents/DC0073
- Reviewed: 2026-10-27
