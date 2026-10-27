# Multi-factor Authentication Technique Response Playbook

## Target technique

**M1032 — Multi-factor Authentication**


Multi-Factor Authentication (MFA) enhances security by requiring users to provide at least two forms of verification to prove their identity before granting access. These factors typically include: - *Something you know*: Passwords, PINs. - *Something you have*: Physical tokens, smartphone authenticator apps. - *Something you are*: Biometric data such as fingerprints, facial recognition, or retinal scans. Implementing MFA across all critical systems and services ensures robust protection against account takeover and unauthorized access. This mitigation can be implemented through the following measures: Identity and Access Management (IAM): - Use IAM solutions like Azure Active Directory, Okta, or AWS IAM to enforce MFA policies for all user logins, especially for privileged roles. - Enable conditional access policies to enforce MFA for risky sign-ins (e.g., unfamiliar devices, geolocations). - Enable Conditional Access policies to only allow logins from trusted devices, such as those enrolled in Intune or joined via Hybrid/Entra. Authentication Tools and Methods: - Use authenticator applications such as Google Authenticator, Microsoft Authenticator, or Authy for time-based one-time passwords (TOTP). - Deploy hardware-based tokens like YubiKey, RSA SecurID, or smart cards for additional security. - Enforce biometric authentication for compatible devices and applications. Secure Legacy Systems: - Integrate MFA solutions with older systems using third-party tools like Duo Security or Thales SafeNet. - Enable RADIUS/NPS servers to facilitate MFA for VPNs, RDP, and other network logins. Monitoring and Alerting: - Use SIEM tools to monitor failed MFA attempts, login anomalies, or brute-force attempts against MFA systems. - Implement alerts for suspicious MFA activities, such as repeated failed codes or new device registrations. Training and Policy Enforcement: - Educate employees on the importance of MFA and secure authenticator usage. - Enforce policies that require MFA on all critical systems, especially for remote access, privileged accounts, and cloud applications.

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
- M1032: https://attack.mitre.org/mitigations/M1032
- Reviewed: 2026-10-27
