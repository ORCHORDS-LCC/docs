# Analytic 1242 Technique Operationalization Review

## Reference

- Technique: **AN1242 — Analytic 1242**

Detection focuses on abnormal or unauthorized cloud instance creation events. From a defender’s perspective, suspicious behavior includes VM/instance creation by rarely used or newly created accounts, creation events from unusual geolocations, or rapid sequences of snapshot creation followed by instance creation and mounting. Unexpected network or IAM policy changes applied to new instances can indicate adversarial use rather than legitimate provisioning.

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
- AN1242: https://attack.mitre.org/detectionstrategies/DET0449#AN1242
- Reviewed: 2026-10-27
