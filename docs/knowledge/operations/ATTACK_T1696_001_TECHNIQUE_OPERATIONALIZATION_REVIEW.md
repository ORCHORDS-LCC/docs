# Automate CAPTCHA Completion Technique Operationalization Review

## Reference

- Technique: **T1696.001 — Automate CAPTCHA Completion**

Adversaries may attempt to use bots to successfully solve CAPTCHA challenges. CAPTCHA challenges are typically used by defenders to detect and prevent bot and spam traffic from accessing protected webpages. CAPTCHAs are automated tests often placed before login screens or form fields. Traditional CAPTCHAs ask the user to decipher a string of characters, type the characters into a box, and submit the form. reCAPTCHA asks the user to identify images, click a checkbox, or evaluate the user’s behavior from mouse movement and device cookies. Adversaries may use scripts or toolkits to automatically solve the CAPTCHA puzzle. For example, adversaries may develop a script that uses the ImageMagick toolkit to solve the CAPTCHA puzzles to then create multiple valid accounts. ImageMagick tool can convert the images into a RGB complemented image. The CAPTCHA challenge may be solved by identifying and comparing attributes of the RGB images to select the expected image. Once the CAPTCHA challenge is solved, the adversary’s script may access the protected page. After accessing the protected the page, the adversary may submit valid forms to the target.

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
- T1696.001: https://attack.mitre.org/techniques/T1696/001
- Reviewed: 2026-10-27
