# Runtime Data Manipulation Mitigation Technique Operationalization Review

## Reference

- Technique: **T1494 — Runtime Data Manipulation Mitigation**

Identify critical business and system processes that may be targeted by adversaries and work to secure those systems against tampering. Prevent critical business and system processes from being replaced, overwritten, or reconfigured to load potentially malicious code. Identify potentially malicious software and audit and/or block it by using whitelisting tools, like AppLocker, or Software Restriction Policies where appropriate.

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
- T1494: https://attack.mitre.org/mitigations/T1494
- Reviewed: 2026-10-27
