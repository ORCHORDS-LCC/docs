# Water Galura Technique Operationalization Review

## Reference

- Technique: **G1050 — Water Galura**

Water Galura are the operators of the Qilin Ransomware-as-a-Service (RaaS) who handle payload generation, ransom negotiations, and the publication of stolen data for Qilin affilates recruited on Russian cybercrime forums. Water Galura have been active since at least 2022 and use a double extortion model where they demand payment for providing decryption keys and for refraining from publishing the stolen data to their leak site.

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
- G1050: https://attack.mitre.org/groups/G1050
- Reviewed: 2026-10-27
