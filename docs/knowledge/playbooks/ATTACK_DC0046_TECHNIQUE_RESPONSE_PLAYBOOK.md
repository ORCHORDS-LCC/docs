# Drive Modification Technique Response Playbook

## Target technique

**DC0046 — Drive Modification**


The alteration of a drive letter, mount point, or other attributes of a data storage device, which could involve reassignment, renaming, permissions changes, or other modifications. Examples: - Drive Letter Reassignment: A USB drive previously assigned `E:\` is reassigned to `D:\` on a Windows machine. - Mount Point Change: On a Linux system, a mounted storage device at `/mnt/external` is moved to `/mnt/storage`. - Drive Permission Changes: A shared drive's permissions are modified to allow write access for unauthorized users or processes. - Renaming of a Drive: A network drive labeled "HR_Share" is renamed to "Shared_Resources." - Modification of Cloud-Integrated Drives: A cloud storage mount such as Google Drive is modified to sync only specific folders. This data component can be collected through the following measures: Windows Event Logs - Relevant Events: - Event ID 98: Indicates changes to a volume (e.g., drive letter reassignment). - Event ID 1006: Logs permission modifications or changes to removable storage. - Configuration: Enable "Storage Operational Logs" in the Event Viewer: `Applications and Services Logs > Microsoft > Windows > Storage-Tiering > Operational` Linux System Logs - Auditd Configuration: Add audit rules to track changes to mounted drives: `auditctl -w /mnt/ -p w -k drive_modification` - Command-Line Monitoring: Use `dmesg` or `journalctl` to observe drive modifications. macOS System Logs - Unified Logs: Collect mount or drive modification events: `log show --info | grep "Volume modified"` - Command-Line Monitoring: Use `diskutil` to track changes: Endpoint Detection and Response (EDR) Tools - Configure policies in EDR solutions to monitor and log changes to drive configurations or attributes. SIEM Tools - Aggregate logs from multiple systems into a centralized platform like Splunk to correlate events and alert on suspicious drive modification activities.

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
- DC0046: https://attack.mitre.org/datacomponents/DC0046
- Reviewed: 2026-10-27
