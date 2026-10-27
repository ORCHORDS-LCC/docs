# Ember Bear Technique Engineering Review

## Reference

- Technique: **G1003 — Ember Bear**

Ember Bear is a Russian state-sponsored cyber espionage group that has been active since at least 2020, linked to Russia's General Staff Main Intelligence Directorate (GRU) 161st Specialist Training Center (Unit 29155). Ember Bear has primarily focused operations against Ukrainian government and telecommunication entities, but has also operated against critical infrastructure entities in Europe and the Americas. Ember Bear conducted the WhisperGate destructive wiper attacks against Ukraine in early 2022. There is some confusion as to whether Ember Bear overlaps with another Russian-linked entity referred to as Saint Bear. At present available evidence strongly suggests these are distinct activities with different behavioral profiles.

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
- G1003: https://attack.mitre.org/groups/G1003
- Reviewed: 2026-10-27
