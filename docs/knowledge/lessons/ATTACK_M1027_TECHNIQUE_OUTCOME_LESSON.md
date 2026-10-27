# M1027 Password Policies Outcome Lesson

## Authoritative description

- Technique: **M1027 — Password Policies**

Set and enforce secure password policies for accounts to reduce the likelihood of unauthorized access. Strong password policies include enforcing password complexity, requiring regular password changes, and preventing password reuse. This mitigation can be implemented through the following measures: Windows Systems: - Use Group Policy Management Console (GPMC) to configure: - Minimum password length (e.g., 12+ characters). - Password complexity requirements. - Password history (e.g., disallow last 24 passwords). - Account lockout duration and thresholds. Linux Systems: - Configure Pluggable Authentication Modules (PAM): - Use `pam_pwquality` to enforce complexity and length requirements. - Implement `pam_tally2` or `pam_faillock` for account lockouts. - Use `pwunconv` to disable password reuse. Password Managers: - Enforce usage of enterprise password managers (e.g., Bitwarden, 1Password, LastPass) to generate and store strong passwords. Password Blacklisting: - Use tools like Have I Been Pwned password checks or NIST-based blacklist solutions to prevent users from setting compromised passwords. Regular Auditing: - Periodically audit password policies and account configurations to ensure compliance using tools like LAPS (Local Admin Password Solution) and vulnerability scanners. *Tools for Implementation* Windows: - Group Policy Management Console (GPMC): Enforce password policies. - Microsoft Local Administrator Password Solution (LAPS): Enforce random, unique admin passwords. Linux/macOS: - PAM Modules (pam_pwquality, pam_tally2, pam_faillock): Enforce password rules. - Lynis: Audit password policies and system configurations. Cross-Platform: - Password Managers (Bitwarden, 1Password, KeePass): Manage and enforce strong passwords. - Have I Been Pwned API: Prevent the use of breached passwords. - NIST SP 800-63B compliant tools: Enforce password guidelines and blacklisting.

## Reusable lesson

This technique should be treated as an explicit review question when it is relevant to the system or organisation, rather than assumed to be covered by a generic control statement or by tooling that reports a related signal.

## Apply the lesson

1. Define the real scope before judging coverage.
2. Inspect current technical, process, governance, or operational evidence.
3. Separate documented intent from verified behaviour.
4. Record partial coverage and unresolved gaps instead of converting them into a pass.
5. Revisit when the underlying scope, threat environment, technology, suppliers, or mission materially changes.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- M1027: https://attack.mitre.org/mitigations/M1027
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
