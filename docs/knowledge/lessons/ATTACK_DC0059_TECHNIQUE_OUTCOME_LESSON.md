# DC0059 File Metadata Outcome Lesson

## Authoritative description

- Technique: **DC0059 — File Metadata**

Contextual information about a file, including attributes such as the file's name, size, type, content (e.g., signatures, headers, media), user/owner, permissions, timestamps, and other related properties. File metadata provides insights into a file's characteristics and can be used to detect malicious activity, unauthorized modifications, or other anomalies. Examples: - File Ownership and Permissions: Checking the owner and permissions of a critical configuration file like /etc/passwd on Linux or C:\Windows\System32\config\SAM on Windows. - Timestamps: Analyzing the creation, modification, and access timestamps of a file. - File Content and Signatures: Extracting the headers of an executable file to verify its signature or detect packing/obfuscation. - File Attributes: Analyzing attributes like hidden, system, or read-only flags in Windows. - File Hashes: Generating MD5, SHA-1, or SHA-256 hashes of files to compare against threat intelligence feeds. - File Location: Monitoring files located in unusual directories or paths, such as temporary or user folders.

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
- DC0059: https://attack.mitre.org/datacomponents/DC0059
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
