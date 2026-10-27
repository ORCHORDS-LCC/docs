# Messaging Applications Technique Operationalization Review

## Reference

- Technique: **T1213.005 — Messaging Applications**

Adversaries may leverage chat and messaging applications, such as Microsoft Teams, Google Chat, and Slack, to mine valuable information. The following is a brief list of example information that may hold potential value to an adversary and may also be found on messaging applications: * Testing / development credentials (i.e., Chat Messages) * Source code snippets * Links to network shares and other internal resources * Proprietary data * Discussions about ongoing incident response efforts In addition to exfiltrating data from messaging applications, adversaries may leverage data from chat messages in order to improve their targeting - for example, by learning more about an environment or evading ongoing incident response efforts.

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
- T1213.005: https://attack.mitre.org/techniques/T1213/005
- Reviewed: 2026-10-27
