# Snapshot Deletion Technique Engineering Review

## Reference

- Technique: **DC0049 — Snapshot Deletion**

The removal of a point-in-time backup of a cloud storage volume, virtual machine (VM), or database. *Data Collection Measures:* - AWS CloudTrail - Logs `DeleteSnapshot` API calls in EC2, RDS, and EBS services. - Azure Monitor Logs - Tracks snapshot deletions via `Microsoft.Compute/snapshots/delete` API calls. - Google Cloud Logging - Detects snapshot removal through `compute.disks.deleteSnapshot` events.

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
- DC0049: https://attack.mitre.org/datacomponents/DC0049
- Reviewed: 2026-10-27
