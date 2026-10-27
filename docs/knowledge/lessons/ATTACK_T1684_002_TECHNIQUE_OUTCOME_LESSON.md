# T1684.002 Email Spoofing Outcome Lesson

## Authoritative description

- Technique: **T1684.002 — Email Spoofing**
- Tactics: stealth
- Platforms: Linux, macOS, Office Suite, Windows

Adversaries may fake, or spoof, a sender’s identity by modifying the value of relevant email headers in order to establish contact with victims under false pretenses. In addition to actual email content, email headers (such as the FROM header, which contains the email address of the sender) may also be modified. Email clients display these headers when emails appear in a victim's inbox, which may cause modified emails to appear as if they were from the spoofed entity. Enterprise environments can use Domain-based Message Authentication, Reporting, and Conformance (DMARC) as an email authentication protocol that references results of the Sender Policy Framework (SPF) and DomainKeys Identified Mail (DKIM) configurations. SPF and DKIM are configured separately in DNS: SPF verifies that the sending server is authorized for the domain, while DKIM uses a digital signature to verify email integrity and domain authentication. Together, they validate email authenticity and specify how receiving servers should handle authentication failures. Without enforced identity authentication, adversaries may compromise the integrity of an authentication check with altered headers that would not have otherwise passed. An example of a weak or absent DMARC policy is `v=DMARC1; p=none; fo=1;`. The `p=none`. The `p=none` indicates no action should be taken, and therefore no filtering action will take place, even if an email fails authentication checks (i.e., SPF and/or DKIM fail). When a DMARC policy indicates no action, the email will still be delivered to the victim’s inbox. Adversaries have abused weak or absent DMARC policies to circumvent authentication checks and conceal social engineering attempts. Adversaries can alter email headers to include legitimate domain names with fake usernames or impersonate legitimate users via Impersonation for Phishing. Additionally, adversaries may abuse Microsoft 365’s Direct Send functionality to spoof internal users by using internal devices like printers to send emails without authentication.

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
- T1684.002: https://attack.mitre.org/techniques/T1684/002
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
