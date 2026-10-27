# Snapshot Modification Technique Platform Profile

## Reference

- Technique: **DC0058 — Snapshot Modification**
- Platforms named in the source: not stated

Changes made to a cloud snapshot's metadata, attributes, or control settings. These modifications may involve adjusting access permissions, changing retention policies, or altering encryption settings. *Data Collection Measures:* - AWS CloudTrail - Tracks API calls such as `ModifySnapshotAttribute`, `ResetSnapshotAttribute`, and `ModifySnapshotTier`. - Azure Monitor Logs - Logs changes via `Microsoft.Compute/snapshots/write`. - Google Cloud Logging - Captures modifications through `compute.snapshots.setIamPolicy` and `compute.snapshots.patch`.

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
- DC0058: https://attack.mitre.org/datacomponents/DC0058
- Reviewed: 2026-10-27
