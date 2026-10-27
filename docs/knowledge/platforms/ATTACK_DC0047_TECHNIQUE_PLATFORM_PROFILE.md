# Snapshot Enumeration Technique Platform Profile

## Reference

- Technique: **DC0047 — Snapshot Enumeration**
- Platforms named in the source: not stated

The process of listing or retrieving metadata about existing snapshots in a cloud environment. *Data Collection Measures:* - AWS CloudTrail - Logs API calls such as `DescribeSnapshots`, `ListSnapshots`, and `GetSnapshotAttributes`. - Azure Monitor Logs - Tracks snapshot enumeration via `Microsoft.Compute/snapshots/read`. - Google Cloud Logging - Detects snapshot listing through `compute.disks.listSnapshots`.

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
- DC0047: https://attack.mitre.org/datacomponents/DC0047
- Reviewed: 2026-10-27
