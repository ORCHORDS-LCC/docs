# Steal Application Specific Passwords Technique Response Playbook

## Target technique

**T1697 — Steal Application Specific Passwords**

- Tactics: credential-access
- Platforms: Office Suite, Identity Provider, SaaS

Adversaries may steal Application Specific Passwords (ASPs) to gain access to Valid Accounts, bypassing multifactor authentication (MFA) methods. ASPs are passwords typically used to give third-party applications or legacy devices (which do not support MFA methods) account access. An adversary may socially engineer a user into providing an ASP (using methods like Phishing for Information), generate an ASP for an already compromised account, or obtain an ASP stored on a system. Afterward, adversaries may use the ASP to access Valid Accounts and, in some cases, maintain Persistence, bypassing any form of MFA set on the account.

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
- T1697: https://attack.mitre.org/techniques/T1697
- Reviewed: 2026-10-27
