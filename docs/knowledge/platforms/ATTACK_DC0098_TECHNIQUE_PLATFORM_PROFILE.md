# Volume Deletion Technique Platform Profile

## Reference

- Technique: **DC0098 — Volume Deletion**
- Platforms named in the source: not stated

The removal of a cloud-based or on-premise block storage volume. This action permanently deletes the allocated storage and may result in data loss if not backed up. *Data Collection Measures:* - Cloud Logging & APIs - AWS CloudTrail Logs - `eventName: DeleteVolume` (tracks volume deletions) - Azure Monitor Logs - `operationName: Microsoft.Compute/disks/delete` - `status: Success | Failure` (flag unauthorized delete attempts) - Google Cloud Audit Logs - `protoPayload.methodName: "v1.compute.disks.delete"` - `authenticationInfo.principalEmail` (identifies the user deleting the volume) - System & Host-Based Logging - Linux & macOS Logs: - `/var/log/syslog` or `/var/log/messages` for volume detach/deletion actions - Windows Event Logs: - Event ID 98 (Storage Class Memory) - Event ID 225 (Volume Removal Detected) - Event ID 12 (Disk Removal Notification).

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
- DC0098: https://attack.mitre.org/datacomponents/DC0098
- Reviewed: 2026-10-27
