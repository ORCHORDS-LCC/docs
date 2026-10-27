# Spearphishing Voice Technique Response Playbook

## Target technique

**T1566.004 — Spearphishing Voice**

- Tactics: initial-access
- Platforms: Linux, macOS, Windows, Identity Provider

Adversaries may use voice communications to ultimately gain access to victim systems. Spearphishing voice is a specific variant of spearphishing. It is different from other forms of spearphishing in that it employs the use of manipulating a user into providing access to systems through a phone call or other forms of voice communications. Spearphishing frequently involves social engineering techniques, such as posing as a trusted source (ex: Impersonation) and/or creating a sense of urgency or alarm for the recipient. All forms of phishing are electronically delivered social engineering. In this scenario, adversaries are not directly sending malware to a victim vice relying on User Execution for delivery and execution. For example, victims may receive phishing messages that instruct them to call a phone number where they are directed to visit a malicious URL, download malware, or install adversary-accessible remote management tools (Remote Access Tools) onto their computer. Adversaries may also combine voice phishing with Multi-Factor Authentication Request Generation in order to trick users into divulging MFA credentials or accepting authentication prompts.

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
- T1566.004: https://attack.mitre.org/techniques/T1566/004
- Reviewed: 2026-10-27
