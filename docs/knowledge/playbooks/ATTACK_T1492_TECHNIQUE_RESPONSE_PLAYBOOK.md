# Stored Data Manipulation Mitigation Technique Response Playbook

## Target technique

**T1492 — Stored Data Manipulation Mitigation**


Identify critical business and system processes that may be targeted by adversaries and work to secure the data related to those processes against tampering. Ensure least privilege principles are applied to important information resources to reduce exposure to data manipulation risk. Consider encrypting important information to reduce an adversaries ability to perform tailor data modifications. Where applicable, examine using file monitoring software to check integrity on important files and directories as well as take corrective actions when unauthorized changes are detected. Consider implementing IT disaster recovery plans that contain procedures for taking regular data backups that can be used to restore organizational data. Ensure backups are stored off system and is protected from common methods adversaries may use to gain access and manipulate backups.

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
- T1492: https://attack.mitre.org/mitigations/T1492
- Reviewed: 2026-10-27
