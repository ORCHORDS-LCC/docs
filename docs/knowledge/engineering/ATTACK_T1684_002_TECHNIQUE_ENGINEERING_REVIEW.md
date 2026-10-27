# Email Spoofing Technique Engineering Review

## Reference

- Technique: **T1684.002 — Email Spoofing**

Adversaries may fake, or spoof, a sender’s identity by modifying the value of relevant email headers in order to establish contact with victims under false pretenses. In addition to actual email content, email headers (such as the FROM header, which contains the email address of the sender) may also be modified. Email clients display these headers when emails appear in a victim's inbox, which may cause modified emails to appear as if they were from the spoofed entity. Enterprise environments can use Domain-based Message Authentication, Reporting, and Conformance (DMARC) as an email authentication protocol that references results of the Sender Policy Framework (SPF) and DomainKeys Identified Mail (DKIM) configurations. SPF and DKIM are configured separately in DNS: SPF verifies that the sending server is authorized for the domain, while DKIM uses a digital signature to verify email integrity and domain authentication. Together, they validate email authenticity and specify how receiving servers should handle authentication failures. Without enforced identity authentication, adversaries may compromise the integrity of an authentication check with altered headers that would not have otherwise passed. An example of a weak or absent DMARC policy is `v=DMARC1; p=none; fo=1;`. The `p=none`. The `p=none` indicates no action should be taken, and therefore no filtering action will take place, even if an email fails authentication checks (i.e., SPF and/or DKIM fail). When a DMARC policy indicates no action, the email will still be delivered to the victim’s inbox. Adversaries have abused weak or absent DMARC policies to circumvent authentication checks and conceal social engineering attempts. Adversaries can alter email headers to include legitimate domain names with fake usernames or impersonate legitimate users via Impersonation for Phishing. Additionally, adversaries may abuse Microsoft 365’s Direct Send functionality to spoof internal users by using internal devices like printers to send emails without authentication.

## Engineering review

1. Identify the engineering boundary where the technique would apply: the component, the service, or the deployment.
2. Review the design decision that would prevent the technique, and record the alternative considered.
3. Review the implementation evidence for the preventive control.
4. Review the test coverage that would fail if the control regressed.
5. Review the observability: which signal would show the control is not operating.
6. Record the residual risk where prevention is not achievable, and the detection that compensates.

## Review evidence

- the design record for the preventive decision;
- the implementation or configuration evidence;
- the test record showing the control is exercised;
- the observability mapping.

## Limitations

An engineering review describes what the design and the implementation evidence show. It does not claim the technique has been addressed in production.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1684.002: https://attack.mitre.org/techniques/T1684/002
- Reviewed: 2026-10-27
