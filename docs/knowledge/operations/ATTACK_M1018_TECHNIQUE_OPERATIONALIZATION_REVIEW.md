# User Account Management Technique Operationalization Review

## Reference

- Technique: **M1018 — User Account Management**

User Account Management involves implementing and enforcing policies for the lifecycle of user accounts, including creation, modification, and deactivation. Proper account management reduces the attack surface by limiting unauthorized access, managing account privileges, and ensuring accounts are used according to organizational policies. This mitigation can be implemented through the following measures: Enforcing the Principle of Least Privilege - Implementation: Assign users only the minimum permissions required to perform their job functions. Regularly audit accounts to ensure no excess permissions are granted. - Use Case: Reduces the risk of privilege escalation by ensuring accounts cannot perform unauthorized actions. Implementing Strong Password Policies - Implementation: Enforce password complexity requirements (e.g., length, character types). Require password expiration every 90 days and disallow password reuse. - Use Case: Prevents adversaries from gaining unauthorized access through password guessing or brute force attacks. Managing Dormant and Orphaned Accounts - Implementation: Implement automated workflows to disable accounts after a set period of inactivity (e.g., 30 days). Remove orphaned accounts (e.g., accounts without an assigned owner) during regular account audits. - Use Case: Eliminates dormant accounts that could be exploited by attackers. Account Lockout Policies - Implementation: Configure account lockout thresholds (e.g., lock accounts after five failed login attempts). Set lockout durations to a minimum of 15 minutes. - Use Case: Mitigates automated attack techniques that rely on repeated login attempts. Multi-Factor Authentication (MFA) for High-Risk Accounts - Implementation: Require MFA for all administrative accounts and high-risk users. Use MFA mechanisms like hardware tokens, authenticator apps, or biometrics. - Use Case: Prevents unauthorized access, even if credentials are stolen. Restricting Interactive Logins - Implementation: Restrict interactive logins for privileged accounts to specific secure systems or management consoles. Use group policies to enforce logon restrictions. - Use Case: Protects sensitive accounts from misuse or exploitation. *Tools for Implementation* Built-in Tools: - Microsoft Active Directory (AD): Centralized account management and RBAC enforcement. - Group Policy Object (GPO): Enforce password policies, logon restrictions, and account lockout policies. Identity and Access Management (IAM) Tools: - Okta: Centralized user provisioning, MFA, and SSO integration. - Microsoft Azure Active Directory: Provides advanced account lifecycle management, role-based access, and conditional access policies. Privileged Account Management (PAM): - CyberArk, BeyondTrust, Thycotic: Manage and monitor privileged account usage, enforce session recording, and JIT access.

## Operationalization review

1. Record the operational scope: which services, environments, and data the technique could affect.
2. Record the runbook that would be executed, and its owner.
3. Record the telemetry the runbook depends on, and whether it is retained long enough to investigate.
4. Record the detection that would surface the technique before or after it has an effect.
5. Record the recovery path, and the evidence that recovery has been rehearsed.
6. Record the residual operational risk where the runbook depends on a manual step.

## Review evidence

- the runbook and its owner;
- the telemetry retention and coverage record;
- the detection mapping;
- the exercise or rehearsal record.

## Limitations

An operationalization review describes the runbook and the evidence around it. It does not claim the technique has been prevented or detected in a live environment.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- M1018: https://attack.mitre.org/mitigations/M1018
- Reviewed: 2026-10-27
