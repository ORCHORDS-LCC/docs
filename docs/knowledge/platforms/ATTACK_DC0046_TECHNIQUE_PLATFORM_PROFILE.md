# Drive Modification Technique Platform Profile

## Reference

- Technique: **DC0046 — Drive Modification**
- Platforms named in the source: not stated

The alteration of a drive letter, mount point, or other attributes of a data storage device, which could involve reassignment, renaming, permissions changes, or other modifications. Examples: - Drive Letter Reassignment: A USB drive previously assigned `E:\` is reassigned to `D:\` on a Windows machine. - Mount Point Change: On a Linux system, a mounted storage device at `/mnt/external` is moved to `/mnt/storage`. - Drive Permission Changes: A shared drive's permissions are modified to allow write access for unauthorized users or processes. - Renaming of a Drive: A network drive labeled "HR_Share" is renamed to "Shared_Resources." - Modification of Cloud-Integrated Drives: A cloud storage mount such as Google Drive is modified to sync only specific folders. This data component can be collected through the following measures: Windows Event Logs - Relevant Events: - Event ID 98: Indicates changes to a volume (e.g., drive letter reassignment). - Event ID 1006: Logs permission modifications or changes to removable storage. - Configuration: Enable "Storage Operational Logs" in the Event Viewer: `Applications and Services Logs > Microsoft > Windows > Storage-Tiering > Operational` Linux System Logs - Auditd Configuration: Add audit rules to track changes to mounted drives: `auditctl -w /mnt/ -p w -k drive_modification` - Command-Line Monitoring: Use `dmesg` or `journalctl` to observe drive modifications. macOS System Logs - Unified Logs: Collect mount or drive modification events: `log show --info | grep "Volume modified"` - Command-Line Monitoring: Use `diskutil` to track changes: Endpoint Detection and Response (EDR) Tools - Configure policies in EDR solutions to monitor and log changes to drive configurations or attributes. SIEM Tools - Aggregate logs from multiple systems into a centralized platform like Splunk to correlate events and alert on suspicious drive modification activities.

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
- DC0046: https://attack.mitre.org/datacomponents/DC0046
- Reviewed: 2026-10-27
