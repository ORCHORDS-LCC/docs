# Web Cookies Technique Response Playbook

## Target technique

**T1606.001 — Web Cookies**

- Tactics: credential-access
- Platforms: Linux, macOS, Windows, SaaS, IaaS

Adversaries may forge web cookies that can be used to gain access to web applications or Internet services. Web applications and services (hosted in cloud SaaS environments or on-premise servers) often use session cookies to authenticate and authorize user access. Adversaries may generate these cookies in order to gain access to web resources. This differs from Steal Web Session Cookie and other similar behaviors in that the cookies are new and forged by the adversary, rather than stolen or intercepted from legitimate users. Most common web applications have standardized and documented cookie values that can be generated using provided tools or interfaces. The generation of web cookies often requires secret values, such as passwords, Private Keys, or other cryptographic seed values. Once forged, adversaries may use these web cookies to access resources (Web Session Cookie), which may bypass multi-factor and other authentication protection mechanisms.

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
- T1606.001: https://attack.mitre.org/techniques/T1606/001
- Reviewed: 2026-10-27
