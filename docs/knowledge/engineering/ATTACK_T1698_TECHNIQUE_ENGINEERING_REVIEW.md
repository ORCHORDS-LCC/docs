# Indirect Prompt Injection Technique Engineering Review

## Reference

- Technique: **T1698 — Indirect Prompt Injection**

Adversaries may deliver malicious prompts to an LLM indirectly by embedding the prompts in content that the adversary expects may be processed by an LLM. These prompts can be included in web pages, documents, emails, tickets, code, or other sources that an agent, copilot, or other AI system may retrieve and process. When an LLM processes this content, the embedded instructions may cause the system to perform unintended behaviors. Adversaries may use indirect prompt injection to Impair Autonomous Defenses, and for unauthorized execution of any capabilities available to the LLM.

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
- T1698: https://attack.mitre.org/techniques/T1698
- Reviewed: 2026-10-27
