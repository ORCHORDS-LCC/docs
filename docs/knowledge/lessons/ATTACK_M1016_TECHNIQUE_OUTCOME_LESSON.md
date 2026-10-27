# M1016 Vulnerability Scanning Outcome Lesson

## Authoritative description

- Technique: **M1016 — Vulnerability Scanning**

Vulnerability scanning involves the automated or manual assessment of systems, applications, and networks to identify misconfigurations, unpatched software, or other security weaknesses. The process helps prioritize remediation efforts by classifying vulnerabilities based on risk and impact, reducing the likelihood of exploitation by adversaries. This mitigation can be implemented through the following measures: Proactive Identification of Vulnerabilities - Implementation: Use tools like Nessus or OpenVAS to scan endpoints, servers, and applications for missing patches and configuration issues. Schedule regular scans to ensure timely identification of vulnerabilities introduced by new deployments or updates. - Use Case: A scan identifies unpatched software, such as outdated Apache servers, which could be exploited via CVE-XXXX-XXXX. The server is promptly patched, mitigating the risk. Cloud Environment Scanning - Implementation: Use cloud-specific vulnerability management tools like AWS Inspector, Azure Security Center, or GCP Security Command Center to identify issues like open S3 buckets or overly permissive IAM roles. - Use Case: The scan detects a misconfigured S3 bucket with public read access, which is remediated to prevent potential data leakage. Network Device Scanning - Implementation: Use tools to scan network devices for vulnerabilities, such as weak SNMP strings or outdated firmware. Correlate scan results with vendor advisories to prioritize updates. - Use Case: Scanning detects a router running outdated firmware vulnerable to CVE-XXXX-YYYY. The firmware is updated to a secure version. Web Application Scanning - Implementation: Use dynamic application security testing (DAST) tools such as OWASP ZAP or Burp Suite to scan for common vulnerabilities like SQL injection or cross-site scripting (XSS). Perform regular scans post-deployment to identify newly introduced vulnerabilities. - Use Case: A scan identifies a cross-site scripting vulnerability in a form input field, which is promptly remediated by developers. Prioritizing Vulnerabilities - Implementation: Use vulnerability scoring frameworks like CVSS to assess severity. Integrate vulnerability scanning tools with ticketing systems to assign remediation tasks based on criticality. - Use Case: A critical vulnerability with a CVSS score of 9.8 affecting remote access servers is prioritized and patched first. *Tools for Implementation* Open Source Tools: - OpenVAS: Comprehensive network and system vulnerability scanning. - OWASP ZAP: Dynamic scanning of web applications for vulnerabilities. - Nmap with NSE Scripts: Network scanning with scripts to detect vulnerabilities.

## Reusable lesson

This technique should be treated as an explicit review question when it is relevant to the system or organisation, rather than assumed to be covered by a generic control statement or by tooling that reports a related signal.

## Apply the lesson

1. Define the real scope before judging coverage.
2. Inspect current technical, process, governance, or operational evidence.
3. Separate documented intent from verified behaviour.
4. Record partial coverage and unresolved gaps instead of converting them into a pass.
5. Revisit when the underlying scope, threat environment, technology, suppliers, or mission materially changes.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- M1016: https://attack.mitre.org/mitigations/M1016
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
