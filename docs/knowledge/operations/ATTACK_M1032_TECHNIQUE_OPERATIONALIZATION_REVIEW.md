# Multi-factor Authentication Technique Operationalization Review

## Reference

- Technique: **M1032 — Multi-factor Authentication**

Multi-Factor Authentication (MFA) enhances security by requiring users to provide at least two forms of verification to prove their identity before granting access. These factors typically include: - *Something you know*: Passwords, PINs. - *Something you have*: Physical tokens, smartphone authenticator apps. - *Something you are*: Biometric data such as fingerprints, facial recognition, or retinal scans. Implementing MFA across all critical systems and services ensures robust protection against account takeover and unauthorized access. This mitigation can be implemented through the following measures: Identity and Access Management (IAM): - Use IAM solutions like Azure Active Directory, Okta, or AWS IAM to enforce MFA policies for all user logins, especially for privileged roles. - Enable conditional access policies to enforce MFA for risky sign-ins (e.g., unfamiliar devices, geolocations). - Enable Conditional Access policies to only allow logins from trusted devices, such as those enrolled in Intune or joined via Hybrid/Entra. Authentication Tools and Methods: - Use authenticator applications such as Google Authenticator, Microsoft Authenticator, or Authy for time-based one-time passwords (TOTP). - Deploy hardware-based tokens like YubiKey, RSA SecurID, or smart cards for additional security. - Enforce biometric authentication for compatible devices and applications. Secure Legacy Systems: - Integrate MFA solutions with older systems using third-party tools like Duo Security or Thales SafeNet. - Enable RADIUS/NPS servers to facilitate MFA for VPNs, RDP, and other network logins. Monitoring and Alerting: - Use SIEM tools to monitor failed MFA attempts, login anomalies, or brute-force attempts against MFA systems. - Implement alerts for suspicious MFA activities, such as repeated failed codes or new device registrations. Training and Policy Enforcement: - Educate employees on the importance of MFA and secure authenticator usage. - Enforce policies that require MFA on all critical systems, especially for remote access, privileged accounts, and cloud applications.

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
- M1032: https://attack.mitre.org/mitigations/M1032
- Reviewed: 2026-10-27
