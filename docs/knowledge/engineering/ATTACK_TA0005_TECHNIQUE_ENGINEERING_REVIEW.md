# Stealth Technique Engineering Review

## Reference

- Technique: **TA0005 — Stealth**

The adversary is trying to hide and conceal their actions, appearing as normal behavior. Stealth consists of techniques that reduce the likelihood of detection by blending in with legitimate activity or minimizing observable signals. These techniques are characterized by concealment behaviors, such as avoiding, obfuscating, or mimicking normal operations, without modifying security controls or compromising collection and monitoring feeds. The goal is to remain indistinguishable from benign activity while leaving defensive systems intact.

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
- TA0005: https://attack.mitre.org/tactics/TA0005
- Reviewed: 2026-10-27
