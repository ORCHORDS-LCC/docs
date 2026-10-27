# Password Policies Technique Platform Profile

## Reference

- Technique: **M1027 — Password Policies**
- Platforms named in the source: not stated

Set and enforce secure password policies for accounts to reduce the likelihood of unauthorized access. Strong password policies include enforcing password complexity, requiring regular password changes, and preventing password reuse. This mitigation can be implemented through the following measures: Windows Systems: - Use Group Policy Management Console (GPMC) to configure: - Minimum password length (e.g., 12+ characters). - Password complexity requirements. - Password history (e.g., disallow last 24 passwords). - Account lockout duration and thresholds. Linux Systems: - Configure Pluggable Authentication Modules (PAM): - Use `pam_pwquality` to enforce complexity and length requirements. - Implement `pam_tally2` or `pam_faillock` for account lockouts. - Use `pwunconv` to disable password reuse. Password Managers: - Enforce usage of enterprise password managers (e.g., Bitwarden, 1Password, LastPass) to generate and store strong passwords. Password Blacklisting: - Use tools like Have I Been Pwned password checks or NIST-based blacklist solutions to prevent users from setting compromised passwords. Regular Auditing: - Periodically audit password policies and account configurations to ensure compliance using tools like LAPS (Local Admin Password Solution) and vulnerability scanners. *Tools for Implementation* Windows: - Group Policy Management Console (GPMC): Enforce password policies. - Microsoft Local Administrator Password Solution (LAPS): Enforce random, unique admin passwords. Linux/macOS: - PAM Modules (pam_pwquality, pam_tally2, pam_faillock): Enforce password rules. - Lynis: Audit password policies and system configurations. Cross-Platform: - Password Managers (Bitwarden, 1Password, KeePass): Manage and enforce strong passwords. - Have I Been Pwned API: Prevent the use of breached passwords. - NIST SP 800-63B compliant tools: Enforce password guidelines and blacklisting.

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
- M1027: https://attack.mitre.org/mitigations/M1027
- Reviewed: 2026-10-27
