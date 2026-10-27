# Instance Stop Technique Platform Profile

## Reference

- Technique: **DC0089 — Instance Stop**
- Platforms named in the source: not stated

The deactivation or shutdown of a virtual machine instance within a cloud infrastructure. This action typically involves stopping a running instance, which halts its operation and releases certain associated resources, such as CPU and memory. Examples: - Google Cloud Platform (GCP): `instance.stop` events recorded in GCP Audit Logs indicate the deactivation of an instance. - Amazon Web Services (AWS): `StopInstances` actions in AWS CloudTrail indicate EC2 instances being stopped. - Microsoft Azure: `Microsoft.Compute/virtualMachines/deallocate` or `stop` events in Azure Activity Logs represent a virtual machine being stopped or deallocated.

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
- DC0089: https://attack.mitre.org/datacomponents/DC0089
- Reviewed: 2026-10-27
