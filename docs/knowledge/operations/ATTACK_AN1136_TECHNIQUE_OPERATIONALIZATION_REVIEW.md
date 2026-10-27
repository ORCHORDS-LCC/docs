# Analytic 1136 Technique Operationalization Review

## Reference

- Technique: **AN1136 — Analytic 1136**

Abuse of extended attributes (xattrs) to hide payloads in com.apple.* or custom keys. Defender perspective: monitor suspicious use of xattr command with -w (write) and -p (print) flags, especially when followed by execution of interpreters like bash, Python, or osascript. Behavior chain includes: (1) suspicious file modification with new com.apple.* attributes, (2) attribute content inconsistent with expected metadata tags (e.g., high entropy), (3) subsequent process execution correlated with extraction of the attribute.

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
- AN1136: https://attack.mitre.org/detectionstrategies/DET0406#AN1136
- Reviewed: 2026-10-27
