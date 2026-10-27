# T1531 Account Access Removal Outcome Lesson

## Authoritative description

- Technique: **T1531 — Account Access Removal**
- Tactics: impact
- Platforms: Linux, macOS, Windows, SaaS, IaaS, Office Suite, ESXi

Adversaries may interrupt availability of system and network resources by inhibiting access to accounts utilized by legitimate users. Accounts may be deleted, locked, or manipulated (ex: changed credentials, revoked permissions for SaaS platforms such as Sharepoint) to remove access to accounts. Adversaries may also subsequently log off and/or perform a System Shutdown/Reboot to set malicious changes into place. In Windows, Net utility, <code>Set-LocalUser</code> and <code>Set-ADAccountPassword</code> PowerShell cmdlets may be used by adversaries to modify user accounts. Accounts could also be disabled by Group Policy. In Linux, the <code>passwd</code> utility may be used to change passwords. On ESXi servers, accounts can be removed or modified via esxcli (`system account set`, `system account remove`). Adversaries who use ransomware or similar attacks may first perform this and other Impact behaviors, such as Data Destruction and Defacement, in order to impede incident response/recovery before completing the Data Encrypted for Impact objective.

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
- T1531: https://attack.mitre.org/techniques/T1531
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
