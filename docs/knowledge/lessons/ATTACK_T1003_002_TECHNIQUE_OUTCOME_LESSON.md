# T1003.002 Security Account Manager Outcome Lesson

## Authoritative description

- Technique: **T1003.002 — Security Account Manager**
- Tactics: credential-access
- Platforms: Windows

Adversaries may attempt to extract credential material from the Security Account Manager (SAM) database either through in-memory techniques or through the Windows Registry where the SAM database is stored. The SAM is a database file that contains local accounts for the host, typically those found with the net user command. Enumerating the SAM database requires SYSTEM level access. A number of tools can be used to retrieve the SAM file through in-memory techniques: * pwdumpx.exe * gsecdump * Mimikatz * secretsdump.py Alternatively, the SAM can be extracted from the Registry with Reg: * reg save HKLM\sam sam * reg save HKLM\system system Creddump7 can then be used to process the SAM database locally to retrieve hashes. Notes: * RID 500 account is the local, built-in administrator. * RID 501 is the guest account. * User accounts start with a RID of 1,000+.

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
- T1003.002: https://attack.mitre.org/techniques/T1003/002
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
