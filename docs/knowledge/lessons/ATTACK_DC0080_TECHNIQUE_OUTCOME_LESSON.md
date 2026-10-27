# DC0080 Instance Start Outcome Lesson

## Authoritative description

- Technique: **DC0080 — Instance Start**

The initiation or activation of a virtual machine instance within a cloud infrastructure. This action typically involves starting an existing instance that had been stopped or paused, allowing it to resume operation. Examples: - Google Cloud Platform (GCP): Starting an instance through `instance.start` API activity. - AWS: Logging of `StartInstances` in AWS CloudTrail for EC2 instances. - Azure: `Microsoft.Compute/virtualMachines/start` entries indicate a VM instance being started.

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
- DC0080: https://attack.mitre.org/datacomponents/DC0080
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
