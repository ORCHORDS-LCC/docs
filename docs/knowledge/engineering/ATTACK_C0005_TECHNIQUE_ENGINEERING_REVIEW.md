# Operation Spalax Technique Engineering Review

## Reference

- Technique: **C0005 — Operation Spalax**

Operation Spalax was a campaign that primarily targeted Colombian government organizations and private companies, particularly those associated with the energy and metallurgical industries. The Operation Spalax threat actors distributed commodity malware and tools using generic phishing topics related to COVID-19, banking, and law enforcement action. Security researchers noted indicators of compromise and some infrastructure overlaps with other campaigns dating back to April 2018, including at least one separately attributed to APT-C-36, however identified enough differences to report this as separate, unattributed activity.

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
- C0005: https://attack.mitre.org/campaigns/C0005
- Reviewed: 2026-10-27
