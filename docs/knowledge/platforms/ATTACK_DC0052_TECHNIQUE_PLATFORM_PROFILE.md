# Social Media Technique Platform Profile

## Reference

- Technique: **DC0052 — Social Media**
- Platforms named in the source: not stated

Established, compromised, or otherwise acquired by adversaries to conduct reconnaissance, influence operations, social engineering, or other cyber threats. *Data Collection Measures:* - API Monitoring - Social media APIs (e.g., Twitter API, Facebook Graph API) can extract behavioral patterns of accounts. - Web Scraping - Extracts public profile data, friend lists, or interactions to identify impersonation attempts. - Threat Intelligence Feeds - External feeds track malicious personas linked to disinformation campaigns or phishing. - OSINT Tools - Maltego, SpiderFoot, and OpenCTI can map social media persona relationships. - Endpoint Detection - EDR logs user behavior and alerts on suspicious social media interactions. - SIEM Logging - Detects access to known phishing pages or social media abuse via proxy logs. - Dark Web Monitoring - Identifies compromised social media credentials being sold.

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
- DC0052: https://attack.mitre.org/datacomponents/DC0052
- Reviewed: 2026-10-27
