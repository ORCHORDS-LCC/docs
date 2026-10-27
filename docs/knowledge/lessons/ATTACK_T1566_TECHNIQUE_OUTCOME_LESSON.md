# T1566 Phishing Outcome Lesson

## Authoritative description

- Technique: **T1566 — Phishing**
- Tactics: initial-access
- Platforms: Identity Provider, Linux, macOS, Office Suite, SaaS, Windows

Adversaries may send phishing messages to gain access to victim systems. All forms of phishing are electronically delivered social engineering. Phishing can be targeted, known as spearphishing. In spearphishing, a specific individual, company, or industry will be targeted by the adversary. More generally, adversaries can conduct non-targeted phishing, such as in mass malware spam campaigns. Adversaries may send victims emails containing malicious attachments or links, typically to execute malicious code on victim systems. Phishing may also be conducted via third-party services (like social media platforms) or delivered via calendar invites. Phishing may also involve social engineering techniques, such as posing as a trusted source, as well as evasive techniques such as removing or manipulating emails or metadata/headers from compromised accounts being abused to send messages (e.g., Email Hiding Rules). Another way to accomplish this is by Email Spoofing the identity of the sender, which can be used to fool both the human recipient as well as automated security tools, or by including the intended target as a party to an existing email thread that includes malicious files or links (i.e., "thread hijacking"). Victims may also receive phishing messages that instruct them to call a phone number where they are directed to visit a malicious URL, download malware, or install adversary-accessible remote management tools onto their computer (i.e., User Execution).

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
- T1566: https://attack.mitre.org/techniques/T1566
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
