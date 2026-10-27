# APT-C-36 Technique Engineering Review

## Reference

- Technique: **G0099 — APT-C-36**

APT-C-36 is a suspected South American threat group that has engaged in espionage and financially motivated operations since at least 2018. APT-C-36 has targeted government institutions and entities in the financial, energy, and professional manufacturing sectors across Colombia and other Latin American countries.

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
- G0099: https://attack.mitre.org/groups/G0099
- Reviewed: 2026-10-27
