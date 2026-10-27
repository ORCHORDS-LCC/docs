# Automate CAPTCHA Completion Technique Response Playbook

## Target technique

**T1696.001 — Automate CAPTCHA Completion**

- Tactics: stealth
- Platforms: SaaS

Adversaries may attempt to use bots to successfully solve CAPTCHA challenges. CAPTCHA challenges are typically used by defenders to detect and prevent bot and spam traffic from accessing protected webpages. CAPTCHAs are automated tests often placed before login screens or form fields. Traditional CAPTCHAs ask the user to decipher a string of characters, type the characters into a box, and submit the form. reCAPTCHA asks the user to identify images, click a checkbox, or evaluate the user’s behavior from mouse movement and device cookies. Adversaries may use scripts or toolkits to automatically solve the CAPTCHA puzzle. For example, adversaries may develop a script that uses the ImageMagick toolkit to solve the CAPTCHA puzzles to then create multiple valid accounts. ImageMagick tool can convert the images into a RGB complemented image. The CAPTCHA challenge may be solved by identifying and comparing attributes of the RGB images to select the expected image. Once the CAPTCHA challenge is solved, the adversary’s script may access the protected page. After accessing the protected the page, the adversary may submit valid forms to the target.

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
- T1696.001: https://attack.mitre.org/techniques/T1696/001
- Reviewed: 2026-10-27
