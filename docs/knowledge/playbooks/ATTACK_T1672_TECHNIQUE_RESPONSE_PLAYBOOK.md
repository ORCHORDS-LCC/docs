# Email Spoofing Technique Response Playbook

## Target technique

**T1672 — Email Spoofing**

- Tactics: stealth
- Platforms: Office Suite, Windows, macOS, Linux

Adversaries may fake, or spoof, a sender’s identity by modifying the value of relevant email headers in order to establish contact with victims under false pretenses. In addition to actual email content, email headers (such as the FROM header, which contains the email address of the sender) may also be modified. Email clients display these headers when emails appear in a victim's inbox, which may cause modified emails to appear as if they were from the spoofed entity. This behavior may succeed when the spoofed entity either does not enable or enforce identity authentication tools such as Sender Policy Framework (SPF), DomainKeys Identified Mail (DKIM), and/or Domain-based Message Authentication, Reporting and Conformance (DMARC). Even if SPF and DKIM are configured properly, spoofing may still succeed when a domain sets a weak DMARC policy such as `v=DMARC1; p=none; fo=1;`. This means that while DMARC is technically present, email servers are not instructed to take any filtering action when emails fail authentication checks. Adversaries may abuse Microsoft 365’s Direct Send functionality to spoof internal users by using internal devices like printers to send emails without authentication. Adversaries may also abuse absent or weakly configured SPF, SKIM, and/or DMARC policies to conceal social engineering attempts such as Phishing. They may also leverage email spoofing for Impersonation of legitimate external individuals and organizations, such as journalists and academics.

## Preconditions

- the estate in scope is identified, with the systems the technique could apply to;
- an owner is accountable for detection and response;
- current telemetry and configuration can be inspected;
- the technique is applicable or requires an applicability decision.

## Procedure

1. Confirm the scope and owner.
2. Read the current technique description and the associated detection guidance.
3. Inventory the telemetry that would carry the technique's indicators.
4. Inspect whether the indicators are present in the environment.
5. Exercise the detection path and confirm it produces the expected signal.
6. Record gaps in detection coverage and assign remediation owners.
7. Record justified non-applicability or accepted detection gaps separately.
8. Set the next event-driven or periodic verification trigger.

## Failure handling

If the detection path does not produce the expected signal, treat the coverage as unverified, preserve the test evidence, and route the gap through the appropriate remediation or risk process.

## Completion evidence

Scope, owner, source version, telemetry inspected, tests performed, findings, exceptions, remediation links, reviewer, and next trigger.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1672: https://attack.mitre.org/techniques/T1672
- Reviewed: 2026-10-27
