# Restrict Registry Permissions Technique Platform Profile

## Reference

- Technique: **M1024 — Restrict Registry Permissions**
- Platforms named in the source: not stated

Restricting registry permissions involves configuring access control settings for sensitive registry keys and hives to ensure that only authorized users or processes can make modifications. By limiting access, organizations can prevent unauthorized changes that adversaries might use for persistence, privilege escalation, or defense evasion. This mitigation can be implemented through the following measures: Review and Adjust Permissions on Critical Keys - Regularly review permissions on keys such as `Run`, `RunOnce`, and `Services` to ensure only authorized users have write access. - Use tools like `icacls` or `PowerShell` to automate permission adjustments. Enable Registry Auditing - Enable auditing on sensitive keys to log access attempts. - Use Event Viewer or SIEM solutions to analyze logs and detect suspicious activity. - Example Audit Policy: `auditpol /set /subcategory:"Registry" /success:enable /failure:enable` Protect Credential-Related Hives - Limit access to hives like `SAM`,`SECURITY`, and `SYSTEM` to prevent credential dumping or other unauthorized access. - Use LSA Protection to add an additional security layer for credential storage. Restrict Registry Editor Usage - Use Group Policy to restrict access to regedit.exe for non-administrative users. - Block execution of registry editing tools on endpoints where they are unnecessary. Deploy Baseline Configuration Tools - Use tools like Microsoft Security Compliance Toolkit or CIS Benchmarks to apply and maintain secure registry configurations. *Tools for Implementation* Registry Permission Tools: - Registry Editor (regedit): Built-in tool to manage registry permissions. - PowerShell: Automate permissions and manage keys. `Set-ItemProperty -Path "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run" -Name "KeyName" -Value "Value"` - icacls: Command-line tool to modify ACLs. Monitoring Tools: - Sysmon: Monitor and log registry events. - Event Viewer: View registry access logs. Policy Management Tools: - Group Policy Management Console (GPMC): Enforce registry permissions via GPOs. - Microsoft Endpoint Manager: Deploy configuration baselines for registry permissions.

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
- M1024: https://attack.mitre.org/mitigations/M1024
- Reviewed: 2026-10-27
