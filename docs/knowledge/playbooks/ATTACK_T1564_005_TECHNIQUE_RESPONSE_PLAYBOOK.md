# Hidden File System Technique Response Playbook

## Target technique

**T1564.005 — Hidden File System**

- Tactics: stealth
- Platforms: Linux, macOS, Windows

Adversaries may use a hidden file system to conceal malicious activity from users and security tools. File systems provide a structure to store and access data from physical storage. Typically, a user engages with a file system through applications that allow them to access files and directories, which are an abstraction from their physical location (ex: disk sector). Standard file systems include FAT, NTFS, ext4, and APFS. File systems can also contain other structures, such as the Volume Boot Record (VBR) and Master File Table (MFT) in NTFS. Adversaries may use their own abstracted file system, separate from the standard file system present on the infected system. In doing so, adversaries can hide the presence of malicious components and file input/output from security tools. Hidden file systems, sometimes referred to as virtual file systems, can be implemented in numerous ways. One implementation would be to store a file system in reserved disk space unused by disk structures or standard file system partitions. Another implementation could be for an adversary to drop their own portable partition image as a file on top of the standard file system. Adversaries may also fragment files across the existing file system structure in non-standard ways.

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
- T1564.005: https://attack.mitre.org/techniques/T1564/005
- Reviewed: 2026-10-27
