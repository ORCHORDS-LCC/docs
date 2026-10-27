# DC0073 Instance Modification Outcome Lesson

## Authoritative description

- Technique: **DC0073 — Instance Modification**

Changes made to a virtual machine (VM) or compute instance, including alterations to its configuration, metadata, attached policies, or operational state. Such modifications can include updating metadata, attaching or detaching resource policies, resizing instances, or modifying network configurations. Examples: - AWS: instance modifications include API actions like `ModifyInstanceAttribute`, `ModifyInstanceMetadataOptions`, or `RebootInstances`. - Azure: modifications can be tracked through operations like `Microsoft.Compute/virtualMachines/write`. - GCP: instance modification events include operations like `instances.setMetadata`, `instances.addResourcePolicies`, or `instances.resize`. *Data Collection Measures:* - AWS CloudTrail: Log Location: Stored in S3 or forwarded to CloudWatch. - Azure Activity Logs: Log Location: Accessible via Azure Monitor or exported to a storage account. - GCP Audit Logs: Log Location: Logs Explorer or BigQuery.

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
- DC0073: https://attack.mitre.org/datacomponents/DC0073
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
