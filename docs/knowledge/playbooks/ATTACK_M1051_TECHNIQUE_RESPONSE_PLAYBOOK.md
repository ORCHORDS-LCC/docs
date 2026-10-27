# Update Software Technique Response Playbook

## Target technique

**M1051 — Update Software**


Software updates ensure systems are protected against known vulnerabilities by applying patches and upgrades provided by vendors. Regular updates reduce the attack surface and prevent adversaries from exploiting known security gaps. This includes patching operating systems, applications, drivers, and firmware. This mitigation can be implemented through the following measures: Regular Operating System Updates - Implementation: Apply the latest Windows security updates monthly using WSUS (Windows Server Update Services) or a similar patch management solution. Configure systems to check for updates automatically and schedule reboots during maintenance windows. - Use Case: Prevents exploitation of OS vulnerabilities such as privilege escalation or remote code execution. Application Patching - Implementation: Monitor Apache's update release notes for security patches addressing vulnerabilities. Schedule updates for off-peak hours to avoid downtime while maintaining security compliance. - Use Case: Prevents exploitation of web application vulnerabilities, such as those leading to unauthorized access or data breaches. Firmware Updates - Implementation: Regularly check the vendor’s website for firmware updates addressing vulnerabilities. Plan for update deployment during scheduled maintenance to minimize business disruption. - Use Case: Protects against vulnerabilities that adversaries could exploit to gain access to network devices or inject malicious traffic. Emergency Patch Deployment - Implementation: Use the emergency patch deployment feature of the organization's patch management tool to apply updates to all affected Exchange servers within 24 hours. - Use Case: Reduces the risk of exploitation by rapidly addressing critical vulnerabilities. Centralized Patch Management - Implementation: Implement a centralized patch management system, such as SCCM or ManageEngine, to automate and track patch deployment across all environments. Generate regular compliance reports to ensure all systems are updated. - Use Case: Streamlines patching processes and ensures no critical systems are missed. *Tools for Implementation* Patch Management Tools: - WSUS: Manage and deploy Microsoft updates across the organization. - ManageEngine Patch Manager Plus: Automate patch deployment for OS and third-party apps. - Ansible: Automate updates across multiple platforms, including Linux and Windows. Vulnerability Scanning Tools: - OpenVAS: Open-source vulnerability scanning to identify missing patches.

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
- M1051: https://attack.mitre.org/mitigations/M1051
- Reviewed: 2026-10-27
