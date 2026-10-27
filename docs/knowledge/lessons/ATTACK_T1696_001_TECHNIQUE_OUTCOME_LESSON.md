# T1696.001 Automate CAPTCHA Completion Outcome Lesson

## Authoritative description

- Technique: **T1696.001 — Automate CAPTCHA Completion**
- Tactics: stealth
- Platforms: SaaS

Adversaries may attempt to use bots to successfully solve CAPTCHA challenges. CAPTCHA challenges are typically used by defenders to detect and prevent bot and spam traffic from accessing protected webpages. CAPTCHAs are automated tests often placed before login screens or form fields. Traditional CAPTCHAs ask the user to decipher a string of characters, type the characters into a box, and submit the form. reCAPTCHA asks the user to identify images, click a checkbox, or evaluate the user’s behavior from mouse movement and device cookies. Adversaries may use scripts or toolkits to automatically solve the CAPTCHA puzzle. For example, adversaries may develop a script that uses the ImageMagick toolkit to solve the CAPTCHA puzzles to then create multiple valid accounts. ImageMagick tool can convert the images into a RGB complemented image. The CAPTCHA challenge may be solved by identifying and comparing attributes of the RGB images to select the expected image. Once the CAPTCHA challenge is solved, the adversary’s script may access the protected page. After accessing the protected the page, the adversary may submit valid forms to the target.

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
- T1696.001: https://attack.mitre.org/techniques/T1696/001
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
