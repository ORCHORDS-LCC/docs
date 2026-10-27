# Avoid CAPTCHA Technique Response Playbook

## Target technique

**T1696.002 — Avoid CAPTCHA**

- Tactics: stealth
- Platforms: SaaS

Adversaries may avoid CAPTCHA challenges by mimicking human behavior. Automation tests, such as CAPTCHA, are typically used by defenders to detect and prevent bot and spam traffic from accessing protected webpages. CAPTCHAs are often placed before login screens or form fields. Traditional CAPTCHAs ask the user to decipher a string of characters, type the characters into a box, and submit the form. reCAPTCHA asks the user to identify images, click a checkbox, or evaluate the user’s behavior from mouse movement and device cookies. Adversaries may attempt to avoid CAPTCHA challenges by constructing a bot that mimics human behavior through browser automation. The automated browser may mimic a human by Masquerading a Browser Fingerprint and through attributes such as session history, IP reputation, and the use of browser APIs. For example, adversaries may use Selenium browsers to simulate a human user. In the Selenium browsers, JavaScript is injected into the website’s Document Object Model (DOM). The injected script may modify browser attributes such as Audio Context and Voice engines, graphic rendering, installed fonts, and browser navigator objects.

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
- T1696.002: https://attack.mitre.org/techniques/T1696/002
- Reviewed: 2026-10-27
