# T1027.011 Fileless Storage Outcome Lesson

## Authoritative description

- Technique: **T1027.011 — Fileless Storage**
- Tactics: stealth
- Platforms: Linux, Windows

Adversaries may store data in "fileless" formats to conceal malicious activity from defenses. Fileless storage can be broadly defined as any format other than a file. Common examples of non-volatile fileless storage in Windows systems include the Windows Registry, event logs, or WMI repository. Shared memory directories on Linux systems (`/dev/shm`, `/run/shm`, `/var/run`, and `/var/lock`) and volatile directories on Network Devices (`/tmp` and `/volatile`) may also be considered fileless storage, as files written to these directories are mapped directly to RAM and not stored on the disk.. Similar to fileless in-memory behaviors such as Reflective Code Loading and Process Injection, fileless data storage may remain undetected by antivirus and other endpoint security tools that can only access specific file formats from disk storage. Leveraging fileless storage may also allow adversaries to bypass the protections offered by read-only file systems in Linux. Adversaries may use fileless storage to conceal various types of stored data, including payloads/shellcode (potentially being used as part of Persistence) and collected data not yet exfiltrated from the victim (e.g., Local Data Staging). Adversaries also often encrypt, encode, splice, or otherwise obfuscate this fileless data when stored. Some forms of fileless storage activity may indirectly create artifacts in the file system, but in central and otherwise difficult to inspect formats such as the WMI (e.g., `%SystemRoot%\System32\Wbem\Repository`) or Registry (e.g., `%SystemRoot%\System32\Config`) physical files.

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
- T1027.011: https://attack.mitre.org/techniques/T1027/011
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
