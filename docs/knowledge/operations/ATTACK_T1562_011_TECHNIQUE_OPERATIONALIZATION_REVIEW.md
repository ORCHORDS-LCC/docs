# Spoof Security Alerting Technique Operationalization Review

## Reference

- Technique: **T1562.011 — Spoof Security Alerting**

Adversaries may spoof security alerting from tools, presenting false evidence to impair defenders’ awareness of malicious activity. Messages produced by defensive tools contain information about potential security events as well as the functioning status of security software and the system. Security reporting messages are important for monitoring the normal operation of a system and identifying important events that can signal a security incident. Rather than or in addition to Indicator Blocking, an adversary can spoof positive affirmations that security tools are continuing to function even after legitimate security tools have been disabled (e.g., Disable or Modify Tools). An adversary can also present a “healthy” system status even after infection. This can be abused to enable further malicious activity by delaying defender responses. For example, adversaries may show a fake Windows Security GUI and tray icon with a “healthy” system status after Windows Defender and other system tools have been disabled.

## Operationalization review

1. Record the operational scope: which services, environments, and data the technique could affect.
2. Record the runbook that would be executed, and its owner.
3. Record the telemetry the runbook depends on, and whether it is retained long enough to investigate.
4. Record the detection that would surface the technique before or after it has an effect.
5. Record the recovery path, and the evidence that recovery has been rehearsed.
6. Record the residual operational risk where the runbook depends on a manual step.

## Review evidence

- the runbook and its owner;
- the telemetry retention and coverage record;
- the detection mapping;
- the exercise or rehearsal record.

## Limitations

An operationalization review describes the runbook and the evidence around it. It does not claim the technique has been prevented or detected in a live environment.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1562.011: https://attack.mitre.org/techniques/T1562/011
- Reviewed: 2026-10-27
