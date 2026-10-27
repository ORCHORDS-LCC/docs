# Restrict Web-Based Content Technique Platform Profile

## Reference

- Technique: **M1021 — Restrict Web-Based Content**
- Platforms named in the source: not stated

Restricting web-based content involves enforcing policies and technologies that limit access to potentially malicious websites, unsafe downloads, and unauthorized browser behaviors. This can include URL filtering, download restrictions, script blocking, and extension control to protect against exploitation, phishing, and malware delivery. This mitigation can be implemented through the following measures: Deploy Web Proxy Filtering: - Use solutions to filter web traffic based on categories, reputation, and content types. - Enforce policies that block unsafe websites or file types at the gateway level. Enable DNS-Based Filtering: - Implement tools to restrict access to domains associated with malware or phishing campaigns. - Use public DNS filtering services to enhance protection. Enforce Content Security Policies (CSP): - Configure CSP headers on internal and external web applications to restrict script execution, iframe embedding, and cross-origin requests. Control Browser Features: - Disable unapproved browser features like automatic downloads, developer tools, or unsafe scripting. - Enforce policies through tools like Group Policy Management to control browser settings. Monitor and Alert on Web-Based Threats: - Use SIEM tools to collect and analyze web proxy logs for signs of anomalous or malicious activity. - Configure alerts for access attempts to blocked domains or repeated file download failures.

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
- M1021: https://attack.mitre.org/mitigations/M1021
- Reviewed: 2026-10-27
