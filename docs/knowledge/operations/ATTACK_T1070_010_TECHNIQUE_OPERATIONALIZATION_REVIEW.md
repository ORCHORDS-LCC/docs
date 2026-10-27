# Relocate Malware Technique Operationalization Review

## Reference

- Technique: **T1070.010 — Relocate Malware**

Once a payload is delivered, adversaries may reproduce copies of the same malware on the victim system to remove evidence of their presence and/or avoid defenses. Copying malware payloads to new locations may also be combined with File Deletion to cleanup older artifacts. Relocating malware may be a part of many actions intended to evade defenses. For example, adversaries may copy and rename payloads to better blend into the local environment (i.e., Match Legitimate Resource Name or Location). Payloads may also be repositioned to target File/Path Exclusions as well as specific locations associated with establishing Persistence. Relocating malicious payloads may also hinder defensive analysis, especially to separate these payloads from earlier events (such as User Execution and Phishing) that may have generated alerts or otherwise drawn attention from defenders. Moving payloads into target directories does not alter the Creation timestamp, thereby evading detection logic reliant on modifications to this artifact (i.e., Timestomp).

## Operationalization review

1. Record the operational scope: which services, environments, and data the technique could affect.
2. Record the runbook that would be executed, and its owner.
3. Record the telemetry the runbook depends on, and whether it is retained long enough to investigate.
4. Record the detection that would surface the technique before or after it has an effect.
5. Record the recovery path, and the evidence that recovery has been rehearsed.
6. Record the residual operational risk where the runbook depends on a manual step.

## Review evidence

- the runbook and its owner;
- the telemetry retention and coverage record;
- the detection mapping;
- the exercise or rehearsal record.

## Limitations

An operationalization review describes the runbook and the evidence around it. It does not claim the technique has been prevented or detected in a live environment.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1070.010: https://attack.mitre.org/techniques/T1070/010
- Reviewed: 2026-10-27
