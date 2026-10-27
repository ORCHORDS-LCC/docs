# Havoc Technique Operationalization Review

## Reference

- Technique: **S1229 — Havoc**

Havoc is an open-source post-exploitation command and control (C2) framework first released on GitHub in October 2022 by C5pider (Paul Ungur), who continues to maintain and develop it with community contributors. Havoc provides a wide range of offensive security capabilities and has been adopted by multiple threat actors to establish and maintain control over compromised systems.

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
- S1229: https://attack.mitre.org/software/S1229
- Reviewed: 2026-10-27
