# VPNFilter Technique Operationalization Review

## Reference

- Technique: **S1010 — VPNFilter**

VPNFilter is a multi-stage, modular platform with versatile capabilities to support both intelligence-collection and destructive cyber attack operations. VPNFilter modules such as its packet sniffer ('ps') can collect traffic that passes through an infected device, allowing the theft of website credentials and monitoring of Modbus SCADA protocols. VPNFilter was assessed to be replaced by Sandworm Team with Cyclops Blink starting in 2019.

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
- S1010: https://attack.mitre.org/software/S1010
- Reviewed: 2026-10-27
