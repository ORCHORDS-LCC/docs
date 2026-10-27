# Night Dragon Technique Operationalization Review

## Reference

- Technique: **C0002 — Night Dragon**

Night Dragon was a cyber espionage campaign that targeted oil, energy, and petrochemical companies, along with individuals and executives in Kazakhstan, Taiwan, Greece, and the United States. The unidentified threat actors searched for information related to oil and gas field production systems, financials, and collected data from SCADA systems. Based on the observed techniques, tools, and network activities, security researchers assessed the campaign involved a threat group based in China.

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
- C0002: https://attack.mitre.org/campaigns/C0002
- Reviewed: 2026-10-27
