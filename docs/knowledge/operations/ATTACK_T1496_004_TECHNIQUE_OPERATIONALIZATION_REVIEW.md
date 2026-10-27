# Cloud Service Hijacking Technique Operationalization Review

## Reference

- Technique: **T1496.004 — Cloud Service Hijacking**

Adversaries may leverage compromised software-as-a-service (SaaS) applications to complete resource-intensive tasks, which may impact hosted service availability. For example, adversaries may leverage email and messaging services, such as AWS Simple Email Service (SES), AWS Simple Notification Service (SNS), SendGrid, and Twilio, in order to send large quantities of spam / Phishing emails and SMS messages. Alternatively, they may engage in LLMJacking by leveraging reverse proxies to hijack the power of cloud-hosted AI models. In some cases, adversaries may leverage services that the victim is already using. In others, particularly when the service is part of a larger cloud platform, they may first enable the service. Leveraging SaaS applications may cause the victim to incur significant financial costs, use up service quotas, and otherwise impact availability.

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
- T1496.004: https://attack.mitre.org/techniques/T1496/004
- Reviewed: 2026-10-27
