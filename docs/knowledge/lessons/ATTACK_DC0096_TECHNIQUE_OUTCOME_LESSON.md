# DC0096 Passive DNS Outcome Lesson

## Authoritative description

- Technique: **DC0096 — Passive DNS**

"Domain Name: Passive DNS" captures logged historical and real-time domain name system (DNS) data. This includes records of domain-to-IP address resolutions over time, enabling analysts to track the evolution of domain infrastructure, uncover historical patterns of use, and detect malicious activities tied to domains and their associated IP addresses. Examples: - Historical Resolutions - Shared IP Usage - Temporal Patterns - Malicious Domain Clustering - Historical Lookback This data component can be collected through the following measures: - Passive DNS Platforms: Use platforms that specialize in passive DNS collection and analysis: - Tools: Farsight DNSDB, RiskIQ PassiveTotal, PassiveDNS. - Threat Intelligence Feeds: Integrate passive DNS data from commercial or open-source threat intelligence providers. - Custom DNS Collectors: Deploy custom tools to capture DNS traffic at the network level for analysis. - Cloud DNS Services: Leverage cloud DNS services (e.g., AWS Route 53, Azure DNS) that maintain DNS query logs.

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
- DC0096: https://attack.mitre.org/datacomponents/DC0096
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
