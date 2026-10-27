# DC0046 Drive Modification Outcome Lesson

## Authoritative description

- Technique: **DC0046 — Drive Modification**

The alteration of a drive letter, mount point, or other attributes of a data storage device, which could involve reassignment, renaming, permissions changes, or other modifications. Examples: - Drive Letter Reassignment: A USB drive previously assigned `E:\` is reassigned to `D:\` on a Windows machine. - Mount Point Change: On a Linux system, a mounted storage device at `/mnt/external` is moved to `/mnt/storage`. - Drive Permission Changes: A shared drive's permissions are modified to allow write access for unauthorized users or processes. - Renaming of a Drive: A network drive labeled "HR_Share" is renamed to "Shared_Resources." - Modification of Cloud-Integrated Drives: A cloud storage mount such as Google Drive is modified to sync only specific folders. This data component can be collected through the following measures: Windows Event Logs - Relevant Events: - Event ID 98: Indicates changes to a volume (e.g., drive letter reassignment). - Event ID 1006: Logs permission modifications or changes to removable storage. - Configuration: Enable "Storage Operational Logs" in the Event Viewer: `Applications and Services Logs > Microsoft > Windows > Storage-Tiering > Operational` Linux System Logs - Auditd Configuration: Add audit rules to track changes to mounted drives: `auditctl -w /mnt/ -p w -k drive_modification` - Command-Line Monitoring: Use `dmesg` or `journalctl` to observe drive modifications. macOS System Logs - Unified Logs: Collect mount or drive modification events: `log show --info | grep "Volume modified"` - Command-Line Monitoring: Use `diskutil` to track changes: Endpoint Detection and Response (EDR) Tools - Configure policies in EDR solutions to monitor and log changes to drive configurations or attributes. SIEM Tools - Aggregate logs from multiple systems into a centralized platform like Splunk to correlate events and alert on suspicious drive modification activities.

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
- DC0046: https://attack.mitre.org/datacomponents/DC0046
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
