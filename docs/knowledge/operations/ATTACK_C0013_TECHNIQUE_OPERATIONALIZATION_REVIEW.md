# Operation Sharpshooter Technique Operationalization Review

## Reference

- Technique: **C0013 — Operation Sharpshooter**

Operation Sharpshooter was a global cyber espionage campaign that targeted nuclear, defense, government, energy, and financial companies, with many located in Germany, Turkey, the United Kingdom, and the United States. Security researchers noted the campaign shared many similarities with previous Lazarus Group operations, including fake job recruitment lures and shared malware code.

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
- C0013: https://attack.mitre.org/campaigns/C0013
- Reviewed: 2026-10-27
