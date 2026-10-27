# Limit Software Installation Technique Engineering Review

## Reference

- Technique: **M1033 — Limit Software Installation**

Prevent users or groups from installing unauthorized or unapproved software to reduce the risk of introducing malicious or vulnerable applications. This can be achieved through allowlists, software restriction policies, endpoint management tools, and least privilege access principles. This mitigation can be implemented through the following measures: Application Whitelisting - Implement Microsoft AppLocker or Windows Defender Application Control (WDAC) to create and enforce allowlists for approved software. - Whitelist applications based on file hash, path, or digital signatures. Restrict User Permissions - Remove local administrator rights for all non-IT users. - Use Role-Based Access Control (RBAC) to restrict installation permissions to privileged accounts only. Software Restriction Policies (SRP) - Use GPO to configure SRP to deny execution of binaries from directories such as `%AppData%`, `%Temp%`, and external drives. - Restrict specific file types (`.exe`, `.bat`, `.msi`, `.js`, `.vbs`) to trusted directories only. Endpoint Management Solutions - Deploy tools like Microsoft Intune, SCCM, or Jamf for centralized software management. - Maintain a list of approved software, versions, and updates across the enterprise. Monitor Software Installation Events - Enable logging of software installation events and monitor Windows Event ID 4688 and Event ID 11707 for software installs. - Use SIEM or EDR tools to alert on attempts to install unapproved software. Implement Software Inventory Management - Use tools like OSQuery or Wazuh to scan for unauthorized software on endpoints and servers. - Conduct regular audits to detect and remove unapproved software. *Tools for Implementation* Application Whitelisting: - Microsoft AppLocker - Windows Defender Application Control (WDAC) Endpoint Management: - Microsoft Intune - SCCM (System Center Configuration Manager) - Jamf Pro (macOS) - Puppet or Ansible for automation Software Restriction Policies: - Group Policy Object (GPO) - Microsoft Software Restriction Policies (SRP) Monitoring and Logging: - Splunk - OSQuery - Wazuh (open-source SIEM and XDR) - EDRs Inventory Management and Auditing: - OSQuery - Wazuh.

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
- M1033: https://attack.mitre.org/mitigations/M1033
- Reviewed: 2026-10-27
