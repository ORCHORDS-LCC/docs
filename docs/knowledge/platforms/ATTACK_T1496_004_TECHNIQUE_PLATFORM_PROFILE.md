# Cloud Service Hijacking Technique Platform Profile

## Reference

- Technique: **T1496.004 — Cloud Service Hijacking**
- Platforms named in the source: SaaS

Adversaries may leverage compromised software-as-a-service (SaaS) applications to complete resource-intensive tasks, which may impact hosted service availability. For example, adversaries may leverage email and messaging services, such as AWS Simple Email Service (SES), AWS Simple Notification Service (SNS), SendGrid, and Twilio, in order to send large quantities of spam / Phishing emails and SMS messages. Alternatively, they may engage in LLMJacking by leveraging reverse proxies to hijack the power of cloud-hosted AI models. In some cases, adversaries may leverage services that the victim is already using. In others, particularly when the service is part of a larger cloud platform, they may first enable the service. Leveraging SaaS applications may cause the victim to incur significant financial costs, use up service quotas, and otherwise impact availability.

## Platform profile

1. Record the platforms in scope and the versions actually deployed.
2. Compare the deployed platform surface against the platforms the source names.
3. Record where the platform provides a native control for the technique, and where it does not.
4. Record the configuration evidence for the native control, where one exists.
5. Record the gap where the platform provides no native control, and the compensating detection.
6. Record the platform version, because platform behaviour changes between versions.

## Evidence

- the platform and version inventory for the scoped estate;
- the configuration export or screenshot for the native control;
- the detection evidence where the platform provides none.

## Limitations

A technique entry describes a class of abuse across platforms. The platform-specific exposure is a property of the deployment, established only by inventory and configuration evidence.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1496.004: https://attack.mitre.org/techniques/T1496/004
- Reviewed: 2026-10-27
