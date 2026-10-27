# Remote Access Tools Mitigation Technique Engineering Review

## Reference

- Technique: **T1219 — Remote Access Tools Mitigation**

Properly configure firewalls, application firewalls, and proxies to limit outgoing traffic to sites and services used by remote access tools. Network intrusion detection and prevention systems that use network signatures may be able to prevent traffic to these services as well. Use application whitelisting to mitigate use of and installation of unapproved software.

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
- T1219: https://attack.mitre.org/mitigations/T1219
- Reviewed: 2026-10-27
