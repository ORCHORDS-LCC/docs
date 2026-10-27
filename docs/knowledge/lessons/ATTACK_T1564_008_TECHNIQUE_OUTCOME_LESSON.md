# T1564.008 Email Hiding Rules Outcome Lesson

## Authoritative description

- Technique: **T1564.008 — Email Hiding Rules**
- Tactics: stealth
- Platforms: Windows, Linux, macOS, Office Suite

Adversaries may use email rules to hide inbound emails in a compromised user's mailbox. Many email clients allow users to create inbox rules for various email functions, including moving emails to other folders, marking emails as read, or deleting emails. Rules may be created or modified within email clients or through external features such as the <code>New-InboxRule</code> or <code>Set-InboxRule</code> PowerShell cmdlets on Windows systems. Adversaries may utilize email rules within a compromised user's mailbox to delete and/or move emails to less noticeable folders. Adversaries may do this to hide security alerts, C2 communication, or responses to Internal Spearphishing emails sent from the compromised account. Any user or administrator within the organization (or adversary with valid credentials) may be able to create rules to automatically move or delete emails. These rules can be abused to impair/delay detection had the email content been immediately seen by a user or defender. Malicious rules commonly filter out emails based on key words (such as <code>malware</code>, <code>suspicious</code>, <code>phish</code>, and <code>hack</code>) found in message bodies and subject lines. In some environments, administrators may be able to enable email rules that operate organization-wide rather than on individual inboxes. For example, Microsoft Exchange supports transport rules that evaluate all mail an organization receives against user-specified conditions, then performs a user-specified action on mail that adheres to those conditions. Adversaries that abuse such features may be able to automatically modify or delete all emails related to specific topics (such as internal security incident notifications).

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
- T1564.008: https://attack.mitre.org/techniques/T1564/008
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
