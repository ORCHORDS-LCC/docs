# Windows Registry Key Modification Technique Response Playbook

## Target technique

**DC0063 — Windows Registry Key Modification**


Changes made to an existing registry key or its values. These modifications can include altering permissions, modifying stored data, or updating configuration settings. *Data Collection Measures:* - Windows Event Logs - Event ID 4657 - Registry Value Modified: Logs changes to registry values, including modifications to startup entries, security settings, or system configurations. - Sysmon (System Monitor) for Windows - Sysmon Event ID 13 - Registry Value Set: Captures changes to specific registry values. - Sysmon Event ID 14 - Registry Key & Value Renamed: Logs renaming of registry keys, which may indicate evasion attempts. - Endpoint Detection and Response (EDR) Solutions - Monitor registry modifications for suspicious behavior.

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
- DC0063: https://attack.mitre.org/datacomponents/DC0063
- Reviewed: 2026-10-27
