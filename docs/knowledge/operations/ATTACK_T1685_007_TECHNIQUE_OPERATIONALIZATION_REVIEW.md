# Impair Autonomous Defenses Technique Operationalization Review

## Reference

- Technique: **T1685.007 — Impair Autonomous Defenses**

Adversaries may use methods like Indirect Prompt Injection to disrupt, disable, or otherwise impair autonomous defensive capabilities such as LLM-assisted processing of malware, artifacts, or activity. This behavior may cause a system to ignore data, fail to alert on malicious activity, abort analysis, or to be disabled completely. Adversaries may include content in malware implants that mimic an LLM prompt scaffold that contains fake system messages in order to convince the LLM that it has encountered an error. Depending on the type of error, the LLM may abort analysis, truncate, or refuse to continue. Adversaries may also embed prompts in malware intended to stop agents or systems from analyzing the malware.

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
- T1685.007: https://attack.mitre.org/techniques/T1685/007
- Reviewed: 2026-10-27
