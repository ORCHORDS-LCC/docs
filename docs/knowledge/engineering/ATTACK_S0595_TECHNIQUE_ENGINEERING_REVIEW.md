# ThiefQuest Technique Engineering Review

## Reference

- Technique: **S0595 — ThiefQuest**

ThiefQuest is a virus, data stealer, and wiper that presents itself as ransomware targeting macOS systems. ThiefQuest was first seen in 2020 distributed via trojanized pirated versions of popular macOS software on Russian forums sharing torrent links. Even though ThiefQuest presents itself as ransomware, since the dynamically generated encryption key is never sent to the attacker it may be more appropriately thought of as a form of wiper malware.

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
- S0595: https://attack.mitre.org/software/S0595
- Reviewed: 2026-10-27
