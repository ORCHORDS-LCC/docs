# Analytic 0180 Technique Operationalization Review

## Reference

- Technique: **AN0180 — Analytic 0180**

Behavioral chain: (1) Safari/Chrome/Firefox/Office handles a URL; unified logs show open/click or LSQuarantine assignment, (2) outbound connection to untrusted domain, (3) a new file appears in ~/Downloads or /private/var/folders/* with quarantine flag.

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
- AN0180: https://attack.mitre.org/detectionstrategies/DET0066#AN0180
- Reviewed: 2026-10-27
