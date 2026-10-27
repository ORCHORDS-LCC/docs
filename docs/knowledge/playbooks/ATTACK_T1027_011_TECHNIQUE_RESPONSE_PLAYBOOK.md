# Fileless Storage Technique Response Playbook

## Target technique

**T1027.011 — Fileless Storage**

- Tactics: stealth
- Platforms: Linux, Windows

Adversaries may store data in "fileless" formats to conceal malicious activity from defenses. Fileless storage can be broadly defined as any format other than a file. Common examples of non-volatile fileless storage in Windows systems include the Windows Registry, event logs, or WMI repository. Shared memory directories on Linux systems (`/dev/shm`, `/run/shm`, `/var/run`, and `/var/lock`) and volatile directories on Network Devices (`/tmp` and `/volatile`) may also be considered fileless storage, as files written to these directories are mapped directly to RAM and not stored on the disk.. Similar to fileless in-memory behaviors such as Reflective Code Loading and Process Injection, fileless data storage may remain undetected by antivirus and other endpoint security tools that can only access specific file formats from disk storage. Leveraging fileless storage may also allow adversaries to bypass the protections offered by read-only file systems in Linux. Adversaries may use fileless storage to conceal various types of stored data, including payloads/shellcode (potentially being used as part of Persistence) and collected data not yet exfiltrated from the victim (e.g., Local Data Staging). Adversaries also often encrypt, encode, splice, or otherwise obfuscate this fileless data when stored. Some forms of fileless storage activity may indirectly create artifacts in the file system, but in central and otherwise difficult to inspect formats such as the WMI (e.g., `%SystemRoot%\System32\Wbem\Repository`) or Registry (e.g., `%SystemRoot%\System32\Config`) physical files.

## Preconditions

- the estate in scope is identified, with the systems the technique could apply to;
- an owner is accountable for detection and response;
- current telemetry and configuration can be inspected;
- the technique is applicable or requires an applicability decision.

## Procedure

1. Confirm the scope and owner.
2. Read the current technique description and the associated detection guidance.
3. Inventory the telemetry that would carry the technique's indicators.
4. Inspect whether the indicators are present in the environment.
5. Exercise the detection path and confirm it produces the expected signal.
6. Record gaps in detection coverage and assign remediation owners.
7. Record justified non-applicability or accepted detection gaps separately.
8. Set the next event-driven or periodic verification trigger.

## Failure handling

If the detection path does not produce the expected signal, treat the coverage as unverified, preserve the test evidence, and route the gap through the appropriate remediation or risk process.

## Completion evidence

Scope, owner, source version, telemetry inspected, tests performed, findings, exceptions, remediation links, reviewer, and next trigger.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1027.011: https://attack.mitre.org/techniques/T1027/011
- Reviewed: 2026-10-27
