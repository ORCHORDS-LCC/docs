# T1698 Indirect Prompt Injection Outcome Lesson

## Authoritative description

- Technique: **T1698 — Indirect Prompt Injection**
- Tactics: execution
- Platforms: Windows, SaaS

Adversaries may deliver malicious prompts to an LLM indirectly by embedding the prompts in content that the adversary expects may be processed by an LLM. These prompts can be included in web pages, documents, emails, tickets, code, or other sources that an agent, copilot, or other AI system may retrieve and process. When an LLM processes this content, the embedded instructions may cause the system to perform unintended behaviors. Adversaries may use indirect prompt injection to Impair Autonomous Defenses, and for unauthorized execution of any capabilities available to the LLM.

## Reusable lesson

This technique should be treated as an explicit review question when it is relevant to the system or organisation, rather than assumed to be covered by a generic control statement or by tooling that reports a related signal.

## Apply the lesson

1. Define the real scope before judging coverage.
2. Inspect current technical, process, governance, or operational evidence.
3. Separate documented intent from verified behaviour.
4. Record partial coverage and unresolved gaps instead of converting them into a pass.
5. Revisit when the underlying scope, threat environment, technology, suppliers, or mission materially changes.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1698: https://attack.mitre.org/techniques/T1698
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
