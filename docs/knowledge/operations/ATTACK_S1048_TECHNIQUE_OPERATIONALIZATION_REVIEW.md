# macOS.OSAMiner Technique Operationalization Review

## Reference

- Technique: **S1048 — macOS.OSAMiner**

MacOS.OSAMiner is a Monero mining trojan that was first observed in 2018; security researchers assessed macOS.OSAMiner may have been circulating since at least 2015. macOS.OSAMiner is known for embedding one run-only AppleScript into another, which helped the malware evade full analysis for five years due to a lack of Apple event (AEVT) analysis tools.

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
- S1048: https://attack.mitre.org/software/S1048
- Reviewed: 2026-10-27
