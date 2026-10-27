# T1098.002 Additional Email Delegate Permissions Outcome Lesson

## Authoritative description

- Technique: **T1098.002 — Additional Email Delegate Permissions**
- Tactics: persistence, privilege-escalation
- Platforms: Windows, Office Suite

Adversaries may grant additional permission levels to maintain persistent access to an adversary-controlled email account. For example, the <code>Add-MailboxPermission</code> PowerShell cmdlet, available in on-premises Exchange and in the cloud-based service Office 365, adds permissions to a mailbox. In Google Workspace, delegation can be enabled via the Google Admin console and users can delegate accounts via their Gmail settings. Adversaries may also assign mailbox folder permissions through individual folder permissions or roles. In Office 365 environments, adversaries may assign the Default or Anonymous user permissions or roles to the Top of Information Store (root), Inbox, or other mailbox folders. By assigning one or both user permissions to a folder, the adversary can utilize any other account in the tenant to maintain persistence to the target user’s mail folders. This may be used in persistent threat incidents as well as BEC (Business Email Compromise) incidents where an adversary can add Additional Cloud Roles to the accounts they wish to compromise. This may further enable use of additional techniques for gaining access to systems. For example, compromised business accounts are often used to send messages to other accounts in the network of the target business while creating inbox rules (ex: Internal Spearphishing), so the messages evade spam/phishing detection mechanisms.

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
- T1098.002: https://attack.mitre.org/techniques/T1098/002
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
