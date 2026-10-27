# Direct Prompt Injection Technique Operationalization Review

## Reference

- Technique: **T1699 — Direct Prompt Injection**

Adversaries may input malicious prompts directly into an LLM’s user interface. The prompts can be designed to bypass safeguards, manipulate context, override previous instructions, or coerce the LLM into unauthorized behavior. Adversaries may use direct prompt injection to Generate Content prohibited by the LLM's guardrails or to induce the system to utilize its capabilities in unintended or prohibited ways. Adversaries may achieve this by instructing the LLM to ignore previous instructions or safety rules, or by impersonating a role such as a researcher or privileged user.

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
- T1699: https://attack.mitre.org/techniques/T1699
- Reviewed: 2026-10-27
