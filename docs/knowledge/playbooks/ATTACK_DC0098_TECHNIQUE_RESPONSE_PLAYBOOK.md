# Volume Deletion Technique Response Playbook

## Target technique

**DC0098 — Volume Deletion**


The removal of a cloud-based or on-premise block storage volume. This action permanently deletes the allocated storage and may result in data loss if not backed up. *Data Collection Measures:* - Cloud Logging & APIs - AWS CloudTrail Logs - `eventName: DeleteVolume` (tracks volume deletions) - Azure Monitor Logs - `operationName: Microsoft.Compute/disks/delete` - `status: Success | Failure` (flag unauthorized delete attempts) - Google Cloud Audit Logs - `protoPayload.methodName: "v1.compute.disks.delete"` - `authenticationInfo.principalEmail` (identifies the user deleting the volume) - System & Host-Based Logging - Linux & macOS Logs: - `/var/log/syslog` or `/var/log/messages` for volume detach/deletion actions - Windows Event Logs: - Event ID 98 (Storage Class Memory) - Event ID 225 (Volume Removal Detected) - Event ID 12 (Disk Removal Notification).

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
- DC0098: https://attack.mitre.org/datacomponents/DC0098
- Reviewed: 2026-10-27
