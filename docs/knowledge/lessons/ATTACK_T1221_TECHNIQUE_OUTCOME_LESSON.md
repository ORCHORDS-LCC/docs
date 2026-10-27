# T1221 Template Injection Mitigation Outcome Lesson

## Authoritative description

- Technique: **T1221 — Template Injection Mitigation**

Consider disabling Microsoft Office macros/active content to prevent the execution of malicious payloads in documents , though this setting may not mitigate the Forced Authentication use for this technique. Because this technique involves user interaction on the endpoint, it's difficult to fully mitigate. However, there are potential mitigations including training users to identify social engineering techniques and spearphishing emails. Network/Host intrusion prevention systems, antivirus, and detonation chambers can be employed to prevent documents from fetching and/or executing malicious payloads.

## Reusable lesson

This technique should be treated as an explicit review question when it is relevant to the system or organisation, rather than assumed to be covered by a generic control statement or by tooling that reports a related signal.

## Apply the lesson

1. Define the real scope before judging coverage.
2. Inspect current technical, process, governance, or operational evidence.
3. Separate documented intent from verified behaviour.
4. Record partial coverage and unresolved gaps instead of converting them into a pass.
5. Revisit when the underlying scope, threat environment, technology, suppliers, or mission materially changes.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1221: https://attack.mitre.org/mitigations/T1221
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
