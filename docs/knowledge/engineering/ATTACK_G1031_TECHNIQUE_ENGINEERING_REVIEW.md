# Saint Bear Technique Engineering Review

## Reference

- Technique: **G1031 — Saint Bear**

Saint Bear is a Russian-nexus threat actor active since early 2021, primarily targeting entities in Ukraine and Georgia. The group is notable for a specific remote access tool, Saint Bot, and information stealer, OutSteel in campaigns. Saint Bear typically relies on phishing or web staging of malicious documents and related file types for initial access, spoofing government or related entities. Saint Bear has previously been confused with Ember Bear operations, but analysis of behaviors, tools, and targeting indicates these are distinct clusters.

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
- G1031: https://attack.mitre.org/groups/G1031
- Reviewed: 2026-10-27
