# SAML Tokens Technique Platform Profile

## Reference

- Technique: **T1606.002 — SAML Tokens**
- Platforms named in the source: SaaS, Windows, IaaS, Office Suite, Identity Provider

An adversary may forge SAML tokens with any permissions claims and lifetimes if they possess a valid SAML token-signing certificate. The default lifetime of a SAML token is one hour, but the validity period can be specified in the <code>NotOnOrAfter</code> value of the <code>conditions ...</code> element in a token. This value can be changed using the <code>AccessTokenLifetime</code> in a <code>LifetimeTokenPolicy</code>. Forged SAML tokens enable adversaries to authenticate across services that use SAML 2.0 as an SSO (single sign-on) mechanism. An adversary may utilize Private Keys to compromise an organization's token-signing certificate to create forged SAML tokens. If the adversary has sufficient permissions to establish a new federation trust with their own Active Directory Federation Services (AD FS) server, they may instead generate their own trusted token-signing certificate. This differs from Steal Application Access Token and other similar behaviors in that the tokens are new and forged by the adversary, rather than stolen or intercepted from legitimate users. An adversary may gain administrative Entra ID privileges if a SAML token is forged which claims to represent a highly privileged account. This may lead to Use Alternate Authentication Material, which may bypass multi-factor and other authentication protection mechanisms.

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
- T1606.002: https://attack.mitre.org/techniques/T1606/002
- Reviewed: 2026-10-27
