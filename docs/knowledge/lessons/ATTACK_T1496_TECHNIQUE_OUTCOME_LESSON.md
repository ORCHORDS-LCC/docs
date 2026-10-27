# T1496 Resource Hijacking Outcome Lesson

## Authoritative description

- Technique: **T1496 — Resource Hijacking**
- Tactics: impact
- Platforms: Windows, IaaS, Linux, macOS, Containers, SaaS

Adversaries may leverage the resources of co-opted systems to complete resource-intensive tasks, which may impact system and/or hosted service availability. Resource hijacking may take a number of different forms. For example, adversaries may: * Leverage compute resources in order to mine cryptocurrency * Sell network bandwidth to proxy networks * Generate SMS traffic for profit * Abuse cloud-based messaging services to send large quantities of spam messages In some cases, adversaries may leverage multiple types of Resource Hijacking at once.

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
- T1496: https://attack.mitre.org/techniques/T1496
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
