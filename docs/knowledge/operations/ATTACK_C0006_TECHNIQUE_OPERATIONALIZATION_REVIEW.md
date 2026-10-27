# Operation Honeybee Technique Operationalization Review

## Reference

- Technique: **C0006 — Operation Honeybee**

Operation Honeybee was a campaign that targeted humanitarian aid and inter-Korean affairs organizations from at least late 2017 through early 2018. Operation Honeybee initially targeted South Korea, but expanded to include Vietnam, Singapore, Japan, Indonesia, Argentina, and Canada. Security researchers assessed the threat actors were likely Korean speakers based on metadata used in both lure documents and executables, and named the campaign "Honeybee" after the author name discovered in malicious Word documents.

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
- C0006: https://attack.mitre.org/campaigns/C0006
- Reviewed: 2026-10-27
