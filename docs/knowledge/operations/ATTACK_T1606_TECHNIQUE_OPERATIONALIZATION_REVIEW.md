# Forge Web Credentials Technique Operationalization Review

## Reference

- Technique: **T1606 — Forge Web Credentials**

Adversaries may forge credential materials that can be used to gain access to web applications or Internet services. Web applications and services (hosted in cloud SaaS environments or on-premise servers) often use session cookies, tokens, or other materials to authenticate and authorize user access. Adversaries may generate these credential materials in order to gain access to web resources. This differs from Steal Web Session Cookie, Steal Application Access Token, and other similar behaviors in that the credentials are new and forged by the adversary, rather than stolen or intercepted from legitimate users. The generation of web credentials often requires secret values, such as passwords, Private Keys, or other cryptographic seed values. Adversaries may also forge tokens by taking advantage of features such as the `AssumeRole` and `GetFederationToken` APIs in AWS, which allow users to request temporary security credentials (i.e., Temporary Elevated Cloud Access), or the `zmprov gdpak` command in Zimbra, which generates a pre-authentication key that can be used to generate tokens for any user in the domain. Once forged, adversaries may use these web credentials to access resources (ex: Use Alternate Authentication Material), which may bypass multi-factor and other authentication protection mechanisms.

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
- T1606: https://attack.mitre.org/techniques/T1606
- Reviewed: 2026-10-27
