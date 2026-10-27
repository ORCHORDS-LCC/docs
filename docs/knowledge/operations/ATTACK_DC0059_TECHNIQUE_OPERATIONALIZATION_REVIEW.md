# File Metadata Technique Operationalization Review

## Reference

- Technique: **DC0059 — File Metadata**

Contextual information about a file, including attributes such as the file's name, size, type, content (e.g., signatures, headers, media), user/owner, permissions, timestamps, and other related properties. File metadata provides insights into a file's characteristics and can be used to detect malicious activity, unauthorized modifications, or other anomalies. Examples: - File Ownership and Permissions: Checking the owner and permissions of a critical configuration file like /etc/passwd on Linux or C:\Windows\System32\config\SAM on Windows. - Timestamps: Analyzing the creation, modification, and access timestamps of a file. - File Content and Signatures: Extracting the headers of an executable file to verify its signature or detect packing/obfuscation. - File Attributes: Analyzing attributes like hidden, system, or read-only flags in Windows. - File Hashes: Generating MD5, SHA-1, or SHA-256 hashes of files to compare against threat intelligence feeds. - File Location: Monitoring files located in unusual directories or paths, such as temporary or user folders.

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
- DC0059: https://attack.mitre.org/datacomponents/DC0059
- Reviewed: 2026-10-27
