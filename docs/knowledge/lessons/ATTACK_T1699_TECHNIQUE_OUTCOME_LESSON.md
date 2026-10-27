# T1699 Direct Prompt Injection Outcome Lesson

## Authoritative description

- Technique: **T1699 — Direct Prompt Injection**
- Tactics: execution
- Platforms: Windows, SaaS

Adversaries may input malicious prompts directly into an LLM’s user interface. The prompts can be designed to bypass safeguards, manipulate context, override previous instructions, or coerce the LLM into unauthorized behavior. Adversaries may use direct prompt injection to Generate Content prohibited by the LLM's guardrails or to induce the system to utilize its capabilities in unintended or prohibited ways. Adversaries may achieve this by instructing the LLM to ignore previous instructions or safety rules, or by impersonating a role such as a researcher or privileged user.

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
- T1699: https://attack.mitre.org/techniques/T1699
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
