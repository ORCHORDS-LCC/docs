# AcidPour Technique Operationalization Review

## Reference

- Technique: **S1167 — AcidPour**

AcidPour is a variant of AcidRain designed to impact a wider range of x86 architecture Linux devices. AcidPour is an x86 ELF binary that expands on the targeted devices and locations in AcidRain by including items such as Unsorted Block Image (UBI), Deice Mapper (DM), and various flash memory references. Based on this expanded targeting, AcidPour can impact a variety of device types including IoT, networking, and ICS embedded device types. AcidPour is a wiping payload associated with the Sandworm Team threat actor, and potentially linked to attacks against Ukrainian internet service providers (ISPs) in 2023.

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
- S1167: https://attack.mitre.org/software/S1167
- Reviewed: 2026-10-27
