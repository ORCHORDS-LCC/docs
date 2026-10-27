# Update Software Technique Engineering Review

## Reference

- Technique: **M1051 — Update Software**

Software updates ensure systems are protected against known vulnerabilities by applying patches and upgrades provided by vendors. Regular updates reduce the attack surface and prevent adversaries from exploiting known security gaps. This includes patching operating systems, applications, drivers, and firmware. This mitigation can be implemented through the following measures: Regular Operating System Updates - Implementation: Apply the latest Windows security updates monthly using WSUS (Windows Server Update Services) or a similar patch management solution. Configure systems to check for updates automatically and schedule reboots during maintenance windows. - Use Case: Prevents exploitation of OS vulnerabilities such as privilege escalation or remote code execution. Application Patching - Implementation: Monitor Apache's update release notes for security patches addressing vulnerabilities. Schedule updates for off-peak hours to avoid downtime while maintaining security compliance. - Use Case: Prevents exploitation of web application vulnerabilities, such as those leading to unauthorized access or data breaches. Firmware Updates - Implementation: Regularly check the vendor’s website for firmware updates addressing vulnerabilities. Plan for update deployment during scheduled maintenance to minimize business disruption. - Use Case: Protects against vulnerabilities that adversaries could exploit to gain access to network devices or inject malicious traffic. Emergency Patch Deployment - Implementation: Use the emergency patch deployment feature of the organization's patch management tool to apply updates to all affected Exchange servers within 24 hours. - Use Case: Reduces the risk of exploitation by rapidly addressing critical vulnerabilities. Centralized Patch Management - Implementation: Implement a centralized patch management system, such as SCCM or ManageEngine, to automate and track patch deployment across all environments. Generate regular compliance reports to ensure all systems are updated. - Use Case: Streamlines patching processes and ensures no critical systems are missed. *Tools for Implementation* Patch Management Tools: - WSUS: Manage and deploy Microsoft updates across the organization. - ManageEngine Patch Manager Plus: Automate patch deployment for OS and third-party apps. - Ansible: Automate updates across multiple platforms, including Linux and Windows. Vulnerability Scanning Tools: - OpenVAS: Open-source vulnerability scanning to identify missing patches.

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
- M1051: https://attack.mitre.org/mitigations/M1051
- Reviewed: 2026-10-27
