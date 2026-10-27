# Social Media Technique Response Playbook

## Target technique

**DC0052 — Social Media**


Established, compromised, or otherwise acquired by adversaries to conduct reconnaissance, influence operations, social engineering, or other cyber threats. *Data Collection Measures:* - API Monitoring - Social media APIs (e.g., Twitter API, Facebook Graph API) can extract behavioral patterns of accounts. - Web Scraping - Extracts public profile data, friend lists, or interactions to identify impersonation attempts. - Threat Intelligence Feeds - External feeds track malicious personas linked to disinformation campaigns or phishing. - OSINT Tools - Maltego, SpiderFoot, and OpenCTI can map social media persona relationships. - Endpoint Detection - EDR logs user behavior and alerts on suspicious social media interactions. - SIEM Logging - Detects access to known phishing pages or social media abuse via proxy logs. - Dark Web Monitoring - Identifies compromised social media credentials being sold.

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
- DC0052: https://attack.mitre.org/datacomponents/DC0052
- Reviewed: 2026-10-27
