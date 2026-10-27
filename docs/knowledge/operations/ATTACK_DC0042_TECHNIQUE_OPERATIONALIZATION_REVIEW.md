# Drive Creation Technique Operationalization Review

## Reference

- Technique: **DC0042 — Drive Creation**

The activity of assigning a new drive letter or creating a mount point for a data storage device, such as a USB, network share, or external hard drive, enabling access to its content on a host system. Examples: - USB Drive Insertion: A USB drive is plugged in and automatically assigned the letter `E:\` on a Windows machine. - Network Drive Mapping: A network share `\\server\share` is mapped to the drive `Z:\`. - Virtual Drive Creation: A virtual disk is mounted on `/mnt/virtualdrive` using an ISO image or a virtual hard disk (VHD). - Cloud Storage Mounting: Google Drive is mounted as `G:\` on a Windows machine using a cloud sync tool. - External Storage Integration: An external HDD or SSD is connected and assigned `/mnt/external` on a Linux system..

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
- DC0042: https://attack.mitre.org/datacomponents/DC0042
- Reviewed: 2026-10-27
