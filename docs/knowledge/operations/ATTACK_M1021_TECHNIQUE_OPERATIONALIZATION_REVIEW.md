# Restrict Web-Based Content Technique Operationalization Review

## Reference

- Technique: **M1021 — Restrict Web-Based Content**

Restricting web-based content involves enforcing policies and technologies that limit access to potentially malicious websites, unsafe downloads, and unauthorized browser behaviors. This can include URL filtering, download restrictions, script blocking, and extension control to protect against exploitation, phishing, and malware delivery. This mitigation can be implemented through the following measures: Deploy Web Proxy Filtering: - Use solutions to filter web traffic based on categories, reputation, and content types. - Enforce policies that block unsafe websites or file types at the gateway level. Enable DNS-Based Filtering: - Implement tools to restrict access to domains associated with malware or phishing campaigns. - Use public DNS filtering services to enhance protection. Enforce Content Security Policies (CSP): - Configure CSP headers on internal and external web applications to restrict script execution, iframe embedding, and cross-origin requests. Control Browser Features: - Disable unapproved browser features like automatic downloads, developer tools, or unsafe scripting. - Enforce policies through tools like Group Policy Management to control browser settings. Monitor and Alert on Web-Based Threats: - Use SIEM tools to collect and analyze web proxy logs for signs of anomalous or malicious activity. - Configure alerts for access attempts to blocked domains or repeated file download failures.

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
- M1021: https://attack.mitre.org/mitigations/M1021
- Reviewed: 2026-10-27
