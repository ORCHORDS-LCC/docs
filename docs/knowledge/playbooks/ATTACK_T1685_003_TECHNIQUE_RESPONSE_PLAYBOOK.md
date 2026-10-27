# Modify or Spoof Tool UI Technique Response Playbook

## Target technique

**T1685.003 — Modify or Spoof Tool UI**

- Tactics: defense-impairment
- Platforms: Linux, macOS, Windows

Adversaries may spoof or manipulate security tool user interfaces (UIs) to falsely indicate tools are functioning normally and delay detection and response. Adversaries may present misleading or falsified security tool interfaces (UIs) that display normal or healthy status indicators, even when underlying security tools have been disabled, degraded, or otherwise tampered with. Security tools typically provide visibility into system health, alerting, and operational status; by misrepresenting this information, adversaries can undermine defender trust in these signals and obscure the true security posture of the system. This behavior is often used in conjunction with efforts to disable or modify tools, where adversaries first impair the functionality of defenses (e.g., EDR, logging agents) and then replace or mimic their interfaces to conceal the loss of visibility. By maintaining the appearance of normal operations, such as showing active protection, successful updates, or absence of threats, adversaries can delay investigation and response, enabling continued malicious activity. For example, adversaries may display a fake Windows Security interface or system tray icon indicating a “protected” or “healthy” state after disabling Windows Defender or related services.

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
- T1685.003: https://attack.mitre.org/techniques/T1685/003
- Reviewed: 2026-10-27
