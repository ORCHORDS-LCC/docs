# C0063 2025 Poland Wiper Attacks Outcome Lesson

## Authoritative description

- Technique: **C0063 — 2025 Poland Wiper Attacks**

2025 Poland Wiper Attacks is a Russian state-sponsored campaign that conducted destructive cyberattacks against Polish energy infrastructure in December 2025. Targets included more than 30 wind and photovoltaic farms, a combined heat and power (CHP) plant, and a manufacturing sector company. The attacks on the distributed energy resources (DER) disrupted communications between affected facilities and the distribution system operator, but did not impact electricity generation or heat supply. Across the campaign, threat actors deployed two previously undocumented wiper tools, DynoWiper, a Windows-based wiper and LazyWiper, a PowerShell wiper, distributed via malicious Group Policy Objects. At the CHP plant, threat actors had maintained access since at least March 2025, using that foothold to obtain credentials and move laterally before attempting wiper deployment. Some reporting has assessed the activity to be consistent with Russian Federal Security Service (FSB) threat activity group Dragonfly, also tracked as STATIC TUNDRA, while other reporting attributes the destructive wiper activities to the Russian General Staff Main Intelligence Directorate (GRU) threat activity group ELECTRUM, also tracked as Sandworm Team.

## Reusable lesson

This technique should be treated as an explicit review question when it is relevant to the system or organisation, rather than assumed to be covered by a generic control statement or by tooling that reports a related signal.

## Apply the lesson

1. Define the real scope before judging coverage.
2. Inspect current technical, process, governance, or operational evidence.
3. Separate documented intent from verified behaviour.
4. Record partial coverage and unresolved gaps instead of converting them into a pass.
5. Revisit when the underlying scope, threat environment, technology, suppliers, or mission materially changes.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- C0063: https://attack.mitre.org/campaigns/C0063
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
