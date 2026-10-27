# T1606.002 SAML Tokens Outcome Lesson

## Authoritative description

- Technique: **T1606.002 — SAML Tokens**
- Tactics: credential-access
- Platforms: SaaS, Windows, IaaS, Office Suite, Identity Provider

An adversary may forge SAML tokens with any permissions claims and lifetimes if they possess a valid SAML token-signing certificate. The default lifetime of a SAML token is one hour, but the validity period can be specified in the <code>NotOnOrAfter</code> value of the <code>conditions ...</code> element in a token. This value can be changed using the <code>AccessTokenLifetime</code> in a <code>LifetimeTokenPolicy</code>. Forged SAML tokens enable adversaries to authenticate across services that use SAML 2.0 as an SSO (single sign-on) mechanism. An adversary may utilize Private Keys to compromise an organization's token-signing certificate to create forged SAML tokens. If the adversary has sufficient permissions to establish a new federation trust with their own Active Directory Federation Services (AD FS) server, they may instead generate their own trusted token-signing certificate. This differs from Steal Application Access Token and other similar behaviors in that the tokens are new and forged by the adversary, rather than stolen or intercepted from legitimate users. An adversary may gain administrative Entra ID privileges if a SAML token is forged which claims to represent a highly privileged account. This may lead to Use Alternate Authentication Material, which may bypass multi-factor and other authentication protection mechanisms.

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
- T1606.002: https://attack.mitre.org/techniques/T1606/002
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
