# Restrict Registry Permissions Technique Response Playbook

## Target technique

**M1024 — Restrict Registry Permissions**


Restricting registry permissions involves configuring access control settings for sensitive registry keys and hives to ensure that only authorized users or processes can make modifications. By limiting access, organizations can prevent unauthorized changes that adversaries might use for persistence, privilege escalation, or defense evasion. This mitigation can be implemented through the following measures: Review and Adjust Permissions on Critical Keys - Regularly review permissions on keys such as `Run`, `RunOnce`, and `Services` to ensure only authorized users have write access. - Use tools like `icacls` or `PowerShell` to automate permission adjustments. Enable Registry Auditing - Enable auditing on sensitive keys to log access attempts. - Use Event Viewer or SIEM solutions to analyze logs and detect suspicious activity. - Example Audit Policy: `auditpol /set /subcategory:"Registry" /success:enable /failure:enable` Protect Credential-Related Hives - Limit access to hives like `SAM`,`SECURITY`, and `SYSTEM` to prevent credential dumping or other unauthorized access. - Use LSA Protection to add an additional security layer for credential storage. Restrict Registry Editor Usage - Use Group Policy to restrict access to regedit.exe for non-administrative users. - Block execution of registry editing tools on endpoints where they are unnecessary. Deploy Baseline Configuration Tools - Use tools like Microsoft Security Compliance Toolkit or CIS Benchmarks to apply and maintain secure registry configurations. *Tools for Implementation* Registry Permission Tools: - Registry Editor (regedit): Built-in tool to manage registry permissions. - PowerShell: Automate permissions and manage keys. `Set-ItemProperty -Path "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run" -Name "KeyName" -Value "Value"` - icacls: Command-line tool to modify ACLs. Monitoring Tools: - Sysmon: Monitor and log registry events. - Event Viewer: View registry access logs. Policy Management Tools: - Group Policy Management Console (GPMC): Enforce registry permissions via GPOs. - Microsoft Endpoint Manager: Deploy configuration baselines for registry permissions.

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
- M1024: https://attack.mitre.org/mitigations/M1024
- Reviewed: 2026-10-27
