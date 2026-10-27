# S9002 Diskpart Outcome Lesson

## Authoritative description

- Technique: **S9002 — Diskpart**
- Platforms: Windows

Diskpart is a Windows command-line utility that is used to manage the computer’s drives, which includes disks, partitions, volumes and virtual hard disks. Adversaries may abuse Diskpart to perform discovery and destructive actions on a system’s storage. For example, adversaries have been observed using Diskpart to conduct Discovery techniques to enumerate disks and volumes to gather information about the host environment, and to execute commands such as `clean all` to remove partition information and overwrite data across disks, resulting in data destruction.

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
- S9002: https://attack.mitre.org/software/S9002
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
