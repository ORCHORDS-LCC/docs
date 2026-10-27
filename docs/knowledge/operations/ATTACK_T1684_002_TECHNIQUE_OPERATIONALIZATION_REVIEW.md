# Email Spoofing Technique Operationalization Review

## Reference

- Technique: **T1684.002 — Email Spoofing**

Adversaries may fake, or spoof, a sender’s identity by modifying the value of relevant email headers in order to establish contact with victims under false pretenses. In addition to actual email content, email headers (such as the FROM header, which contains the email address of the sender) may also be modified. Email clients display these headers when emails appear in a victim's inbox, which may cause modified emails to appear as if they were from the spoofed entity. Enterprise environments can use Domain-based Message Authentication, Reporting, and Conformance (DMARC) as an email authentication protocol that references results of the Sender Policy Framework (SPF) and DomainKeys Identified Mail (DKIM) configurations. SPF and DKIM are configured separately in DNS: SPF verifies that the sending server is authorized for the domain, while DKIM uses a digital signature to verify email integrity and domain authentication. Together, they validate email authenticity and specify how receiving servers should handle authentication failures. Without enforced identity authentication, adversaries may compromise the integrity of an authentication check with altered headers that would not have otherwise passed. An example of a weak or absent DMARC policy is `v=DMARC1; p=none; fo=1;`. The `p=none`. The `p=none` indicates no action should be taken, and therefore no filtering action will take place, even if an email fails authentication checks (i.e., SPF and/or DKIM fail). When a DMARC policy indicates no action, the email will still be delivered to the victim’s inbox. Adversaries have abused weak or absent DMARC policies to circumvent authentication checks and conceal social engineering attempts. Adversaries can alter email headers to include legitimate domain names with fake usernames or impersonate legitimate users via Impersonation for Phishing. Additionally, adversaries may abuse Microsoft 365’s Direct Send functionality to spoof internal users by using internal devices like printers to send emails without authentication.

## Operationalization review

1. Record the operational scope: which services, environments, and data the technique could affect.
2. Record the runbook that would be executed, and its owner.
3. Record the telemetry the runbook depends on, and whether it is retained long enough to investigate.
4. Record the detection that would surface the technique before or after it has an effect.
5. Record the recovery path, and the evidence that recovery has been rehearsed.
6. Record the residual operational risk where the runbook depends on a manual step.

## Review evidence

- the runbook and its owner;
- the telemetry retention and coverage record;
- the detection mapping;
- the exercise or rehearsal record.

## Limitations

An operationalization review describes the runbook and the evidence around it. It does not claim the technique has been prevented or detected in a live environment.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1684.002: https://attack.mitre.org/techniques/T1684/002
- Reviewed: 2026-10-27
