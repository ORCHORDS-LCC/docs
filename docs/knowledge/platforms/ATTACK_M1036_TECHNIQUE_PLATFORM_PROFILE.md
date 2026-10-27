# Account Use Policies Technique Platform Profile

## Reference

- Technique: **M1036 — Account Use Policies**
- Platforms named in the source: not stated

Account Use Policies help mitigate unauthorized access by configuring and enforcing rules that govern how and when accounts can be used. These policies include enforcing account lockout mechanisms, restricting login times, and setting inactivity timeouts. Proper configuration of these policies reduces the risk of brute-force attacks, credential theft, and unauthorized access by limiting the opportunities for malicious actors to exploit accounts. This mitigation can be implemented through the following measures: Account Lockout Policies: - Implementation: Configure account lockout settings so that after a defined number of failed login attempts (e.g., 3-5 attempts), the account is locked for a specific time period (e.g., 15 minutes) or requires an administrator to unlock it. - Use Case: This prevents brute-force attacks by limiting how many incorrect password attempts can be made before the account is temporarily disabled, reducing the likelihood of an attacker successfully guessing a password. Login Time Restrictions: - Implementation: Set up login time policies to restrict when users or groups can log into systems. For example, only allowing login during standard business hours (e.g., 8 AM to 6 PM) for non-administrative accounts. - Use Case: This prevents unauthorized access outside of approved working hours, where login attempts might be more suspicious or harder to monitor. For example, if an account that is only supposed to be active during the day logs in at 2 AM, it should raise an alert or be blocked. Inactivity Timeout and Session Termination: - Implementation: Enforce session timeouts after a period of inactivity (e.g., 10-15 minutes) and require users to re-authenticate if they wish to resume the session. - Use Case: This policy prevents attackers from hijacking active sessions left unattended. For example, if an employee walks away from their computer without locking it, an attacker with physical access to the system would be unable to exploit the session. Password Aging Policies: - Implementation: Enforce password aging rules, requiring users to change their passwords after a defined period (e.g., 90 days) and ensure passwords are not reused by maintaining a password history. - Use Case: This limits the risk of compromised passwords being used indefinitely. Regular password changes make it more difficult for attackers to reuse stolen credentials. Account Expiration and Deactivation: - Implementation: Configure user accounts, especially for temporary or contract workers, to automatically expire after a set date or event. Accounts that remain unused for a specific period should be deactivated automatically. - Use Case: This prevents dormant accounts from becoming an attack vector. For example, an attacker can exploit unused accounts if they are not properly monitored or deactivated. **Tools for Implementation**: - Group Policy Objects (GPOs) in Windows: To enforce account lockout thresholds, login time restrictions, session timeouts, and password policies. - Identity and Access Management (IAM) solutions: For centralized management of user accounts, session policies, and automated deactivation of accounts. - Security Information and Event Management (SIEM) platforms: To monitor and alert on unusual login activity, such as failed logins or out-of-hours access attempts. - Multi-Factor Authentication (MFA) Tools: To further enforce secure login attempts, preventing brute-force or credential stuffing attacks.

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
- M1036: https://attack.mitre.org/mitigations/M1036
- Reviewed: 2026-10-27
