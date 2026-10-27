# TeamPCP Technique Engineering Review

## Reference

- Technique: **G1056 — TeamPCP**

TeamPCP is a financially-motivated, cloud-native threat group that has been active since at least September 2025. Initially focused on ransomware and cryptocurrency theft, TeamPCP shifted in early 2026 to systematic, worm-driven credential theft and software supply chain attacks targeting Continuous Integration and Continuous Delivery (CI/CD) workflows. TeamPCP has monetized access through extortion and through partnerships with ransomware actors including Vect and CipherForce.

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
- G1056: https://attack.mitre.org/groups/G1056
- Reviewed: 2026-10-27
