# Disable or Modify Cloud Log Technique Response Playbook

## Target technique

**T1685.002 — Disable or Modify Cloud Log**

- Tactics: defense-impairment
- Platforms: IaaS, SaaS, Identity Provider, Office Suite

An adversary may disable or modify cloud logging capabilities and integrations to limit what data is collected on their activities and avoid detection. Cloud environments allow for collection and analysis of audit and application logs that provide insight into what activities a user does within the environment. If an adversary has sufficient permissions, they can disable or modify logging to avoid detection of their activities. For example, in AWS an adversary may disable CloudWatch/CloudTrail integrations prior to conducting further malicious activity. They may alternatively tamper with logging functionality, for example, by removing any associated SNS topics, disabling multi-region logging, or disabling settings that validate and/or encrypt log files. In Office 365, an adversary may disable logging on mail collection activities for specific users by using the Set-MailboxAuditBypassAssociation cmdlet, by disabling M365 Advanced Auditing for the user, or by downgrading the user’s license from an Enterprise E5 to an Enterprise E3 license.

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
- T1685.002: https://attack.mitre.org/techniques/T1685/002
- Reviewed: 2026-10-27
