# Analytic 2024 Technique Platform Profile

## Reference

- Technique: **AN2024 — Analytic 2024**
- Platforms named in the source: PRE

Monitor logged domain name system (DNS) data for purchased domains that can be used during targeting. Reputation/category-based detection may be difficult until the categorization is updated. Detection efforts may be focused on related stages of the adversary lifecycle, such as during Initial Access and Command and Control. Domain registration information is, by design, captured in public registration logs. Consider use of services that may aid in tracking of newly acquired domains, such as WHOIS databases and/or passive DNS. In some cases it may be possible to pivot on known pieces of domain registration information to uncover other infrastructure purchased by the adversary. Consider monitoring for domains created with a similar structure to your own, including under a different TLD. Though various tools and services exist to track, query, and monitor domain name registration information, tracking across multiple DNS infrastructures can require multiple tools/services or more advanced analytics. Detection efforts may be focused on related stages of the adversary lifecycle, such as during Initial Access and Command and Control. Monitor queried domain name system (DNS) registry data for purchased domains that can be used during targeting. Reputation/category-based detection may be difficult until the categorization is updated. Detection efforts may be focused on related stages of the adversary lifecycle, such as during Initial Access and Command and Control.

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
- AN2024: https://attack.mitre.org/detectionstrategies/DET0892#AN2024
- Reviewed: 2026-10-27
