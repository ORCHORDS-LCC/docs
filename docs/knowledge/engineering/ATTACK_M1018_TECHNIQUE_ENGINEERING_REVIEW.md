# User Account Management Technique Engineering Review

## Reference

- Technique: **M1018 — User Account Management**

User Account Management involves implementing and enforcing policies for the lifecycle of user accounts, including creation, modification, and deactivation. Proper account management reduces the attack surface by limiting unauthorized access, managing account privileges, and ensuring accounts are used according to organizational policies. This mitigation can be implemented through the following measures: Enforcing the Principle of Least Privilege - Implementation: Assign users only the minimum permissions required to perform their job functions. Regularly audit accounts to ensure no excess permissions are granted. - Use Case: Reduces the risk of privilege escalation by ensuring accounts cannot perform unauthorized actions. Implementing Strong Password Policies - Implementation: Enforce password complexity requirements (e.g., length, character types). Require password expiration every 90 days and disallow password reuse. - Use Case: Prevents adversaries from gaining unauthorized access through password guessing or brute force attacks. Managing Dormant and Orphaned Accounts - Implementation: Implement automated workflows to disable accounts after a set period of inactivity (e.g., 30 days). Remove orphaned accounts (e.g., accounts without an assigned owner) during regular account audits. - Use Case: Eliminates dormant accounts that could be exploited by attackers. Account Lockout Policies - Implementation: Configure account lockout thresholds (e.g., lock accounts after five failed login attempts). Set lockout durations to a minimum of 15 minutes. - Use Case: Mitigates automated attack techniques that rely on repeated login attempts. Multi-Factor Authentication (MFA) for High-Risk Accounts - Implementation: Require MFA for all administrative accounts and high-risk users. Use MFA mechanisms like hardware tokens, authenticator apps, or biometrics. - Use Case: Prevents unauthorized access, even if credentials are stolen. Restricting Interactive Logins - Implementation: Restrict interactive logins for privileged accounts to specific secure systems or management consoles. Use group policies to enforce logon restrictions. - Use Case: Protects sensitive accounts from misuse or exploitation. *Tools for Implementation* Built-in Tools: - Microsoft Active Directory (AD): Centralized account management and RBAC enforcement. - Group Policy Object (GPO): Enforce password policies, logon restrictions, and account lockout policies. Identity and Access Management (IAM) Tools: - Okta: Centralized user provisioning, MFA, and SSO integration. - Microsoft Azure Active Directory: Provides advanced account lifecycle management, role-based access, and conditional access policies. Privileged Account Management (PAM): - CyberArk, BeyondTrust, Thycotic: Manage and monitor privileged account usage, enforce session recording, and JIT access.

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
- M1018: https://attack.mitre.org/mitigations/M1018
- Reviewed: 2026-10-27
