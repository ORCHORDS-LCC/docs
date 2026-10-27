# NTFS File Attributes Mitigation Technique Engineering Review

## Reference

- Technique: **T1096 — NTFS File Attributes Mitigation**

It may be difficult or inadvisable to block access to EA and ADSs. Efforts should be focused on preventing potentially malicious software from running. Identify and block potentially malicious software that may contain functionality to hide information in EA and ADSs by using whitelisting tools like AppLocker or Software Restriction Policies where appropriate. Consider adjusting read and write permissions for NTFS EA, though this should be tested to ensure routine OS operations are not impeded.

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
- T1096: https://attack.mitre.org/mitigations/T1096
- Reviewed: 2026-10-27
