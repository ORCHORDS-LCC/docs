# T1685.003 Modify or Spoof Tool UI Outcome Lesson

## Authoritative description

- Technique: **T1685.003 — Modify or Spoof Tool UI**
- Tactics: defense-impairment
- Platforms: Linux, macOS, Windows

Adversaries may spoof or manipulate security tool user interfaces (UIs) to falsely indicate tools are functioning normally and delay detection and response. Adversaries may present misleading or falsified security tool interfaces (UIs) that display normal or healthy status indicators, even when underlying security tools have been disabled, degraded, or otherwise tampered with. Security tools typically provide visibility into system health, alerting, and operational status; by misrepresenting this information, adversaries can undermine defender trust in these signals and obscure the true security posture of the system. This behavior is often used in conjunction with efforts to disable or modify tools, where adversaries first impair the functionality of defenses (e.g., EDR, logging agents) and then replace or mimic their interfaces to conceal the loss of visibility. By maintaining the appearance of normal operations, such as showing active protection, successful updates, or absence of threats, adversaries can delay investigation and response, enabling continued malicious activity. For example, adversaries may display a fake Windows Security interface or system tray icon indicating a “protected” or “healthy” state after disabling Windows Defender or related services.

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
- T1685.003: https://attack.mitre.org/techniques/T1685/003
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
