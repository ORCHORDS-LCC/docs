# Drive Access Technique Operationalization Review

## Reference

- Technique: **DC0054 — Drive Access**

Refers to the act of accessing a data storage device, such as a hard drive, SSD, USB, or network-mounted drive. This data component logs the opening or mounting of drives, capturing activities such as reading, writing, or executing files within an assigned drive letter (e.g., `C:\`, `/mnt/drive`) or mount point. Examples: - Removable Drive Insertion: A USB drive is inserted, assigned the letter `F:\`, and files are accessed. - Network Drive Mounting: A network share `\\server\share` is mapped to the drive `Z:\`. - External Hard Drive Access: An external drive is connected, mounted at `/mnt/backup`, and accessed for copying files. - System Volume Access: The system volume `C:\` is accessed for modifications to critical files. - Cloud-Synced Drives: Cloud storage drives like OneDrive or Google Drive are accessed via local mounts.

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
- DC0054: https://attack.mitre.org/datacomponents/DC0054
- Reviewed: 2026-10-27
