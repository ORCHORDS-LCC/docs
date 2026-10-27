# Snapshot Modification Technique Engineering Review

## Reference

- Technique: **DC0058 — Snapshot Modification**

Changes made to a cloud snapshot's metadata, attributes, or control settings. These modifications may involve adjusting access permissions, changing retention policies, or altering encryption settings. *Data Collection Measures:* - AWS CloudTrail - Tracks API calls such as `ModifySnapshotAttribute`, `ResetSnapshotAttribute`, and `ModifySnapshotTier`. - Azure Monitor Logs - Logs changes via `Microsoft.Compute/snapshots/write`. - Google Cloud Logging - Captures modifications through `compute.snapshots.setIamPolicy` and `compute.snapshots.patch`.

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
- DC0058: https://attack.mitre.org/datacomponents/DC0058
- Reviewed: 2026-10-27
