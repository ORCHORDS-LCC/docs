# T1696 Anti-Automation Evasion Outcome Lesson

## Authoritative description

- Technique: **T1696 — Anti-Automation Evasion**
- Tactics: stealth
- Platforms: SaaS

Adversaries may employ various means to evade or complete automation checks. Automation checks distinguish human users from bot traffic and prevent bots from reaching the web pages protected by automation checks. For example, a user may be required to solve a CAPTCHA challenge before accessing a form or login page. Traditional CAPTCHAs ask the user to decipher a string of characters, type the characters into a box, and submit the form. reCAPTCHA asks the user to identify images, click a checkbox, or evaluate the user’s behavior from mouse movement and device cookies. Adversaries may pay for a service that forwards the CAPTCHA challenge to a remote human worker. The human service then solves the CAPTCHA on behalf of the bot. AI tools, such as CapSolver, can also be used to automatically solve CAPTCHA challenges.

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
- T1696: https://attack.mitre.org/techniques/T1696
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
