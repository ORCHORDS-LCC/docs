# SAML Tokens Technique Engineering Review

## Reference

- Technique: **T1606.002 — SAML Tokens**

An adversary may forge SAML tokens with any permissions claims and lifetimes if they possess a valid SAML token-signing certificate. The default lifetime of a SAML token is one hour, but the validity period can be specified in the NotOnOrAfter value of the conditions ... element in a token. This value can be changed using the AccessTokenLifetime in a LifetimeTokenPolicy. Forged SAML tokens enable adversaries to authenticate across services that use SAML 2.0 as an SSO (single sign-on) mechanism. An adversary may utilize Private Keys to compromise an organization's token-signing certificate to create forged SAML tokens. If the adversary has sufficient permissions to establish a new federation trust with their own Active Directory Federation Services (AD FS) server, they may instead generate their own trusted token-signing certificate. This differs from Steal Application Access Token and other similar behaviors in that the tokens are new and forged by the adversary, rather than stolen or intercepted from legitimate users. An adversary may gain administrative Entra ID privileges if a SAML token is forged which claims to represent a highly privileged account. This may lead to Use Alternate Authentication Material, which may bypass multi-factor and other authentication protection mechanisms.

## Engineering review

1. Identify the engineering boundary where the technique would apply: the component, the service, or the deployment.
2. Review the design decision that would prevent the technique, and record the alternative considered.
3. Review the implementation evidence for the preventive control.
4. Review the test coverage that would fail if the control regressed.
5. Review the observability: which signal would show the control is not operating.
6. Record the residual risk where prevention is not achievable, and the detection that compensates.

## Review evidence

- the design record for the preventive decision;
- the implementation or configuration evidence;
- the test record showing the control is exercised;
- the observability mapping.

## Limitations

An engineering review describes what the design and the implementation evidence show. It does not claim the technique has been addressed in production.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1606.002: https://attack.mitre.org/techniques/T1606/002
- Reviewed: 2026-10-27
