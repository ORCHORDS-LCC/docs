# Shamoon Technique Operationalization Review

## Reference

- Technique: **S0140 — Shamoon**

Shamoon is wiper malware that was first used by an Iranian group known as the "Cutting Sword of Justice" in 2012. Other versions known as Shamoon 2 and Shamoon 3 were observed in 2016 and 2018. Shamoon has also been seen leveraging RawDisk and Filerase to carry out data wiping tasks. Analysis has linked Shamoon with Kwampirs based on multiple shared artifacts and coding patterns. The term Shamoon is sometimes used to refer to the group using the malware as well as the malware itself.

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
- S0140: https://attack.mitre.org/software/S0140
- Reviewed: 2026-10-27
