# Instance Stop Technique Response Playbook

## Target technique

**DC0089 — Instance Stop**


The deactivation or shutdown of a virtual machine instance within a cloud infrastructure. This action typically involves stopping a running instance, which halts its operation and releases certain associated resources, such as CPU and memory. Examples: - Google Cloud Platform (GCP): `instance.stop` events recorded in GCP Audit Logs indicate the deactivation of an instance. - Amazon Web Services (AWS): `StopInstances` actions in AWS CloudTrail indicate EC2 instances being stopped. - Microsoft Azure: `Microsoft.Compute/virtualMachines/deallocate` or `stop` events in Azure Activity Logs represent a virtual machine being stopped or deallocated.

## Preconditions

- the estate in scope is identified, with the systems the technique could apply to;
- an owner is accountable for detection and response;
- current telemetry and configuration can be inspected;
- the technique is applicable or requires an applicability decision.

## Procedure

1. Confirm the scope and owner.
2. Read the current technique description and the associated detection guidance.
3. Inventory the telemetry that would carry the technique's indicators.
4. Inspect whether the indicators are present in the environment.
5. Exercise the detection path and confirm it produces the expected signal.
6. Record gaps in detection coverage and assign remediation owners.
7. Record justified non-applicability or accepted detection gaps separately.
8. Set the next event-driven or periodic verification trigger.

## Failure handling

If the detection path does not produce the expected signal, treat the coverage as unverified, preserve the test evidence, and route the gap through the appropriate remediation or risk process.

## Completion evidence

Scope, owner, source version, telemetry inspected, tests performed, findings, exceptions, remediation links, reviewer, and next trigger.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- DC0089: https://attack.mitre.org/datacomponents/DC0089
- Reviewed: 2026-10-27
