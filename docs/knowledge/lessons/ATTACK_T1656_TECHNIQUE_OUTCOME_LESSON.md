# T1656 Impersonation Outcome Lesson

## Authoritative description

- Technique: **T1656 — Impersonation**
- Tactics: stealth
- Platforms: Linux, macOS, Office Suite, SaaS, Windows

Adversaries may impersonate a trusted person or organization in order to persuade and trick a target into performing some action on their behalf. For example, adversaries may communicate with victims (via Phishing for Information, Phishing, or Internal Spearphishing) while impersonating a known sender such as an executive, colleague, or third-party vendor. Established trust can then be leveraged to accomplish an adversary’s ultimate goals, possibly against multiple victims. In many cases of business email compromise or email fraud campaigns, adversaries use impersonation to defraud victims -- deceiving them into sending money or divulging information that ultimately enables Financial Theft. Adversaries will often also use social engineering techniques such as manipulative and persuasive language in email subject lines and body text such as `payment`, `request`, or `urgent` to push the victim to act quickly before malicious activity is detected. These campaigns are often specifically targeted against people who, due to job roles and/or accesses, can carry out the adversary’s goal. Impersonation is typically preceded by reconnaissance techniques such as Gather Victim Identity Information and Gather Victim Org Information as well as acquiring infrastructure such as email domains (i.e. Domains) to substantiate their false identity. There is the potential for multiple victims in campaigns involving impersonation. For example, an adversary may Compromise Accounts targeting one organization which can then be used to support impersonation against other entities.

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
- T1656: https://attack.mitre.org/techniques/T1656
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
