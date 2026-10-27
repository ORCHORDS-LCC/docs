# BOLDMOVE Technique Operationalization Review

## Reference

- Technique: **S1184 — BOLDMOVE**

BOLDMOVE is a type of backdoor malware written in C linked to People’s Republic of China operations from 2022 through 2023. BOLDMOVE includes both Windows and Linux variants, with some Linux variants specifically designed for FortiGate Firewall devices. BOLDMOVE is linked to zero-day exploitation of CVE-2022-42475 in FortiOSS SSL-VPNs. The record for BOLDMOVE only covers known Linux variants.

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
- S1184: https://attack.mitre.org/software/S1184
- Reviewed: 2026-10-27
