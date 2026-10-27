# T1110 Brute Force Mitigation Outcome Lesson

## Authoritative description

- Technique: **T1110 — Brute Force Mitigation**

Set account lockout policies after a certain number of failed login attempts to prevent passwords from being guessed. Too strict a policy can create a denial of service condition and render environments un-usable, with all accounts being locked-out permanently. Use multifactor authentication. Follow best practices for mitigating access to Valid Accounts Refer to NIST guidelines when creating passwords. Where possible, also enable multi factor authentication on external facing services.

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
- T1110: https://attack.mitre.org/mitigations/T1110
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
