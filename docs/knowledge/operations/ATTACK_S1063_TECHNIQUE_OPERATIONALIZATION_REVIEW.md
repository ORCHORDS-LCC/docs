# Brute Ratel C4 Technique Operationalization Review

## Reference

- Technique: **S1063 — Brute Ratel C4**

Brute Ratel C4 is a commercial red-teaming and adversarial attack simulation tool that first appeared in December 2020. Brute Ratel C4 was specifically designed to avoid detection by endpoint detection and response (EDR) and antivirus (AV) capabilities, and deploys agents called badgers to enable arbitrary command execution for lateral movement, privilege escalation, and persistence. In September 2022, a cracked version of Brute Ratel C4 was leaked in the cybercriminal underground, leading to its use by threat actors.

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
- S1063: https://attack.mitre.org/software/S1063
- Reviewed: 2026-10-27
