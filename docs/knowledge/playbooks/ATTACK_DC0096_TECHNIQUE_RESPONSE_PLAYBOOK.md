# Passive DNS Technique Response Playbook

## Target technique

**DC0096 — Passive DNS**


"Domain Name: Passive DNS" captures logged historical and real-time domain name system (DNS) data. This includes records of domain-to-IP address resolutions over time, enabling analysts to track the evolution of domain infrastructure, uncover historical patterns of use, and detect malicious activities tied to domains and their associated IP addresses. Examples: - Historical Resolutions - Shared IP Usage - Temporal Patterns - Malicious Domain Clustering - Historical Lookback This data component can be collected through the following measures: - Passive DNS Platforms: Use platforms that specialize in passive DNS collection and analysis: - Tools: Farsight DNSDB, RiskIQ PassiveTotal, PassiveDNS. - Threat Intelligence Feeds: Integrate passive DNS data from commercial or open-source threat intelligence providers. - Custom DNS Collectors: Deploy custom tools to capture DNS traffic at the network level for analysis. - Cloud DNS Services: Leverage cloud DNS services (e.g., AWS Route 53, Azure DNS) that maintain DNS query logs.

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
- DC0096: https://attack.mitre.org/datacomponents/DC0096
- Reviewed: 2026-10-27
