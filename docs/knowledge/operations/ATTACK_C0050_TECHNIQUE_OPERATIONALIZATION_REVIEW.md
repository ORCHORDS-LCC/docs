# J-magic Campaign Technique Operationalization Review

## Reference

- Technique: **C0050 — J-magic Campaign**

The J-magic Campaign was active from mid-2023 to at least mid-2024 and featured the use of the J-magic backdoor, a custom cd00r variant tailored for use against Juniper routers. The J-magic Campaign targeted Junos OS routers serving as VPN gateways primarily in the semiconductor, energy, manufacturing, and IT sectors.

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
- C0050: https://attack.mitre.org/campaigns/C0050
- Reviewed: 2026-10-27
