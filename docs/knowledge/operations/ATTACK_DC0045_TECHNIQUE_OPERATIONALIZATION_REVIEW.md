# Windows Registry Key Deletion Technique Operationalization Review

## Reference

- Technique: **DC0045 — Windows Registry Key Deletion**

The removal of a registry key within the Windows operating system. *Data Collection Measures:* - Windows Event Logs - Event ID 4658 - Registry Key Handle Closed: Captures when a handle to a registry key is closed, which may indicate deletion. - Event ID 4660 - Object Deleted: Logs when a registry key is deleted. - Sysmon (System Monitor) for Windows - Sysmon Event ID 12 - Registry Key Deleted: Logs when a registry key is removed. - Sysmon Event ID 13 - Registry Value Deleted: Captures removal of specific registry values. - Endpoint Detection and Response (EDR) Solutions - Monitor registry deletions for suspicious behavior.

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
- DC0045: https://attack.mitre.org/datacomponents/DC0045
- Reviewed: 2026-10-27
