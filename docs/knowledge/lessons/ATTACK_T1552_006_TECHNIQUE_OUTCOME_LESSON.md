# T1552.006 Group Policy Preferences Outcome Lesson

## Authoritative description

- Technique: **T1552.006 — Group Policy Preferences**
- Tactics: credential-access
- Platforms: Windows

Adversaries may attempt to find unsecured credentials in Group Policy Preferences (GPP). GPP are tools that allow administrators to create domain policies with embedded credentials. These policies allow administrators to set local accounts. These group policies are stored in SYSVOL on a domain controller. This means that any domain user can view the SYSVOL share and decrypt the password (using the AES key that has been made public). The following tools and scripts can be used to gather and decrypt the password file from Group Policy Preference XML files: * Metasploit’s post exploitation module: <code>post/windows/gather/credentials/gpp</code> * Get-GPPPassword * gpprefdecrypt.py On the SYSVOL share, adversaries may use the following command to enumerate potential GPP XML files: <code>dir /s * .xml</code>.

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
- T1552.006: https://attack.mitre.org/techniques/T1552/006
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
