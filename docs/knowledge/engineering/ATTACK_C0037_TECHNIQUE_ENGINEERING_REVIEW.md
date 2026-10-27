# Water Curupira Pikabot Distribution Technique Engineering Review

## Reference

- Technique: **C0037 — Water Curupira Pikabot Distribution**

Pikabot was distributed in Water Curupira Pikabot Distribution throughout 2023 by an entity linked to BlackBasta ransomware deployment via email attachments. This activity followed the take-down of QakBot, with several technical overlaps and similarities with QakBot, indicating a possible connection. The identified activity led to the deployment of tools such as Cobalt Strike, while coinciding with campaigns delivering DarkGate and IcedID en route to ransomware deployment.

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
- C0037: https://attack.mitre.org/campaigns/C0037
- Reviewed: 2026-10-27
