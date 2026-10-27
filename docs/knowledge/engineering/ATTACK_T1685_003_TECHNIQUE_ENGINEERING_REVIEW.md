# Modify or Spoof Tool UI Technique Engineering Review

## Reference

- Technique: **T1685.003 — Modify or Spoof Tool UI**

Adversaries may spoof or manipulate security tool user interfaces (UIs) to falsely indicate tools are functioning normally and delay detection and response. Adversaries may present misleading or falsified security tool interfaces (UIs) that display normal or healthy status indicators, even when underlying security tools have been disabled, degraded, or otherwise tampered with. Security tools typically provide visibility into system health, alerting, and operational status; by misrepresenting this information, adversaries can undermine defender trust in these signals and obscure the true security posture of the system. This behavior is often used in conjunction with efforts to disable or modify tools, where adversaries first impair the functionality of defenses (e.g., EDR, logging agents) and then replace or mimic their interfaces to conceal the loss of visibility. By maintaining the appearance of normal operations, such as showing active protection, successful updates, or absence of threats, adversaries can delay investigation and response, enabling continued malicious activity. For example, adversaries may display a fake Windows Security interface or system tray icon indicating a “protected” or “healthy” state after disabling Windows Defender or related services.

## Engineering review

1. Identify the engineering boundary where the technique would apply: the component, the service, or the deployment.
2. Review the design decision that would prevent the technique, and record the alternative considered.
3. Review the implementation evidence for the preventive control.
4. Review the test coverage that would fail if the control regressed.
5. Review the observability: which signal would show the control is not operating.
6. Record the residual risk where prevention is not achievable, and the detection that compensates.

## Review evidence

- the design record for the preventive decision;
- the implementation or configuration evidence;
- the test record showing the control is exercised;
- the observability mapping.

## Limitations

An engineering review describes what the design and the implementation evidence show. It does not claim the technique has been addressed in production.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1685.003: https://attack.mitre.org/techniques/T1685/003
- Reviewed: 2026-10-27
