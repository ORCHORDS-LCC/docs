# C0024 SolarWinds Compromise Outcome Lesson

## Authoritative description

- Technique: **C0024 — SolarWinds Compromise**

The SolarWinds Compromise was a sophisticated supply chain cyber operation conducted by APT29 that was discovered in mid-December 2020. APT29 used customized malware to inject malicious code into the SolarWinds Orion software build process that was later distributed through a normal software update; they also used password spraying, token theft, API abuse, spear phishing, and other supply chain attacks to compromise user accounts and leverage their associated access. Victims of this campaign included government, consulting, technology, telecom, and other organizations in North America, Europe, Asia, and the Middle East. This activity has been labled the StellarParticle campaign in industry reporting. Industry reporting also initially referred to the actors involved in this campaign as UNC2452, NOBELIUM, Dark Halo, and SolarStorm. In April 2021, the US and UK governments attributed the SolarWinds Compromise to Russia's Foreign Intelligence Service (SVR); public statements included citations to APT29, Cozy Bear, and The Dukes. The US government assessed that of the approximately 18,000 affected public and private sector customers of Solar Winds’ Orion product, a much smaller number were compromised by follow-on APT29 activity on their systems.

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
- C0024: https://attack.mitre.org/campaigns/C0024
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
