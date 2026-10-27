# Drive Access Technique Response Playbook

## Target technique

**DC0054 — Drive Access**


Refers to the act of accessing a data storage device, such as a hard drive, SSD, USB, or network-mounted drive. This data component logs the opening or mounting of drives, capturing activities such as reading, writing, or executing files within an assigned drive letter (e.g., `C:\`, `/mnt/drive`) or mount point. Examples: - Removable Drive Insertion: A USB drive is inserted, assigned the letter `F:\`, and files are accessed. - Network Drive Mounting: A network share `\\server\share` is mapped to the drive `Z:\`. - External Hard Drive Access: An external drive is connected, mounted at `/mnt/backup`, and accessed for copying files. - System Volume Access: The system volume `C:\` is accessed for modifications to critical files. - Cloud-Synced Drives: Cloud storage drives like OneDrive or Google Drive are accessed via local mounts.

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
- DC0054: https://attack.mitre.org/datacomponents/DC0054
- Reviewed: 2026-10-27
