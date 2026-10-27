# M1032 Multi-factor Authentication Outcome Lesson

## Authoritative description

- Technique: **M1032 — Multi-factor Authentication**

Multi-Factor Authentication (MFA) enhances security by requiring users to provide at least two forms of verification to prove their identity before granting access. These factors typically include: - *Something you know*: Passwords, PINs. - *Something you have*: Physical tokens, smartphone authenticator apps. - *Something you are*: Biometric data such as fingerprints, facial recognition, or retinal scans. Implementing MFA across all critical systems and services ensures robust protection against account takeover and unauthorized access. This mitigation can be implemented through the following measures: Identity and Access Management (IAM): - Use IAM solutions like Azure Active Directory, Okta, or AWS IAM to enforce MFA policies for all user logins, especially for privileged roles. - Enable conditional access policies to enforce MFA for risky sign-ins (e.g., unfamiliar devices, geolocations). - Enable Conditional Access policies to only allow logins from trusted devices, such as those enrolled in Intune or joined via Hybrid/Entra. Authentication Tools and Methods: - Use authenticator applications such as Google Authenticator, Microsoft Authenticator, or Authy for time-based one-time passwords (TOTP). - Deploy hardware-based tokens like YubiKey, RSA SecurID, or smart cards for additional security. - Enforce biometric authentication for compatible devices and applications. Secure Legacy Systems: - Integrate MFA solutions with older systems using third-party tools like Duo Security or Thales SafeNet. - Enable RADIUS/NPS servers to facilitate MFA for VPNs, RDP, and other network logins. Monitoring and Alerting: - Use SIEM tools to monitor failed MFA attempts, login anomalies, or brute-force attempts against MFA systems. - Implement alerts for suspicious MFA activities, such as repeated failed codes or new device registrations. Training and Policy Enforcement: - Educate employees on the importance of MFA and secure authenticator usage. - Enforce policies that require MFA on all critical systems, especially for remote access, privileged accounts, and cloud applications.

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
- M1032: https://attack.mitre.org/mitigations/M1032
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
