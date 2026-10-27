# Fileless Storage Technique Operationalization Review

## Reference

- Technique: **T1027.011 — Fileless Storage**

Adversaries may store data in "fileless" formats to conceal malicious activity from defenses. Fileless storage can be broadly defined as any format other than a file. Common examples of non-volatile fileless storage in Windows systems include the Windows Registry, event logs, or WMI repository. Shared memory directories on Linux systems (`/dev/shm`, `/run/shm`, `/var/run`, and `/var/lock`) and volatile directories on Network Devices (`/tmp` and `/volatile`) may also be considered fileless storage, as files written to these directories are mapped directly to RAM and not stored on the disk.. Similar to fileless in-memory behaviors such as Reflective Code Loading and Process Injection, fileless data storage may remain undetected by antivirus and other endpoint security tools that can only access specific file formats from disk storage. Leveraging fileless storage may also allow adversaries to bypass the protections offered by read-only file systems in Linux. Adversaries may use fileless storage to conceal various types of stored data, including payloads/shellcode (potentially being used as part of Persistence) and collected data not yet exfiltrated from the victim (e.g., Local Data Staging). Adversaries also often encrypt, encode, splice, or otherwise obfuscate this fileless data when stored. Some forms of fileless storage activity may indirectly create artifacts in the file system, but in central and otherwise difficult to inspect formats such as the WMI (e.g., `%SystemRoot%\System32\Wbem\Repository`) or Registry (e.g., `%SystemRoot%\System32\Config`) physical files.

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
- T1027.011: https://attack.mitre.org/techniques/T1027/011
- Reviewed: 2026-10-27
