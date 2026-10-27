# Instance Start Technique Engineering Review

## Reference

- Technique: **DC0080 — Instance Start**

The initiation or activation of a virtual machine instance within a cloud infrastructure. This action typically involves starting an existing instance that had been stopped or paused, allowing it to resume operation. Examples: - Google Cloud Platform (GCP): Starting an instance through `instance.start` API activity. - AWS: Logging of `StartInstances` in AWS CloudTrail for EC2 instances. - Azure: `Microsoft.Compute/virtualMachines/start` entries indicate a VM instance being started.

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
- DC0080: https://attack.mitre.org/datacomponents/DC0080
- Reviewed: 2026-10-27
