# Restrict Web-Based Content Technique Engineering Review

## Reference

- Technique: **M1021 — Restrict Web-Based Content**

Restricting web-based content involves enforcing policies and technologies that limit access to potentially malicious websites, unsafe downloads, and unauthorized browser behaviors. This can include URL filtering, download restrictions, script blocking, and extension control to protect against exploitation, phishing, and malware delivery. This mitigation can be implemented through the following measures: Deploy Web Proxy Filtering: - Use solutions to filter web traffic based on categories, reputation, and content types. - Enforce policies that block unsafe websites or file types at the gateway level. Enable DNS-Based Filtering: - Implement tools to restrict access to domains associated with malware or phishing campaigns. - Use public DNS filtering services to enhance protection. Enforce Content Security Policies (CSP): - Configure CSP headers on internal and external web applications to restrict script execution, iframe embedding, and cross-origin requests. Control Browser Features: - Disable unapproved browser features like automatic downloads, developer tools, or unsafe scripting. - Enforce policies through tools like Group Policy Management to control browser settings. Monitor and Alert on Web-Based Threats: - Use SIEM tools to collect and analyze web proxy logs for signs of anomalous or malicious activity. - Configure alerts for access attempts to blocked domains or repeated file download failures.

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
- M1021: https://attack.mitre.org/mitigations/M1021
- Reviewed: 2026-10-27
