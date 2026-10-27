# Social Media Technique Engineering Review

## Reference

- Technique: **DC0052 — Social Media**

Established, compromised, or otherwise acquired by adversaries to conduct reconnaissance, influence operations, social engineering, or other cyber threats. *Data Collection Measures:* - API Monitoring - Social media APIs (e.g., Twitter API, Facebook Graph API) can extract behavioral patterns of accounts. - Web Scraping - Extracts public profile data, friend lists, or interactions to identify impersonation attempts. - Threat Intelligence Feeds - External feeds track malicious personas linked to disinformation campaigns or phishing. - OSINT Tools - Maltego, SpiderFoot, and OpenCTI can map social media persona relationships. - Endpoint Detection - EDR logs user behavior and alerts on suspicious social media interactions. - SIEM Logging - Detects access to known phishing pages or social media abuse via proxy logs. - Dark Web Monitoring - Identifies compromised social media credentials being sold.

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
- DC0052: https://attack.mitre.org/datacomponents/DC0052
- Reviewed: 2026-10-27
