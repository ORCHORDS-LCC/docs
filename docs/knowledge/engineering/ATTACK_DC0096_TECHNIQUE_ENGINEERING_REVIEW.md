# Passive DNS Technique Engineering Review

## Reference

- Technique: **DC0096 — Passive DNS**

"Domain Name: Passive DNS" captures logged historical and real-time domain name system (DNS) data. This includes records of domain-to-IP address resolutions over time, enabling analysts to track the evolution of domain infrastructure, uncover historical patterns of use, and detect malicious activities tied to domains and their associated IP addresses. Examples: - Historical Resolutions - Shared IP Usage - Temporal Patterns - Malicious Domain Clustering - Historical Lookback This data component can be collected through the following measures: - Passive DNS Platforms: Use platforms that specialize in passive DNS collection and analysis: - Tools: Farsight DNSDB, RiskIQ PassiveTotal, PassiveDNS. - Threat Intelligence Feeds: Integrate passive DNS data from commercial or open-source threat intelligence providers. - Custom DNS Collectors: Deploy custom tools to capture DNS traffic at the network level for analysis. - Cloud DNS Services: Leverage cloud DNS services (e.g., AWS Route 53, Azure DNS) that maintain DNS query logs.

## Engineering review

1. Identify the engineering boundary where the technique would apply: the component, the service, or the deployment.
2. Review the design decision that would prevent the technique, and record the alternative considered.
3. Review the implementation evidence for the preventive control.
4. Review the test coverage that would fail if the control regressed.
5. Review the observability: which signal would show the control is not operating.
6. Record the residual risk where prevention is not achievable, and the detection that compensates.

## Review evidence

- the design record for the preventive decision;
- the implementation or configuration evidence;
- the test record showing the control is exercised;
- the observability mapping.

## Limitations

An engineering review describes what the design and the implementation evidence show. It does not claim the technique has been addressed in production.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- DC0096: https://attack.mitre.org/datacomponents/DC0096
- Reviewed: 2026-10-27
