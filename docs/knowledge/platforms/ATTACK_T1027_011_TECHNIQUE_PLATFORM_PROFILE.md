# Fileless Storage Technique Platform Profile

## Reference

- Technique: **T1027.011 — Fileless Storage**
- Platforms named in the source: Linux, Windows

Adversaries may store data in "fileless" formats to conceal malicious activity from defenses. Fileless storage can be broadly defined as any format other than a file. Common examples of non-volatile fileless storage in Windows systems include the Windows Registry, event logs, or WMI repository. Shared memory directories on Linux systems (`/dev/shm`, `/run/shm`, `/var/run`, and `/var/lock`) and volatile directories on Network Devices (`/tmp` and `/volatile`) may also be considered fileless storage, as files written to these directories are mapped directly to RAM and not stored on the disk.. Similar to fileless in-memory behaviors such as Reflective Code Loading and Process Injection, fileless data storage may remain undetected by antivirus and other endpoint security tools that can only access specific file formats from disk storage. Leveraging fileless storage may also allow adversaries to bypass the protections offered by read-only file systems in Linux. Adversaries may use fileless storage to conceal various types of stored data, including payloads/shellcode (potentially being used as part of Persistence) and collected data not yet exfiltrated from the victim (e.g., Local Data Staging). Adversaries also often encrypt, encode, splice, or otherwise obfuscate this fileless data when stored. Some forms of fileless storage activity may indirectly create artifacts in the file system, but in central and otherwise difficult to inspect formats such as the WMI (e.g., `%SystemRoot%\System32\Wbem\Repository`) or Registry (e.g., `%SystemRoot%\System32\Config`) physical files.

## Platform profile

1. Record the platforms in scope and the versions actually deployed.
2. Compare the deployed platform surface against the platforms the source names.
3. Record where the platform provides a native control for the technique, and where it does not.
4. Record the configuration evidence for the native control, where one exists.
5. Record the gap where the platform provides no native control, and the compensating detection.
6. Record the platform version, because platform behaviour changes between versions.

## Evidence

- the platform and version inventory for the scoped estate;
- the configuration export or screenshot for the native control;
- the detection evidence where the platform provides none.

## Limitations

A technique entry describes a class of abuse across platforms. The platform-specific exposure is a property of the deployment, established only by inventory and configuration evidence.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1027.011: https://attack.mitre.org/techniques/T1027/011
- Reviewed: 2026-10-27
