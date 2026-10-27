# Web Cookies Technique Engineering Review

## Reference

- Technique: **T1606.001 — Web Cookies**

Adversaries may forge web cookies that can be used to gain access to web applications or Internet services. Web applications and services (hosted in cloud SaaS environments or on-premise servers) often use session cookies to authenticate and authorize user access. Adversaries may generate these cookies in order to gain access to web resources. This differs from Steal Web Session Cookie and other similar behaviors in that the cookies are new and forged by the adversary, rather than stolen or intercepted from legitimate users. Most common web applications have standardized and documented cookie values that can be generated using provided tools or interfaces. The generation of web cookies often requires secret values, such as passwords, Private Keys, or other cryptographic seed values. Once forged, adversaries may use these web cookies to access resources (Web Session Cookie), which may bypass multi-factor and other authentication protection mechanisms.

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
- T1606.001: https://attack.mitre.org/techniques/T1606/001
- Reviewed: 2026-10-27
