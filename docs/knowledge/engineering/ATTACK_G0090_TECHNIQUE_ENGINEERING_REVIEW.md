# WIRTE Technique Engineering Review

## Reference

- Technique: **G0090 — WIRTE**

WIRTE is a cyberespionage actor, believed to be a subgroup of the Hamas-affiliated Gaza Cybergang, that has been active since at least August 2018. WIRTE has targeted diplomatic, financial, military, legal, and technology organizations across the Middle East, North Africa, and in Europe to gather intelligence. WIRTE has remained persistently active despite the ongoing Israel-Hamas conflict and has expanded their operations to include wiper malware attacks against Israeli targets.

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
- G0090: https://attack.mitre.org/groups/G0090
- Reviewed: 2026-10-27
