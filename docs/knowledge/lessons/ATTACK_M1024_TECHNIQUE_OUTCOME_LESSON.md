# M1024 Restrict Registry Permissions Outcome Lesson

## Authoritative description

- Technique: **M1024 — Restrict Registry Permissions**

Restricting registry permissions involves configuring access control settings for sensitive registry keys and hives to ensure that only authorized users or processes can make modifications. By limiting access, organizations can prevent unauthorized changes that adversaries might use for persistence, privilege escalation, or defense evasion. This mitigation can be implemented through the following measures: Review and Adjust Permissions on Critical Keys - Regularly review permissions on keys such as `Run`, `RunOnce`, and `Services` to ensure only authorized users have write access. - Use tools like `icacls` or `PowerShell` to automate permission adjustments. Enable Registry Auditing - Enable auditing on sensitive keys to log access attempts. - Use Event Viewer or SIEM solutions to analyze logs and detect suspicious activity. - Example Audit Policy: `auditpol /set /subcategory:"Registry" /success:enable /failure:enable` Protect Credential-Related Hives - Limit access to hives like `SAM`,`SECURITY`, and `SYSTEM` to prevent credential dumping or other unauthorized access. - Use LSA Protection to add an additional security layer for credential storage. Restrict Registry Editor Usage - Use Group Policy to restrict access to regedit.exe for non-administrative users. - Block execution of registry editing tools on endpoints where they are unnecessary. Deploy Baseline Configuration Tools - Use tools like Microsoft Security Compliance Toolkit or CIS Benchmarks to apply and maintain secure registry configurations. *Tools for Implementation* Registry Permission Tools: - Registry Editor (regedit): Built-in tool to manage registry permissions. - PowerShell: Automate permissions and manage keys. `Set-ItemProperty -Path "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run" -Name "KeyName" -Value "Value"` - icacls: Command-line tool to modify ACLs. Monitoring Tools: - Sysmon: Monitor and log registry events. - Event Viewer: View registry access logs. Policy Management Tools: - Group Policy Management Console (GPMC): Enforce registry permissions via GPOs. - Microsoft Endpoint Manager: Deploy configuration baselines for registry permissions.

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
- M1024: https://attack.mitre.org/mitigations/M1024
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
