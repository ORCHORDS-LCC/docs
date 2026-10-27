# Forge Web Credentials Technique Platform Profile

## Reference

- Technique: **T1606 — Forge Web Credentials**
- Platforms named in the source: SaaS, Windows, macOS, Linux, IaaS, Office Suite, Identity Provider

Adversaries may forge credential materials that can be used to gain access to web applications or Internet services. Web applications and services (hosted in cloud SaaS environments or on-premise servers) often use session cookies, tokens, or other materials to authenticate and authorize user access. Adversaries may generate these credential materials in order to gain access to web resources. This differs from Steal Web Session Cookie, Steal Application Access Token, and other similar behaviors in that the credentials are new and forged by the adversary, rather than stolen or intercepted from legitimate users. The generation of web credentials often requires secret values, such as passwords, Private Keys, or other cryptographic seed values. Adversaries may also forge tokens by taking advantage of features such as the `AssumeRole` and `GetFederationToken` APIs in AWS, which allow users to request temporary security credentials (i.e., Temporary Elevated Cloud Access), or the `zmprov gdpak` command in Zimbra, which generates a pre-authentication key that can be used to generate tokens for any user in the domain. Once forged, adversaries may use these web credentials to access resources (ex: Use Alternate Authentication Material), which may bypass multi-factor and other authentication protection mechanisms.

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
- T1606: https://attack.mitre.org/techniques/T1606
- Reviewed: 2026-10-27
