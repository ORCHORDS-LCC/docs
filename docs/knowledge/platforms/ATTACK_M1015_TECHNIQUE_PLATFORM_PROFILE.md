# Active Directory Configuration Technique Platform Profile

## Reference

- Technique: **M1015 — Active Directory Configuration**
- Platforms named in the source: not stated

Implement robust Active Directory (AD) configurations using group policies to secure user accounts, control access, and minimize the attack surface. AD configurations enable centralized control over account settings, logon policies, and permissions, reducing the risk of unauthorized access and lateral movement within the network. This mitigation can be implemented through the following measures: Account Configuration: - Implementation: Use domain accounts instead of local accounts to leverage AD’s centralized management, including group policies, auditing, and access control. - Use Case: For IT staff managing shared resources, provision domain accounts that allow IT teams to log in centrally, reducing the risk of unmanaged, rogue local accounts on individual machines. Interactive Logon Restrictions: - Implementation: Configure group policies to restrict interactive logons (e.g., direct physical or RDP logons) for service accounts or privileged accounts that do not require such access. - Use Case: Prevent service accounts, such as SQL Server accounts, from having interactive logon privileges. This reduces the risk of these accounts being leveraged for lateral movement if compromised. Remote Desktop Settings: - Implementation: Limit Remote Desktop Protocol (RDP) access to specific, authorized accounts. Use group policies to enforce this, allowing only necessary users to establish RDP sessions. - Use Case: On sensitive servers (e.g., domain controllers or financial databases), restrict RDP access to administrative accounts only, while all other users are denied access. Dedicated Administrative Accounts: - Implementation: Create domain-wide administrative accounts that are restricted from interactive logons, designed solely for high-level tasks (e.g., software installation, patching). - Use Case: Create separate administrative accounts for different purposes, such as one set of accounts for installations and another for managing repository access. This limits exposure and helps reduce attack vectors. Authentication Silos: - Implementation: Configure Authentication Silos in AD, using group policies to create access zones with restrictions based on membership, such as the Protected Users security group. This restricts access to critical accounts and minimizes exposure to potential threats. - Use Case: Place high-risk or high-value accounts, such as executive or administrative accounts, in an Authentication Silo with extra controls, limiting their exposure to only necessary systems. This reduces the risk of credential misuse or abuse if these accounts are compromised. **Tools for Implementation**: - Active Directory Group Policies: Use Group Policy Management Console (GPMC) to configure, deploy, and enforce policies across AD environments. - PowerShell: Automate account configuration, logon restrictions, and policy application using PowerShell scripts. - AD Administrative Center: Manage Authentication Silos and configure high-level policies for critical user groups within AD.

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
- M1015: https://attack.mitre.org/mitigations/M1015
- Reviewed: 2026-10-27
