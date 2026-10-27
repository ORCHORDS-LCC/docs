# 2025 Poland Wiper Attacks Technique Response Playbook

## Target technique

**C0063 — 2025 Poland Wiper Attacks**


2025 Poland Wiper Attacks is a Russian state-sponsored campaign that conducted destructive cyberattacks against Polish energy infrastructure in December 2025. Targets included more than 30 wind and photovoltaic farms, a combined heat and power (CHP) plant, and a manufacturing sector company. The attacks on the distributed energy resources (DER) disrupted communications between affected facilities and the distribution system operator, but did not impact electricity generation or heat supply. Across the campaign, threat actors deployed two previously undocumented wiper tools, DynoWiper, a Windows-based wiper and LazyWiper, a PowerShell wiper, distributed via malicious Group Policy Objects. At the CHP plant, threat actors had maintained access since at least March 2025, using that foothold to obtain credentials and move laterally before attempting wiper deployment. Some reporting has assessed the activity to be consistent with Russian Federal Security Service (FSB) threat activity group Dragonfly, also tracked as STATIC TUNDRA, while other reporting attributes the destructive wiper activities to the Russian General Staff Main Intelligence Directorate (GRU) threat activity group ELECTRUM, also tracked as Sandworm Team.

## Preconditions

- the estate in scope is identified, with the systems the technique could apply to;
- an owner is accountable for detection and response;
- current telemetry and configuration can be inspected;
- the technique is applicable or requires an applicability decision.

## Procedure

1. Confirm the scope and owner.
2. Read the current technique description and the associated detection guidance.
3. Inventory the telemetry that would carry the technique's indicators.
4. Inspect whether the indicators are present in the environment.
5. Exercise the detection path and confirm it produces the expected signal.
6. Record gaps in detection coverage and assign remediation owners.
7. Record justified non-applicability or accepted detection gaps separately.
8. Set the next event-driven or periodic verification trigger.

## Failure handling

If the detection path does not produce the expected signal, treat the coverage as unverified, preserve the test evidence, and route the gap through the appropriate remediation or risk process.

## Completion evidence

Scope, owner, source version, telemetry inspected, tests performed, findings, exceptions, remediation links, reviewer, and next trigger.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- C0063: https://attack.mitre.org/campaigns/C0063
- Reviewed: 2026-10-27
