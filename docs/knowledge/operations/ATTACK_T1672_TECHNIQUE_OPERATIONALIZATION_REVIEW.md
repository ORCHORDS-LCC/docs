# Email Spoofing Technique Operationalization Review

## Reference

- Technique: **T1672 — Email Spoofing**

Adversaries may fake, or spoof, a sender’s identity by modifying the value of relevant email headers in order to establish contact with victims under false pretenses. In addition to actual email content, email headers (such as the FROM header, which contains the email address of the sender) may also be modified. Email clients display these headers when emails appear in a victim's inbox, which may cause modified emails to appear as if they were from the spoofed entity. This behavior may succeed when the spoofed entity either does not enable or enforce identity authentication tools such as Sender Policy Framework (SPF), DomainKeys Identified Mail (DKIM), and/or Domain-based Message Authentication, Reporting and Conformance (DMARC). Even if SPF and DKIM are configured properly, spoofing may still succeed when a domain sets a weak DMARC policy such as `v=DMARC1; p=none; fo=1;`. This means that while DMARC is technically present, email servers are not instructed to take any filtering action when emails fail authentication checks. Adversaries may abuse Microsoft 365’s Direct Send functionality to spoof internal users by using internal devices like printers to send emails without authentication. Adversaries may also abuse absent or weakly configured SPF, SKIM, and/or DMARC policies to conceal social engineering attempts such as Phishing. They may also leverage email spoofing for Impersonation of legitimate external individuals and organizations, such as journalists and academics.

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
- T1672: https://attack.mitre.org/techniques/T1672
- Reviewed: 2026-10-27
