# AN2024 Analytic 2024 Outcome Lesson

## Authoritative description

- Technique: **AN2024 — Analytic 2024**
- Platforms: PRE

Monitor logged domain name system (DNS) data for purchased domains that can be used during targeting. Reputation/category-based detection may be difficult until the categorization is updated. Detection efforts may be focused on related stages of the adversary lifecycle, such as during Initial Access and Command and Control. Domain registration information is, by design, captured in public registration logs. Consider use of services that may aid in tracking of newly acquired domains, such as WHOIS databases and/or passive DNS. In some cases it may be possible to pivot on known pieces of domain registration information to uncover other infrastructure purchased by the adversary. Consider monitoring for domains created with a similar structure to your own, including under a different TLD. Though various tools and services exist to track, query, and monitor domain name registration information, tracking across multiple DNS infrastructures can require multiple tools/services or more advanced analytics. Detection efforts may be focused on related stages of the adversary lifecycle, such as during Initial Access and Command and Control. Monitor queried domain name system (DNS) registry data for purchased domains that can be used during targeting. Reputation/category-based detection may be difficult until the categorization is updated. Detection efforts may be focused on related stages of the adversary lifecycle, such as during Initial Access and Command and Control.

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
- AN2024: https://attack.mitre.org/detectionstrategies/DET0892#AN2024
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
