# Compression Technique Operationalization Review

## Reference

- Technique: **T1027.015 — Compression**

Adversaries may use compression to obfuscate their payloads or files. Compressed file formats such as ZIP, gzip, 7z, and RAR can compress and archive multiple files together to make it easier and faster to transfer files. In addition to compressing files, adversaries may also compress shellcode directly - for example, in order to store it in a Windows Registry key (i.e., Fileless Storage). In order to further evade detection, adversaries may combine multiple ZIP files into one archive. This process of concatenation creates an archive that appears to be a single archive but in fact contains the central directories of the embedded archives. Some ZIP readers, such as 7zip, may not be able to identify concatenated ZIP files and miss the presence of the malicious payload. File archives may be sent as one Spearphishing Attachment through email. Adversaries have sent malicious payloads as archived files to encourage the user to interact with and extract the malicious payload onto their system (i.e., Malicious File). However, some file compression tools, such as 7zip, can be used to produce self-extracting archives. Adversaries may send self-extracting archives to hide the functionality of their payload and launch it without requiring multiple actions from the user. Compression may be used in combination with Encrypted/Encoded File where compressed files are encrypted and password-protected.

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
- T1027.015: https://attack.mitre.org/techniques/T1027/015
- Reviewed: 2026-10-27
