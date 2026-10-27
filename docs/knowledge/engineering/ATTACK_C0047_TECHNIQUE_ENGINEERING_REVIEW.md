# RedDelta Modified PlugX Infection Chain Operations Technique Engineering Review

## Reference

- Technique: **C0047 — RedDelta Modified PlugX Infection Chain Operations**

RedDelta Modified PlugX Infection Chain Operations was executed by Mustang Panda from mid-2023 through the end of 2024 against multiple entities in East and Southeast Asia. RedDelta Modified PlugX Infection Chain Operations involved phishing to deliver malicious files or links to users prompting follow-on installer downloads to load PlugX on victim machines in a persistent state.

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
- C0047: https://attack.mitre.org/campaigns/C0047
- Reviewed: 2026-10-27
