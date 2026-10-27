# Limit Software Installation Technique Response Playbook

## Target technique

**M1033 — Limit Software Installation**


Prevent users or groups from installing unauthorized or unapproved software to reduce the risk of introducing malicious or vulnerable applications. This can be achieved through allowlists, software restriction policies, endpoint management tools, and least privilege access principles. This mitigation can be implemented through the following measures: Application Whitelisting - Implement Microsoft AppLocker or Windows Defender Application Control (WDAC) to create and enforce allowlists for approved software. - Whitelist applications based on file hash, path, or digital signatures. Restrict User Permissions - Remove local administrator rights for all non-IT users. - Use Role-Based Access Control (RBAC) to restrict installation permissions to privileged accounts only. Software Restriction Policies (SRP) - Use GPO to configure SRP to deny execution of binaries from directories such as `%AppData%`, `%Temp%`, and external drives. - Restrict specific file types (`.exe`, `.bat`, `.msi`, `.js`, `.vbs`) to trusted directories only. Endpoint Management Solutions - Deploy tools like Microsoft Intune, SCCM, or Jamf for centralized software management. - Maintain a list of approved software, versions, and updates across the enterprise. Monitor Software Installation Events - Enable logging of software installation events and monitor Windows Event ID 4688 and Event ID 11707 for software installs. - Use SIEM or EDR tools to alert on attempts to install unapproved software. Implement Software Inventory Management - Use tools like OSQuery or Wazuh to scan for unauthorized software on endpoints and servers. - Conduct regular audits to detect and remove unapproved software. *Tools for Implementation* Application Whitelisting: - Microsoft AppLocker - Windows Defender Application Control (WDAC) Endpoint Management: - Microsoft Intune - SCCM (System Center Configuration Manager) - Jamf Pro (macOS) - Puppet or Ansible for automation Software Restriction Policies: - Group Policy Object (GPO) - Microsoft Software Restriction Policies (SRP) Monitoring and Logging: - Splunk - OSQuery - Wazuh (open-source SIEM and XDR) - EDRs Inventory Management and Auditing: - OSQuery - Wazuh.

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
- M1033: https://attack.mitre.org/mitigations/M1033
- Reviewed: 2026-10-27
