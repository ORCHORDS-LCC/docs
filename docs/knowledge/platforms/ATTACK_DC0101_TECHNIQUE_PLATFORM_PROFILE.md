# Domain Registration Technique Platform Profile

## Reference

- Technique: **DC0101 — Domain Registration**
- Platforms named in the source: not stated

"Domain Name: Domain Registration" data component captures information about the assignment, ownership, and metadata of domain names. This information is often sourced from registries like WHOIS and includes details such as registrant names, contact information, registration dates, expiration dates, and registrar details. This data is invaluable for tracking domain ownership, detecting malicious domain registrations, and identifying trends in adversary behavior. Examples: - Registrant Information: WHOIS lookup of example.com - Registration and Expiration Dates: A domain registered a week before being used in phishing attacks. - Domain Status: Status codes like clientTransferProhibited or serverHold indicate domain restrictions or potential hijacking activity. - Name Server Information: Name servers point to a public DNS provider often associated with malicious campaigns. - Privacy Protection: A domain uses WHOIS privacy protection to hide registrant details. This data component can be collected through the following measures: - WHOIS Services: Use tools or services to perform WHOIS lookups: - WHOIS APIs: Automate domain registration lookups with APIs: - Registrar Platforms: Directly query domain registrars (e.g., GoDaddy, Namecheap) for detailed registration data. - Threat Intelligence Platforms: Integrate domain registration data from services like Recorded Future, RiskIQ, or PassiveTotal for enriched analysis.

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
- DC0101: https://attack.mitre.org/datacomponents/DC0101
- Reviewed: 2026-10-27
