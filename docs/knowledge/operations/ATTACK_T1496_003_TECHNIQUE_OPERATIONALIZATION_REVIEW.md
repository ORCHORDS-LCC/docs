# SMS Pumping Technique Operationalization Review

## Reference

- Technique: **T1496.003 — SMS Pumping**

Adversaries may leverage messaging services for SMS pumping, which may impact system and/or hosted service availability. SMS pumping is a type of telecommunications fraud whereby a threat actor first obtains a set of phone numbers from a telecommunications provider, then leverages a victim’s messaging infrastructure to send large amounts of SMS messages to numbers in that set. By generating SMS traffic to their phone number set, a threat actor may earn payments from the telecommunications provider. Threat actors often use publicly available web forms, such as one-time password (OTP) or account verification fields, in order to generate SMS traffic. These fields may leverage services such as Twilio, AWS SNS, and Amazon Cognito in the background. In response to the large quantity of requests, SMS costs may increase and communication channels may become overwhelmed.

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
- T1496.003: https://attack.mitre.org/techniques/T1496/003
- Reviewed: 2026-10-27
