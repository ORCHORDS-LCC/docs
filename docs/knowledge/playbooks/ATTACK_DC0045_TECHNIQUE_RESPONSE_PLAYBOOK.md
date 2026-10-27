# Windows Registry Key Deletion Technique Response Playbook

## Target technique

**DC0045 — Windows Registry Key Deletion**


The removal of a registry key within the Windows operating system. *Data Collection Measures:* - Windows Event Logs - Event ID 4658 - Registry Key Handle Closed: Captures when a handle to a registry key is closed, which may indicate deletion. - Event ID 4660 - Object Deleted: Logs when a registry key is deleted. - Sysmon (System Monitor) for Windows - Sysmon Event ID 12 - Registry Key Deleted: Logs when a registry key is removed. - Sysmon Event ID 13 - Registry Value Deleted: Captures removal of specific registry values. - Endpoint Detection and Response (EDR) Solutions - Monitor registry deletions for suspicious behavior.

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
- DC0045: https://attack.mitre.org/datacomponents/DC0045
- Reviewed: 2026-10-27
