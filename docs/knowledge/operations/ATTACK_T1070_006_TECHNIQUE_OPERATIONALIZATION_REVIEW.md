# Timestomp Technique Operationalization Review

## Reference

- Technique: **T1070.006 — Timestomp**

Adversaries may modify file time attributes to hide new files or changes to existing files. Timestomping is a technique that modifies the timestamps of a file (the modify, access, create, and change times), often to mimic files that are in the same folder and blend malicious files with legitimate files. In Windows systems, both the `$STANDARD_INFORMATION` (`$SI`) and `$FILE_NAME` (`$FN`) attributes record times in a Master File Table (MFT) file. `$SI` (dates/time stamps) is displayed to the end user, including in the File System view, while `$FN` is dealt with by the kernel. Modifying the `$SI` attribute is the most common method of timestomping because it can be modified at the user level using API calls. `$FN` timestomping, however, typically requires interacting with the system kernel or moving or renaming a file. Adversaries modify timestamps on files so that they do not appear conspicuous to forensic investigators or file analysis tools. In order to evade detections that rely on identifying discrepancies between the `$SI` and `$FN` attributes, adversaries may also engage in “double timestomping” by modifying times on both attributes simultaneously. In Linux systems and on ESXi servers, threat actors may attempt to perform timestomping using commands such as `touch -a -m -t <timestamp> <filename>` (which sets access and modification times to a specific value) or `touch -r <filename> <filename>` (which sets access and modification times to match those of another file). Timestomping may be used along with file name Masquerading to hide malware and tools.

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
- T1070.006: https://attack.mitre.org/techniques/T1070/006
- Reviewed: 2026-10-27
