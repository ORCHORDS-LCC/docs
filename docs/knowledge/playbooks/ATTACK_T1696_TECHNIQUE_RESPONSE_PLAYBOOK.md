# Anti-Automation Evasion Technique Response Playbook

## Target technique

**T1696 — Anti-Automation Evasion**

- Tactics: stealth
- Platforms: SaaS

Adversaries may employ various means to evade or complete automation checks. Automation checks distinguish human users from bot traffic and prevent bots from reaching the web pages protected by automation checks. For example, a user may be required to solve a CAPTCHA challenge before accessing a form or login page. Traditional CAPTCHAs ask the user to decipher a string of characters, type the characters into a box, and submit the form. reCAPTCHA asks the user to identify images, click a checkbox, or evaluate the user’s behavior from mouse movement and device cookies. Adversaries may pay for a service that forwards the CAPTCHA challenge to a remote human worker. The human service then solves the CAPTCHA on behalf of the bot. AI tools, such as CapSolver, can also be used to automatically solve CAPTCHA challenges.

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
- T1696: https://attack.mitre.org/techniques/T1696
- Reviewed: 2026-10-27
