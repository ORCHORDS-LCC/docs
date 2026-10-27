# Privileged Account Management Technique Platform Profile

## Reference

- Technique: **M1026 — Privileged Account Management**
- Platforms named in the source: not stated

Privileged Account Management focuses on implementing policies, controls, and tools to securely manage privileged accounts (e.g., SYSTEM, root, or administrative accounts). This includes restricting access, limiting the scope of permissions, monitoring privileged account usage, and ensuring accountability through logging and auditing.This mitigation can be implemented through the following measures: Account Permissions and Roles: - Implement RBAC and least privilege principles to allocate permissions securely. - Use tools like Active Directory Group Policies to enforce access restrictions. Credential Security: - Deploy password vaulting tools like CyberArk, HashiCorp Vault, or KeePass for secure storage and rotation of credentials. - Enforce password policies for complexity, uniqueness, and expiration using tools like Microsoft Group Policy Objects (GPO). Multi-Factor Authentication (MFA): - Enforce MFA for all privileged accounts using Duo Security, Okta, or Microsoft Azure AD MFA. Privileged Access Management (PAM): - Use PAM solutions like CyberArk, BeyondTrust, or Thycotic to manage, monitor, and audit privileged access. Auditing and Monitoring: - Integrate activity monitoring into your SIEM (e.g., Splunk or QRadar) to detect and alert on anomalous privileged account usage. Just-In-Time Access: - Deploy JIT solutions like Azure Privileged Identity Management (PIM) or configure ephemeral roles in AWS and GCP to grant time-limited elevated permissions. *Tools for Implementation* Privileged Access Management (PAM): - CyberArk, BeyondTrust, Thycotic, HashiCorp Vault. Credential Management: - Microsoft LAPS (Local Admin Password Solution), Password Safe, HashiCorp Vault, KeePass. Multi-Factor Authentication: - Duo Security, Okta, Microsoft Azure MFA, Google Authenticator. Linux Privilege Management: - sudo configuration, SELinux, AppArmor. Just-In-Time Access: - Azure Privileged Identity Management (PIM), AWS IAM Roles with session constraints, GCP Identity-Aware Proxy.

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
- M1026: https://attack.mitre.org/mitigations/M1026
- Reviewed: 2026-10-27
