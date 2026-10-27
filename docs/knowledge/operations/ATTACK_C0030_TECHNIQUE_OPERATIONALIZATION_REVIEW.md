# Triton Safety Instrumented System Attack Technique Operationalization Review

## Reference

- Technique: **C0030 — Triton Safety Instrumented System Attack**

Triton Safety Instrumented System Attack was a campaign employed by TEMP.Veles which leveraged the Triton malware framework against a petrochemical organization. The malware and techniques used within this campaign targeted specific Triconex Safety Controllers within the environment. The incident was eventually discovered due to a safety trip that occurred as a result of an issue in the malware.

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
- C0030: https://attack.mitre.org/campaigns/C0030
- Reviewed: 2026-10-27
