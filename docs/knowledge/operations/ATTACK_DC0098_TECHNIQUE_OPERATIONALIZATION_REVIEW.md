# Volume Deletion Technique Operationalization Review

## Reference

- Technique: **DC0098 — Volume Deletion**

The removal of a cloud-based or on-premise block storage volume. This action permanently deletes the allocated storage and may result in data loss if not backed up. *Data Collection Measures:* - Cloud Logging & APIs - AWS CloudTrail Logs - `eventName: DeleteVolume` (tracks volume deletions) - Azure Monitor Logs - `operationName: Microsoft.Compute/disks/delete` - `status: Success | Failure` (flag unauthorized delete attempts) - Google Cloud Audit Logs - `protoPayload.methodName: "v1.compute.disks.delete"` - `authenticationInfo.principalEmail` (identifies the user deleting the volume) - System & Host-Based Logging - Linux & macOS Logs: - `/var/log/syslog` or `/var/log/messages` for volume detach/deletion actions - Windows Event Logs: - Event ID 98 (Storage Class Memory) - Event ID 225 (Volume Removal Detected) - Event ID 12 (Disk Removal Notification).

## Operationalization review

1. Record the operational scope: which services, environments, and data the technique could affect.
2. Record the runbook that would be executed, and its owner.
3. Record the telemetry the runbook depends on, and whether it is retained long enough to investigate.
4. Record the detection that would surface the technique before or after it has an effect.
5. Record the recovery path, and the evidence that recovery has been rehearsed.
6. Record the residual operational risk where the runbook depends on a manual step.

## Review evidence

- the runbook and its owner;
- the telemetry retention and coverage record;
- the detection mapping;
- the exercise or rehearsal record.

## Limitations

An operationalization review describes the runbook and the evidence around it. It does not claim the technique has been prevented or detected in a live environment.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- DC0098: https://attack.mitre.org/datacomponents/DC0098
- Reviewed: 2026-10-27
