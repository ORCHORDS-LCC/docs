# Disk Content Wipe Technique Operationalization Review

## Reference

- Technique: **T1561.001 — Disk Content Wipe**

Adversaries may erase the contents of storage devices on specific systems or in large numbers in a network to interrupt availability to system and network resources. Adversaries may partially or completely overwrite the contents of a storage device rendering the data irrecoverable through the storage interface. Instead of wiping specific disk structures or files, adversaries with destructive intent may wipe arbitrary portions of disk content. To wipe disk content, adversaries may acquire direct access to the hard drive in order to overwrite arbitrarily sized portions of disk with random data. Adversaries have also been observed leveraging third-party drivers like RawDisk to directly access disk content. This behavior is distinct from Data Destruction because sections of the disk are erased instead of individual files. To maximize impact on the target organization in operations where network-wide availability interruption is the goal, malware used for wiping disk content may have worm-like features to propagate across a network by leveraging additional techniques like Valid Accounts, OS Credential Dumping, and SMB/Windows Admin Shares.

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
- T1561.001: https://attack.mitre.org/techniques/T1561/001
- Reviewed: 2026-10-27
