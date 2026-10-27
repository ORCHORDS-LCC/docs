# M1033 Limit Software Installation Outcome Lesson

## Authoritative description

- Technique: **M1033 — Limit Software Installation**

Prevent users or groups from installing unauthorized or unapproved software to reduce the risk of introducing malicious or vulnerable applications. This can be achieved through allowlists, software restriction policies, endpoint management tools, and least privilege access principles. This mitigation can be implemented through the following measures: Application Whitelisting - Implement Microsoft AppLocker or Windows Defender Application Control (WDAC) to create and enforce allowlists for approved software. - Whitelist applications based on file hash, path, or digital signatures. Restrict User Permissions - Remove local administrator rights for all non-IT users. - Use Role-Based Access Control (RBAC) to restrict installation permissions to privileged accounts only. Software Restriction Policies (SRP) - Use GPO to configure SRP to deny execution of binaries from directories such as `%AppData%`, `%Temp%`, and external drives. - Restrict specific file types (`.exe`, `.bat`, `.msi`, `.js`, `.vbs`) to trusted directories only. Endpoint Management Solutions - Deploy tools like Microsoft Intune, SCCM, or Jamf for centralized software management. - Maintain a list of approved software, versions, and updates across the enterprise. Monitor Software Installation Events - Enable logging of software installation events and monitor Windows Event ID 4688 and Event ID 11707 for software installs. - Use SIEM or EDR tools to alert on attempts to install unapproved software. Implement Software Inventory Management - Use tools like OSQuery or Wazuh to scan for unauthorized software on endpoints and servers. - Conduct regular audits to detect and remove unapproved software. *Tools for Implementation* Application Whitelisting: - Microsoft AppLocker - Windows Defender Application Control (WDAC) Endpoint Management: - Microsoft Intune - SCCM (System Center Configuration Manager) - Jamf Pro (macOS) - Puppet or Ansible for automation Software Restriction Policies: - Group Policy Object (GPO) - Microsoft Software Restriction Policies (SRP) Monitoring and Logging: - Splunk - OSQuery - Wazuh (open-source SIEM and XDR) - EDRs Inventory Management and Auditing: - OSQuery - Wazuh.

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
- M1033: https://attack.mitre.org/mitigations/M1033
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
