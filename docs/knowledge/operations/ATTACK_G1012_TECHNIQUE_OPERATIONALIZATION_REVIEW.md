# CURIUM Technique Operationalization Review

## Reference

- Technique: **G1012 — CURIUM**

CURIUM is an Iranian threat group, first reported in September 2019 and active since at least July 2018, targeting IT service providers in the Middle East. CURIUM has since invested in building relationships with potential targets via social media over a period of months to establish trust and confidence before sending malware. Security researchers note CURIUM has demonstrated great patience and persistence by chatting with potential targets daily and sending benign files to help lower their security consciousness.

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
- G1012: https://attack.mitre.org/groups/G1012
- Reviewed: 2026-10-27
