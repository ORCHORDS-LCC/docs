# SMS Pumping Technique Platform Profile

## Reference

- Technique: **T1496.003 — SMS Pumping**
- Platforms named in the source: SaaS

Adversaries may leverage messaging services for SMS pumping, which may impact system and/or hosted service availability. SMS pumping is a type of telecommunications fraud whereby a threat actor first obtains a set of phone numbers from a telecommunications provider, then leverages a victim’s messaging infrastructure to send large amounts of SMS messages to numbers in that set. By generating SMS traffic to their phone number set, a threat actor may earn payments from the telecommunications provider. Threat actors often use publicly available web forms, such as one-time password (OTP) or account verification fields, in order to generate SMS traffic. These fields may leverage services such as Twilio, AWS SNS, and Amazon Cognito in the background. In response to the large quantity of requests, SMS costs may increase and communication channels may become overwhelmed.

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
- T1496.003: https://attack.mitre.org/techniques/T1496/003
- Reviewed: 2026-10-27
