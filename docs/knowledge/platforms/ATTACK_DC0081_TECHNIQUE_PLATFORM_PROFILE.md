# Instance Deletion Technique Platform Profile

## Reference

- Technique: **DC0081 — Instance Deletion**
- Platforms named in the source: not stated

Removal of a virtual machine (VM) or compute instance within a cloud infrastructure. This activity results in the termination and deletion of the allocated resources (e.g., CPU, memory, storage), making the instance unavailable for future use. Examples: - AWS: instance deletion involves the `TerminateInstances` API call, which is recorded in CloudTrail logs. - Azure: VM deletion can be monitored via Azure Activity Logs, showing the `Microsoft.Compute/virtualMachines/delete` operation. - GCP: instance deletion is logged as an instance.delete operation within GCP Audit Logs.

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
- DC0081: https://attack.mitre.org/datacomponents/DC0081
- Reviewed: 2026-10-27
