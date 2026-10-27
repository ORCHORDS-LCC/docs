# Multi-factor Authentication Technique Platform Profile

## Reference

- Technique: **M1032 — Multi-factor Authentication**
- Platforms named in the source: not stated

Multi-Factor Authentication (MFA) enhances security by requiring users to provide at least two forms of verification to prove their identity before granting access. These factors typically include: - *Something you know*: Passwords, PINs. - *Something you have*: Physical tokens, smartphone authenticator apps. - *Something you are*: Biometric data such as fingerprints, facial recognition, or retinal scans. Implementing MFA across all critical systems and services ensures robust protection against account takeover and unauthorized access. This mitigation can be implemented through the following measures: Identity and Access Management (IAM): - Use IAM solutions like Azure Active Directory, Okta, or AWS IAM to enforce MFA policies for all user logins, especially for privileged roles. - Enable conditional access policies to enforce MFA for risky sign-ins (e.g., unfamiliar devices, geolocations). - Enable Conditional Access policies to only allow logins from trusted devices, such as those enrolled in Intune or joined via Hybrid/Entra. Authentication Tools and Methods: - Use authenticator applications such as Google Authenticator, Microsoft Authenticator, or Authy for time-based one-time passwords (TOTP). - Deploy hardware-based tokens like YubiKey, RSA SecurID, or smart cards for additional security. - Enforce biometric authentication for compatible devices and applications. Secure Legacy Systems: - Integrate MFA solutions with older systems using third-party tools like Duo Security or Thales SafeNet. - Enable RADIUS/NPS servers to facilitate MFA for VPNs, RDP, and other network logins. Monitoring and Alerting: - Use SIEM tools to monitor failed MFA attempts, login anomalies, or brute-force attempts against MFA systems. - Implement alerts for suspicious MFA activities, such as repeated failed codes or new device registrations. Training and Policy Enforcement: - Educate employees on the importance of MFA and secure authenticator usage. - Enforce policies that require MFA on all critical systems, especially for remote access, privileged accounts, and cloud applications.

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
- M1032: https://attack.mitre.org/mitigations/M1032
- Reviewed: 2026-10-27
