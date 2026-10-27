# Passive DNS Technique Platform Profile

## Reference

- Technique: **DC0096 — Passive DNS**
- Platforms named in the source: not stated

"Domain Name: Passive DNS" captures logged historical and real-time domain name system (DNS) data. This includes records of domain-to-IP address resolutions over time, enabling analysts to track the evolution of domain infrastructure, uncover historical patterns of use, and detect malicious activities tied to domains and their associated IP addresses. Examples: - Historical Resolutions - Shared IP Usage - Temporal Patterns - Malicious Domain Clustering - Historical Lookback This data component can be collected through the following measures: - Passive DNS Platforms: Use platforms that specialize in passive DNS collection and analysis: - Tools: Farsight DNSDB, RiskIQ PassiveTotal, PassiveDNS. - Threat Intelligence Feeds: Integrate passive DNS data from commercial or open-source threat intelligence providers. - Custom DNS Collectors: Deploy custom tools to capture DNS traffic at the network level for analysis. - Cloud DNS Services: Leverage cloud DNS services (e.g., AWS Route 53, Azure DNS) that maintain DNS query logs.

## Platform profile

1. Record the platforms in scope and the versions actually deployed.
2. Compare the deployed platform surface against the platforms the source names.
3. Record where the platform provides a native control for the technique, and where it does not.
4. Record the configuration evidence for the native control, where one exists.
5. Record the gap where the platform provides no native control, and the compensating detection.
6. Record the platform version, because platform behaviour changes between versions.

## Evidence

- the platform and version inventory for the scoped estate;
- the configuration export or screenshot for the native control;
- the detection evidence where the platform provides none.

## Limitations

A technique entry describes a class of abuse across platforms. The platform-specific exposure is a property of the deployment, established only by inventory and configuration evidence.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- DC0096: https://attack.mitre.org/datacomponents/DC0096
- Reviewed: 2026-10-27
