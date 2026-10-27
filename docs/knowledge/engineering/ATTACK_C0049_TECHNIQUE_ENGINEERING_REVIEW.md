# Leviathan Australian Intrusions Technique Engineering Review

## Reference

- Technique: **C0049 — Leviathan Australian Intrusions**

Leviathan Australian Intrusions consisted of at least two long-term intrusions against victims in Australia by Leviathan, relying on similar tradecraft such as external service exploitation followed by extensive credential capture and re-use to enable privilege escalation and lateral movement. Leviathan Australian Intrusions were focused on exfiltrating sensitive data including valid credentials for the victim organizations.

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
- C0049: https://attack.mitre.org/campaigns/C0049
- Reviewed: 2026-10-27
