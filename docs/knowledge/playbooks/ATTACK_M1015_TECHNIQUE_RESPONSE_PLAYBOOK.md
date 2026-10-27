# Active Directory Configuration Technique Response Playbook

## Target technique

**M1015 — Active Directory Configuration**


Implement robust Active Directory (AD) configurations using group policies to secure user accounts, control access, and minimize the attack surface. AD configurations enable centralized control over account settings, logon policies, and permissions, reducing the risk of unauthorized access and lateral movement within the network. This mitigation can be implemented through the following measures: Account Configuration: - Implementation: Use domain accounts instead of local accounts to leverage AD’s centralized management, including group policies, auditing, and access control. - Use Case: For IT staff managing shared resources, provision domain accounts that allow IT teams to log in centrally, reducing the risk of unmanaged, rogue local accounts on individual machines. Interactive Logon Restrictions: - Implementation: Configure group policies to restrict interactive logons (e.g., direct physical or RDP logons) for service accounts or privileged accounts that do not require such access. - Use Case: Prevent service accounts, such as SQL Server accounts, from having interactive logon privileges. This reduces the risk of these accounts being leveraged for lateral movement if compromised. Remote Desktop Settings: - Implementation: Limit Remote Desktop Protocol (RDP) access to specific, authorized accounts. Use group policies to enforce this, allowing only necessary users to establish RDP sessions. - Use Case: On sensitive servers (e.g., domain controllers or financial databases), restrict RDP access to administrative accounts only, while all other users are denied access. Dedicated Administrative Accounts: - Implementation: Create domain-wide administrative accounts that are restricted from interactive logons, designed solely for high-level tasks (e.g., software installation, patching). - Use Case: Create separate administrative accounts for different purposes, such as one set of accounts for installations and another for managing repository access. This limits exposure and helps reduce attack vectors. Authentication Silos: - Implementation: Configure Authentication Silos in AD, using group policies to create access zones with restrictions based on membership, such as the Protected Users security group. This restricts access to critical accounts and minimizes exposure to potential threats. - Use Case: Place high-risk or high-value accounts, such as executive or administrative accounts, in an Authentication Silo with extra controls, limiting their exposure to only necessary systems. This reduces the risk of credential misuse or abuse if these accounts are compromised. **Tools for Implementation**: - Active Directory Group Policies: Use Group Policy Management Console (GPMC) to configure, deploy, and enforce policies across AD environments. - PowerShell: Automate account configuration, logon restrictions, and policy application using PowerShell scripts. - AD Administrative Center: Manage Authentication Silos and configure high-level policies for critical user groups within AD.

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
- M1015: https://attack.mitre.org/mitigations/M1015
- Reviewed: 2026-10-27
