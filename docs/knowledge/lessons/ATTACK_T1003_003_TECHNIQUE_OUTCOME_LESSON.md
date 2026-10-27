# T1003.003 NTDS Outcome Lesson

## Authoritative description

- Technique: **T1003.003 — NTDS**
- Tactics: credential-access
- Platforms: Windows

Adversaries may attempt to access or create a copy of the Active Directory domain database in order to steal credential information, as well as obtain other information about domain members such as devices, users, and access rights. By default, the NTDS file (NTDS.dit) is located in <code>%SystemRoot%\NTDS\Ntds.dit</code> of a domain controller. In addition to looking for NTDS files on active Domain Controllers, adversaries may search for backups that contain the same or similar information. The following tools and techniques can be used to enumerate the NTDS file and the contents of the entire Active Directory hashes. * Volume Shadow Copy * secretsdump.py * Using the in-built Windows tool, ntdsutil.exe * Invoke-NinjaCopy.

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
- T1003.003: https://attack.mitre.org/techniques/T1003/003
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
