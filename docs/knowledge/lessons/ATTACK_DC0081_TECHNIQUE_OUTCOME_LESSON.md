# DC0081 Instance Deletion Outcome Lesson

## Authoritative description

- Technique: **DC0081 — Instance Deletion**

Removal of a virtual machine (VM) or compute instance within a cloud infrastructure. This activity results in the termination and deletion of the allocated resources (e.g., CPU, memory, storage), making the instance unavailable for future use. Examples: - AWS: instance deletion involves the `TerminateInstances` API call, which is recorded in CloudTrail logs. - Azure: VM deletion can be monitored via Azure Activity Logs, showing the `Microsoft.Compute/virtualMachines/delete` operation. - GCP: instance deletion is logged as an instance.delete operation within GCP Audit Logs.

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
- DC0081: https://attack.mitre.org/datacomponents/DC0081
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
