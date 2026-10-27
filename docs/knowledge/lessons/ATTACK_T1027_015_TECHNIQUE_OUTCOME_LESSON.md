# T1027.015 Compression Outcome Lesson

## Authoritative description

- Technique: **T1027.015 — Compression**
- Tactics: stealth
- Platforms: Linux, macOS, Windows

Adversaries may use compression to obfuscate their payloads or files. Compressed file formats such as ZIP, gzip, 7z, and RAR can compress and archive multiple files together to make it easier and faster to transfer files. In addition to compressing files, adversaries may also compress shellcode directly - for example, in order to store it in a Windows Registry key (i.e., Fileless Storage). In order to further evade detection, adversaries may combine multiple ZIP files into one archive. This process of concatenation creates an archive that appears to be a single archive but in fact contains the central directories of the embedded archives. Some ZIP readers, such as 7zip, may not be able to identify concatenated ZIP files and miss the presence of the malicious payload. File archives may be sent as one Spearphishing Attachment through email. Adversaries have sent malicious payloads as archived files to encourage the user to interact with and extract the malicious payload onto their system (i.e., Malicious File). However, some file compression tools, such as 7zip, can be used to produce self-extracting archives. Adversaries may send self-extracting archives to hide the functionality of their payload and launch it without requiring multiple actions from the user. Compression may be used in combination with Encrypted/Encoded File where compressed files are encrypted and password-protected.

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
- T1027.015: https://attack.mitre.org/techniques/T1027/015
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
