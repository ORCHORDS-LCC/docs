# DC0098 Volume Deletion Outcome Lesson

## Authoritative description

- Technique: **DC0098 — Volume Deletion**

The removal of a cloud-based or on-premise block storage volume. This action permanently deletes the allocated storage and may result in data loss if not backed up. *Data Collection Measures:* - Cloud Logging & APIs - AWS CloudTrail Logs - `eventName: DeleteVolume` (tracks volume deletions) - Azure Monitor Logs - `operationName: Microsoft.Compute/disks/delete` - `status: Success | Failure` (flag unauthorized delete attempts) - Google Cloud Audit Logs - `protoPayload.methodName: "v1.compute.disks.delete"` - `authenticationInfo.principalEmail` (identifies the user deleting the volume) - System & Host-Based Logging - Linux & macOS Logs: - `/var/log/syslog` or `/var/log/messages` for volume detach/deletion actions - Windows Event Logs: - Event ID 98 (Storage Class Memory) - Event ID 225 (Volume Removal Detected) - Event ID 12 (Disk Removal Notification).

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
- DC0098: https://attack.mitre.org/datacomponents/DC0098
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
