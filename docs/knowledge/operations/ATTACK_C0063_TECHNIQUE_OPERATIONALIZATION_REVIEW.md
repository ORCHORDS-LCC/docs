# 2025 Poland Wiper Attacks Technique Operationalization Review

## Reference

- Technique: **C0063 — 2025 Poland Wiper Attacks**

2025 Poland Wiper Attacks is a Russian state-sponsored campaign that conducted destructive cyberattacks against Polish energy infrastructure in December 2025. Targets included more than 30 wind and photovoltaic farms, a combined heat and power (CHP) plant, and a manufacturing sector company. The attacks on the distributed energy resources (DER) disrupted communications between affected facilities and the distribution system operator, but did not impact electricity generation or heat supply. Across the campaign, threat actors deployed two previously undocumented wiper tools, DynoWiper, a Windows-based wiper and LazyWiper, a PowerShell wiper, distributed via malicious Group Policy Objects. At the CHP plant, threat actors had maintained access since at least March 2025, using that foothold to obtain credentials and move laterally before attempting wiper deployment. Some reporting has assessed the activity to be consistent with Russian Federal Security Service (FSB) threat activity group Dragonfly, also tracked as STATIC TUNDRA, while other reporting attributes the destructive wiper activities to the Russian General Staff Main Intelligence Directorate (GRU) threat activity group ELECTRUM, also tracked as Sandworm Team.

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
- C0063: https://attack.mitre.org/campaigns/C0063
- Reviewed: 2026-10-27
