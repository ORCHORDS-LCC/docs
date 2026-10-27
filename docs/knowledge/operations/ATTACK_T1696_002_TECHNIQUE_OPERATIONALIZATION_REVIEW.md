# Avoid CAPTCHA Technique Operationalization Review

## Reference

- Technique: **T1696.002 — Avoid CAPTCHA**

Adversaries may avoid CAPTCHA challenges by mimicking human behavior. Automation tests, such as CAPTCHA, are typically used by defenders to detect and prevent bot and spam traffic from accessing protected webpages. CAPTCHAs are often placed before login screens or form fields. Traditional CAPTCHAs ask the user to decipher a string of characters, type the characters into a box, and submit the form. reCAPTCHA asks the user to identify images, click a checkbox, or evaluate the user’s behavior from mouse movement and device cookies. Adversaries may attempt to avoid CAPTCHA challenges by constructing a bot that mimics human behavior through browser automation. The automated browser may mimic a human by Masquerading a Browser Fingerprint and through attributes such as session history, IP reputation, and the use of browser APIs. For example, adversaries may use Selenium browsers to simulate a human user. In the Selenium browsers, JavaScript is injected into the website’s Document Object Model (DOM). The injected script may modify browser attributes such as Audio Context and Voice engines, graphic rendering, installed fonts, and browser navigator objects.

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
- T1696.002: https://attack.mitre.org/techniques/T1696/002
- Reviewed: 2026-10-27
