# Avoid CAPTCHA Technique Engineering Review

## Reference

- Technique: **T1696.002 — Avoid CAPTCHA**

Adversaries may avoid CAPTCHA challenges by mimicking human behavior. Automation tests, such as CAPTCHA, are typically used by defenders to detect and prevent bot and spam traffic from accessing protected webpages. CAPTCHAs are often placed before login screens or form fields. Traditional CAPTCHAs ask the user to decipher a string of characters, type the characters into a box, and submit the form. reCAPTCHA asks the user to identify images, click a checkbox, or evaluate the user’s behavior from mouse movement and device cookies. Adversaries may attempt to avoid CAPTCHA challenges by constructing a bot that mimics human behavior through browser automation. The automated browser may mimic a human by Masquerading a Browser Fingerprint and through attributes such as session history, IP reputation, and the use of browser APIs. For example, adversaries may use Selenium browsers to simulate a human user. In the Selenium browsers, JavaScript is injected into the website’s Document Object Model (DOM). The injected script may modify browser attributes such as Audio Context and Voice engines, graphic rendering, installed fonts, and browser navigator objects.

## Engineering review

1. Identify the engineering boundary where the technique would apply: the component, the service, or the deployment.
2. Review the design decision that would prevent the technique, and record the alternative considered.
3. Review the implementation evidence for the preventive control.
4. Review the test coverage that would fail if the control regressed.
5. Review the observability: which signal would show the control is not operating.
6. Record the residual risk where prevention is not achievable, and the detection that compensates.

## Review evidence

- the design record for the preventive decision;
- the implementation or configuration evidence;
- the test record showing the control is exercised;
- the observability mapping.

## Limitations

An engineering review describes what the design and the implementation evidence show. It does not claim the technique has been addressed in production.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1696.002: https://attack.mitre.org/techniques/T1696/002
- Reviewed: 2026-10-27
