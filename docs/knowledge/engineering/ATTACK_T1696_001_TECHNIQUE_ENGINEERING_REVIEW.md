# Automate CAPTCHA Completion Technique Engineering Review

## Reference

- Technique: **T1696.001 — Automate CAPTCHA Completion**

Adversaries may attempt to use bots to successfully solve CAPTCHA challenges. CAPTCHA challenges are typically used by defenders to detect and prevent bot and spam traffic from accessing protected webpages. CAPTCHAs are automated tests often placed before login screens or form fields. Traditional CAPTCHAs ask the user to decipher a string of characters, type the characters into a box, and submit the form. reCAPTCHA asks the user to identify images, click a checkbox, or evaluate the user’s behavior from mouse movement and device cookies. Adversaries may use scripts or toolkits to automatically solve the CAPTCHA puzzle. For example, adversaries may develop a script that uses the ImageMagick toolkit to solve the CAPTCHA puzzles to then create multiple valid accounts. ImageMagick tool can convert the images into a RGB complemented image. The CAPTCHA challenge may be solved by identifying and comparing attributes of the RGB images to select the expected image. Once the CAPTCHA challenge is solved, the adversary’s script may access the protected page. After accessing the protected the page, the adversary may submit valid forms to the target.

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
- T1696.001: https://attack.mitre.org/techniques/T1696/001
- Reviewed: 2026-10-27
