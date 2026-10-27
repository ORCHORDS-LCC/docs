# T1562.011 Spoof Security Alerting Outcome Lesson

## Authoritative description

- Technique: **T1562.011 — Spoof Security Alerting**
- Tactics: stealth
- Platforms: Windows, macOS, Linux

Adversaries may spoof security alerting from tools, presenting false evidence to impair defenders’ awareness of malicious activity. Messages produced by defensive tools contain information about potential security events as well as the functioning status of security software and the system. Security reporting messages are important for monitoring the normal operation of a system and identifying important events that can signal a security incident. Rather than or in addition to Indicator Blocking, an adversary can spoof positive affirmations that security tools are continuing to function even after legitimate security tools have been disabled (e.g., Disable or Modify Tools). An adversary can also present a “healthy” system status even after infection. This can be abused to enable further malicious activity by delaying defender responses. For example, adversaries may show a fake Windows Security GUI and tray icon with a “healthy” system status after Windows Defender and other system tools have been disabled.

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
- T1562.011: https://attack.mitre.org/techniques/T1562/011
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
