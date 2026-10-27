# Anti-Automation Evasion Technique Operationalization Review

## Reference

- Technique: **T1696 — Anti-Automation Evasion**

Adversaries may employ various means to evade or complete automation checks. Automation checks distinguish human users from bot traffic and prevent bots from reaching the web pages protected by automation checks. For example, a user may be required to solve a CAPTCHA challenge before accessing a form or login page. Traditional CAPTCHAs ask the user to decipher a string of characters, type the characters into a box, and submit the form. reCAPTCHA asks the user to identify images, click a checkbox, or evaluate the user’s behavior from mouse movement and device cookies. Adversaries may pay for a service that forwards the CAPTCHA challenge to a remote human worker. The human service then solves the CAPTCHA on behalf of the bot. AI tools, such as CapSolver, can also be used to automatically solve CAPTCHA challenges.

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
- T1696: https://attack.mitre.org/techniques/T1696
- Reviewed: 2026-10-27
