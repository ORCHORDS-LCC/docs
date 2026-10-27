# Social Media Technique Operationalization Review

## Reference

- Technique: **DC0052 — Social Media**

Established, compromised, or otherwise acquired by adversaries to conduct reconnaissance, influence operations, social engineering, or other cyber threats. *Data Collection Measures:* - API Monitoring - Social media APIs (e.g., Twitter API, Facebook Graph API) can extract behavioral patterns of accounts. - Web Scraping - Extracts public profile data, friend lists, or interactions to identify impersonation attempts. - Threat Intelligence Feeds - External feeds track malicious personas linked to disinformation campaigns or phishing. - OSINT Tools - Maltego, SpiderFoot, and OpenCTI can map social media persona relationships. - Endpoint Detection - EDR logs user behavior and alerts on suspicious social media interactions. - SIEM Logging - Detects access to known phishing pages or social media abuse via proxy logs. - Dark Web Monitoring - Identifies compromised social media credentials being sold.

## Operationalization review

1. Record the operational scope: which services, environments, and data the technique could affect.
2. Record the runbook that would be executed, and its owner.
3. Record the telemetry the runbook depends on, and whether it is retained long enough to investigate.
4. Record the detection that would surface the technique before or after it has an effect.
5. Record the recovery path, and the evidence that recovery has been rehearsed.
6. Record the residual operational risk where the runbook depends on a manual step.

## Review evidence

- the runbook and its owner;
- the telemetry retention and coverage record;
- the detection mapping;
- the exercise or rehearsal record.

## Limitations

An operationalization review describes the runbook and the evidence around it. It does not claim the technique has been prevented or detected in a live environment.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- DC0052: https://attack.mitre.org/datacomponents/DC0052
- Reviewed: 2026-10-27
