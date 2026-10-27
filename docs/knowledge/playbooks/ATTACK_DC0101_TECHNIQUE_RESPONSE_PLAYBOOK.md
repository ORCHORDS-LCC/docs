# Domain Registration Technique Response Playbook

## Target technique

**DC0101 — Domain Registration**


"Domain Name: Domain Registration" data component captures information about the assignment, ownership, and metadata of domain names. This information is often sourced from registries like WHOIS and includes details such as registrant names, contact information, registration dates, expiration dates, and registrar details. This data is invaluable for tracking domain ownership, detecting malicious domain registrations, and identifying trends in adversary behavior. Examples: - Registrant Information: WHOIS lookup of example.com - Registration and Expiration Dates: A domain registered a week before being used in phishing attacks. - Domain Status: Status codes like clientTransferProhibited or serverHold indicate domain restrictions or potential hijacking activity. - Name Server Information: Name servers point to a public DNS provider often associated with malicious campaigns. - Privacy Protection: A domain uses WHOIS privacy protection to hide registrant details. This data component can be collected through the following measures: - WHOIS Services: Use tools or services to perform WHOIS lookups: - WHOIS APIs: Automate domain registration lookups with APIs: - Registrar Platforms: Directly query domain registrars (e.g., GoDaddy, Namecheap) for detailed registration data. - Threat Intelligence Platforms: Integrate domain registration data from services like Recorded Future, RiskIQ, or PassiveTotal for enriched analysis.

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
- DC0101: https://attack.mitre.org/datacomponents/DC0101
- Reviewed: 2026-10-27
