# T1087.002 Domain Account Outcome Lesson

## Authoritative description

- Technique: **T1087.002 — Domain Account**
- Tactics: discovery
- Platforms: Linux, macOS, Windows

Adversaries may attempt to get a listing of domain accounts. This information can help adversaries determine which domain accounts exist to aid in follow-on behavior such as targeting specific accounts which possess particular privileges. Commands such as net user /domain and net group /domain of the Net utility, dscacheutil -q group on macOS, and ldapsearch on Linux can list domain users and groups. PowerShell cmdlets including Get-ADUser and Get-ADGroupMember may enumerate members of Active Directory groups.

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
- T1087.002: https://attack.mitre.org/techniques/T1087/002
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
