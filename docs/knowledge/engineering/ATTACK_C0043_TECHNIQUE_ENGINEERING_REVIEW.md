# Indian Critical Infrastructure Intrusions Technique Engineering Review

## Reference

- Technique: **C0043 — Indian Critical Infrastructure Intrusions**

Indian Critical Infrastructure Intrusions is a sequence of intrusions from 2021 through early 2022 linked to People’s Republic of China (PRC) threat actors, particularly RedEcho and Threat Activity Group 38 (TAG38). The intrusions appear focused on IT system breach in Indian electric utility entities and logistics firms, as well as potentially managed service providers operating within India. Although focused on OT-operating entities, there is no evidence this campaign was able to progress beyond IT breach and information gathering to OT environment access.

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
- C0043: https://attack.mitre.org/campaigns/C0043
- Reviewed: 2026-10-27
