# SLOTHFULMEDIA Technique Operationalization Review

## Reference

- Technique: **S0533 — SLOTHFULMEDIA**

SLOTHFULMEDIA is a remote access Trojan written in C++ that has been used by an unidentified "sophisticated cyber actor" since at least January 2017. It has been used to target government organizations, defense contractors, universities, and energy companies in Russia, India, Kazakhstan, Kyrgyzstan, Malaysia, Ukraine, and Eastern Europe. In October 2020, Kaspersky Labs assessed SLOTHFULMEDIA is part of an activity cluster it refers to as "IAmTheKing". ESET also noted code similarity between SLOTHFULMEDIA and droppers used by a group it refers to as "PowerPool".

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
- S0533: https://attack.mitre.org/software/S0533
- Reviewed: 2026-10-27
