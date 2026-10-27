# Password Policies Technique Operationalization Review

## Reference

- Technique: **M1027 — Password Policies**

Set and enforce secure password policies for accounts to reduce the likelihood of unauthorized access. Strong password policies include enforcing password complexity, requiring regular password changes, and preventing password reuse. This mitigation can be implemented through the following measures: Windows Systems: - Use Group Policy Management Console (GPMC) to configure: - Minimum password length (e.g., 12+ characters). - Password complexity requirements. - Password history (e.g., disallow last 24 passwords). - Account lockout duration and thresholds. Linux Systems: - Configure Pluggable Authentication Modules (PAM): - Use `pam_pwquality` to enforce complexity and length requirements. - Implement `pam_tally2` or `pam_faillock` for account lockouts. - Use `pwunconv` to disable password reuse. Password Managers: - Enforce usage of enterprise password managers (e.g., Bitwarden, 1Password, LastPass) to generate and store strong passwords. Password Blacklisting: - Use tools like Have I Been Pwned password checks or NIST-based blacklist solutions to prevent users from setting compromised passwords. Regular Auditing: - Periodically audit password policies and account configurations to ensure compliance using tools like LAPS (Local Admin Password Solution) and vulnerability scanners. *Tools for Implementation* Windows: - Group Policy Management Console (GPMC): Enforce password policies. - Microsoft Local Administrator Password Solution (LAPS): Enforce random, unique admin passwords. Linux/macOS: - PAM Modules (pam_pwquality, pam_tally2, pam_faillock): Enforce password rules. - Lynis: Audit password policies and system configurations. Cross-Platform: - Password Managers (Bitwarden, 1Password, KeePass): Manage and enforce strong passwords. - Have I Been Pwned API: Prevent the use of breached passwords. - NIST SP 800-63B compliant tools: Enforce password guidelines and blacklisting.

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
- M1027: https://attack.mitre.org/mitigations/M1027
- Reviewed: 2026-10-27
