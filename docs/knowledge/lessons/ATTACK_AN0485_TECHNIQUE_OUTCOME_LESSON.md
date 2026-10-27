# AN0485 Analytic 0485 Outcome Lesson

## Authoritative description

- Technique: **AN0485 — Analytic 0485**
- Platforms: Linux

On Linux, defenders may observe forged cookie activity as unauthorized modifications to browser cookie databases (e.g., ~/.mozilla/firefox/*/cookies.sqlite, ~/.config/chromium/Default/Cookies) or scripted injection of session tokens. Suspicious usage includes curl/wget commands embedding forged cookies in headers, correlated with abnormal session activity in SaaS or IaaS logs.

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
- AN0485: https://attack.mitre.org/detectionstrategies/DET0171#AN0485
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
