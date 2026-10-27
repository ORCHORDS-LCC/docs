# AcidRain Technique Operationalization Review

## Reference

- Technique: **S1125 — AcidRain**

AcidRain is an ELF binary targeting modems and routers using MIPS architecture. AcidRain is associated with the ViaSat KA-SAT communication outage that took place during the initial phases of the 2022 full-scale invasion of Ukraine. Analysis indicates overlap with another network device-targeting malware, VPNFilter, associated with Sandworm Team. US and European government sources linked AcidRain to Russian government entities, while Ukrainian government sources linked AcidRain specifically to Sandworm Team.

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
- S1125: https://attack.mitre.org/software/S1125
- Reviewed: 2026-10-27
