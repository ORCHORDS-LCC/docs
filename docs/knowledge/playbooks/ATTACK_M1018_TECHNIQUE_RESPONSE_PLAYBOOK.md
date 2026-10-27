# User Account Management Technique Response Playbook

## Target technique

**M1018 — User Account Management**


User Account Management involves implementing and enforcing policies for the lifecycle of user accounts, including creation, modification, and deactivation. Proper account management reduces the attack surface by limiting unauthorized access, managing account privileges, and ensuring accounts are used according to organizational policies. This mitigation can be implemented through the following measures: Enforcing the Principle of Least Privilege - Implementation: Assign users only the minimum permissions required to perform their job functions. Regularly audit accounts to ensure no excess permissions are granted. - Use Case: Reduces the risk of privilege escalation by ensuring accounts cannot perform unauthorized actions. Implementing Strong Password Policies - Implementation: Enforce password complexity requirements (e.g., length, character types). Require password expiration every 90 days and disallow password reuse. - Use Case: Prevents adversaries from gaining unauthorized access through password guessing or brute force attacks. Managing Dormant and Orphaned Accounts - Implementation: Implement automated workflows to disable accounts after a set period of inactivity (e.g., 30 days). Remove orphaned accounts (e.g., accounts without an assigned owner) during regular account audits. - Use Case: Eliminates dormant accounts that could be exploited by attackers. Account Lockout Policies - Implementation: Configure account lockout thresholds (e.g., lock accounts after five failed login attempts). Set lockout durations to a minimum of 15 minutes. - Use Case: Mitigates automated attack techniques that rely on repeated login attempts. Multi-Factor Authentication (MFA) for High-Risk Accounts - Implementation: Require MFA for all administrative accounts and high-risk users. Use MFA mechanisms like hardware tokens, authenticator apps, or biometrics. - Use Case: Prevents unauthorized access, even if credentials are stolen. Restricting Interactive Logins - Implementation: Restrict interactive logins for privileged accounts to specific secure systems or management consoles. Use group policies to enforce logon restrictions. - Use Case: Protects sensitive accounts from misuse or exploitation. *Tools for Implementation* Built-in Tools: - Microsoft Active Directory (AD): Centralized account management and RBAC enforcement. - Group Policy Object (GPO): Enforce password policies, logon restrictions, and account lockout policies. Identity and Access Management (IAM) Tools: - Okta: Centralized user provisioning, MFA, and SSO integration. - Microsoft Azure Active Directory: Provides advanced account lifecycle management, role-based access, and conditional access policies. Privileged Account Management (PAM): - CyberArk, BeyondTrust, Thycotic: Manage and monitor privileged account usage, enforce session recording, and JIT access.

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
- M1018: https://attack.mitre.org/mitigations/M1018
- Reviewed: 2026-10-27
