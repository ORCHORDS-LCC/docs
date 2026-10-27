# Disable or Modify Cloud Log Technique Operationalization Review

## Reference

- Technique: **T1685.002 — Disable or Modify Cloud Log**

An adversary may disable or modify cloud logging capabilities and integrations to limit what data is collected on their activities and avoid detection. Cloud environments allow for collection and analysis of audit and application logs that provide insight into what activities a user does within the environment. If an adversary has sufficient permissions, they can disable or modify logging to avoid detection of their activities. For example, in AWS an adversary may disable CloudWatch/CloudTrail integrations prior to conducting further malicious activity. They may alternatively tamper with logging functionality, for example, by removing any associated SNS topics, disabling multi-region logging, or disabling settings that validate and/or encrypt log files. In Office 365, an adversary may disable logging on mail collection activities for specific users by using the Set-MailboxAuditBypassAssociation cmdlet, by disabling M365 Advanced Auditing for the user, or by downgrading the user’s license from an Enterprise E5 to an Enterprise E3 license.

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
- T1685.002: https://attack.mitre.org/techniques/T1685/002
- Reviewed: 2026-10-27
