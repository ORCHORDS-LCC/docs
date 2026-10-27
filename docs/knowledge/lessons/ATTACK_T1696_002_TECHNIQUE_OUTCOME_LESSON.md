# T1696.002 Avoid CAPTCHA Outcome Lesson

## Authoritative description

- Technique: **T1696.002 — Avoid CAPTCHA**
- Tactics: stealth
- Platforms: SaaS

Adversaries may avoid CAPTCHA challenges by mimicking human behavior. Automation tests, such as CAPTCHA, are typically used by defenders to detect and prevent bot and spam traffic from accessing protected webpages. CAPTCHAs are often placed before login screens or form fields. Traditional CAPTCHAs ask the user to decipher a string of characters, type the characters into a box, and submit the form. reCAPTCHA asks the user to identify images, click a checkbox, or evaluate the user’s behavior from mouse movement and device cookies. Adversaries may attempt to avoid CAPTCHA challenges by constructing a bot that mimics human behavior through browser automation. The automated browser may mimic a human by Masquerading a Browser Fingerprint and through attributes such as session history, IP reputation, and the use of browser APIs. For example, adversaries may use Selenium browsers to simulate a human user. In the Selenium browsers, JavaScript is injected into the website’s Document Object Model (DOM). The injected script may modify browser attributes such as Audio Context and Voice engines, graphic rendering, installed fonts, and browser navigator objects.

## Reusable lesson

This technique should be treated as an explicit review question when it is relevant to the system or organisation, rather than assumed to be covered by a generic control statement or by tooling that reports a related signal.

## Apply the lesson

1. Define the real scope before judging coverage.
2. Inspect current technical, process, governance, or operational evidence.
3. Separate documented intent from verified behaviour.
4. Record partial coverage and unresolved gaps instead of converting them into a pass.
5. Revisit when the underlying scope, threat environment, technology, suppliers, or mission materially changes.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1696.002: https://attack.mitre.org/techniques/T1696/002
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
