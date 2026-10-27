# Indirect Prompt Injection Technique Operationalization Review

## Reference

- Technique: **T1698 — Indirect Prompt Injection**

Adversaries may deliver malicious prompts to an LLM indirectly by embedding the prompts in content that the adversary expects may be processed by an LLM. These prompts can be included in web pages, documents, emails, tickets, code, or other sources that an agent, copilot, or other AI system may retrieve and process. When an LLM processes this content, the embedded instructions may cause the system to perform unintended behaviors. Adversaries may use indirect prompt injection to Impair Autonomous Defenses, and for unauthorized execution of any capabilities available to the LLM.

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
- T1698: https://attack.mitre.org/techniques/T1698
- Reviewed: 2026-10-27
