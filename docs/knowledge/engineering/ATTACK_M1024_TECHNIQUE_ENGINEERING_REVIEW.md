# Restrict Registry Permissions Technique Engineering Review

## Reference

- Technique: **M1024 — Restrict Registry Permissions**

Restricting registry permissions involves configuring access control settings for sensitive registry keys and hives to ensure that only authorized users or processes can make modifications. By limiting access, organizations can prevent unauthorized changes that adversaries might use for persistence, privilege escalation, or defense evasion. This mitigation can be implemented through the following measures: Review and Adjust Permissions on Critical Keys - Regularly review permissions on keys such as `Run`, `RunOnce`, and `Services` to ensure only authorized users have write access. - Use tools like `icacls` or `PowerShell` to automate permission adjustments. Enable Registry Auditing - Enable auditing on sensitive keys to log access attempts. - Use Event Viewer or SIEM solutions to analyze logs and detect suspicious activity. - Example Audit Policy: `auditpol /set /subcategory:"Registry" /success:enable /failure:enable` Protect Credential-Related Hives - Limit access to hives like `SAM`,`SECURITY`, and `SYSTEM` to prevent credential dumping or other unauthorized access. - Use LSA Protection to add an additional security layer for credential storage. Restrict Registry Editor Usage - Use Group Policy to restrict access to regedit.exe for non-administrative users. - Block execution of registry editing tools on endpoints where they are unnecessary. Deploy Baseline Configuration Tools - Use tools like Microsoft Security Compliance Toolkit or CIS Benchmarks to apply and maintain secure registry configurations. *Tools for Implementation* Registry Permission Tools: - Registry Editor (regedit): Built-in tool to manage registry permissions. - PowerShell: Automate permissions and manage keys. `Set-ItemProperty -Path "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run" -Name "KeyName" -Value "Value"` - icacls: Command-line tool to modify ACLs. Monitoring Tools: - Sysmon: Monitor and log registry events. - Event Viewer: View registry access logs. Policy Management Tools: - Group Policy Management Console (GPMC): Enforce registry permissions via GPOs. - Microsoft Endpoint Manager: Deploy configuration baselines for registry permissions.

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
- M1024: https://attack.mitre.org/mitigations/M1024
- Reviewed: 2026-10-27
