# T1570 Lateral Tool Transfer Outcome Lesson

## Authoritative description

- Technique: **T1570 — Lateral Tool Transfer**
- Tactics: lateral-movement
- Platforms: ESXi, Linux, macOS, Windows

Adversaries may transfer tools or other files between systems in a compromised environment. Once brought into the victim environment (i.e., Ingress Tool Transfer) files may then be copied from one system to another to stage adversary tools or other files over the course of an operation. Adversaries may copy files between internal victim systems to support lateral movement using inherent file sharing protocols such as file sharing over SMB/Windows Admin Shares to connected network shares or with authenticated connections via Remote Desktop Protocol. Files can also be transferred using native or otherwise present tools on the victim system, such as scp, rsync, curl, sftp, and ftp. In some cases, adversaries may be able to leverage Web Services such as Dropbox or OneDrive to copy files from one machine to another via shared, automatically synced folders.

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
- T1570: https://attack.mitre.org/techniques/T1570
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
