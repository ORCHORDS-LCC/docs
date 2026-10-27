# T1685.007 Impair Autonomous Defenses Outcome Lesson

## Authoritative description

- Technique: **T1685.007 — Impair Autonomous Defenses**
- Tactics: defense-impairment
- Platforms: Windows, SaaS

Adversaries may use methods like Indirect Prompt Injection to disrupt, disable, or otherwise impair autonomous defensive capabilities such as LLM-assisted processing of malware, artifacts, or activity. This behavior may cause a system to ignore data, fail to alert on malicious activity, abort analysis, or to be disabled completely. Adversaries may include content in malware implants that mimic an LLM prompt scaffold that contains fake system messages in order to convince the LLM that it has encountered an error. Depending on the type of error, the LLM may abort analysis, truncate, or refuse to continue. Adversaries may also embed prompts in malware intended to stop agents or systems from analyzing the malware.

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
- T1685.007: https://attack.mitre.org/techniques/T1685/007
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
