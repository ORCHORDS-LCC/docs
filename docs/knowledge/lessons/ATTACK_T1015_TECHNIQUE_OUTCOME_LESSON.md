# T1015 Accessibility Features Mitigation Outcome Lesson

## Authoritative description

- Technique: **T1015 — Accessibility Features Mitigation**

To use this technique remotely, an adversary must use it in conjunction with RDP. Ensure that Network Level Authentication is enabled to force the remote desktop session to authenticate before the session is created and the login screen displayed. It is enabled by default on Windows Vista and later. If possible, use a Remote Desktop Gateway to manage connections and security configuration of RDP within a network. Identify and block potentially malicious software that may be executed by an adversary with this technique by using whitelisting tools, like AppLocker, or Software Restriction Policies where appropriate.

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
- T1015: https://attack.mitre.org/mitigations/T1015
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
