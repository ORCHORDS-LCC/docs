# Anti-Automation Evasion Technique Platform Profile

## Reference

- Technique: **T1696 — Anti-Automation Evasion**
- Platforms named in the source: SaaS

Adversaries may employ various means to evade or complete automation checks. Automation checks distinguish human users from bot traffic and prevent bots from reaching the web pages protected by automation checks. For example, a user may be required to solve a CAPTCHA challenge before accessing a form or login page. Traditional CAPTCHAs ask the user to decipher a string of characters, type the characters into a box, and submit the form. reCAPTCHA asks the user to identify images, click a checkbox, or evaluate the user’s behavior from mouse movement and device cookies. Adversaries may pay for a service that forwards the CAPTCHA challenge to a remote human worker. The human service then solves the CAPTCHA on behalf of the bot. AI tools, such as CapSolver, can also be used to automatically solve CAPTCHA challenges.

## Platform profile

1. Record the platforms in scope and the versions actually deployed.
2. Compare the deployed platform surface against the platforms the source names.
3. Record where the platform provides a native control for the technique, and where it does not.
4. Record the configuration evidence for the native control, where one exists.
5. Record the gap where the platform provides no native control, and the compensating detection.
6. Record the platform version, because platform behaviour changes between versions.

## Evidence

- the platform and version inventory for the scoped estate;
- the configuration export or screenshot for the native control;
- the detection evidence where the platform provides none.

## Limitations

A technique entry describes a class of abuse across platforms. The platform-specific exposure is a property of the deployment, established only by inventory and configuration evidence.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1696: https://attack.mitre.org/techniques/T1696
- Reviewed: 2026-10-27
