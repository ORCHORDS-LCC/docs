# The Gentlemen Technique Engineering Review

## Reference

- Technique: **G1058 — The Gentlemen**

The Gentlemen is a group that maintains the The Gentlemen Ransomware-as-a-service (RaaS). The Gentlemen was first observed in mid-2025 who had posed The Gentlemen Ransomware as a closed ransomware and shortly later opened the ransomware as a RaaS to affiliates in September 2025. The Gentlemen has been affiliated with the threat group Storm-2697 and GOLD SHERWOOD.

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
- G1058: https://attack.mitre.org/groups/G1058
- Reviewed: 2026-10-27
