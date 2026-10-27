# Dridex Technique Operationalization Review

## Reference

- Technique: **S0384 — Dridex**

Dridex is a prolific banking Trojan that first appeared in 2014. By December 2019, the US Treasury estimated Dridex had infected computers in hundreds of banks and financial institutions in over 40 countries, leading to more than $100 million in theft. Dridex was created from the source code of the Bugat banking Trojan (also known as Cridex).

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
- S0384: https://attack.mitre.org/software/S0384
- Reviewed: 2026-10-27
