# Modify Registry Mitigation Technique Engineering Review

## Reference

- Technique: **T1112 — Modify Registry Mitigation**

Misconfiguration of permissions in the Registry may lead to opportunities for an adversary to execute code, like through Service Registry Permissions Weakness. Ensure proper permissions are set for Registry hives to prevent users from modifying keys for system components that may lead to privilege escalation. Identify and block unnecessary system utilities or potentially malicious software that may be used to modify the Registry by using whitelisting tools like AppLocker or Software Restriction Policies where appropriate.

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
- T1112: https://attack.mitre.org/mitigations/T1112
- Reviewed: 2026-10-27
