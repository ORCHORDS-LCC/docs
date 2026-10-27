# Analytic 2104 Technique Operationalization Review

## Reference

- Technique: **AN2104 — Analytic 2104**

Successful CAPTCHA completion does not expose whether the challenge was solved manually, through automated tooling, through an AI-enabled solver, or through a third-party human-solving service. Providers may independently classify associated sessions as automated or bot-like, but this identifies suspicious automation rather than the method used to complete the CAPTCHA.

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
- AN2104: https://attack.mitre.org/detectionstrategies/DET0937#AN2104
- Reviewed: 2026-10-27
