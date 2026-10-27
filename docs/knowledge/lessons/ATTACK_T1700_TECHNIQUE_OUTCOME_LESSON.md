# T1700 AI-Enabled Exfiltration Outcome Lesson

## Authoritative description

- Technique: **T1700 — AI-Enabled Exfiltration**
- Tactics: exfiltration
- Platforms: Windows, SaaS

Adversaries may utilize Direct Prompt Injection, Indirect Prompt Injection or other methods to instruct enterprise AI agents to exfiltrate data. When enterprise systems incorporate the use of AI assistants or other AI agents, adversaries may abuse these systems to weaponize sanctioned tools available to the agent. As an AI agent processes queries or ingests data, an injected prompt can cause the agent to use its tool connections in unauthorized or unintended ways. When AI agents are induced to exfiltrate data, other exfiltration techniques likely apply as well to transfer the information out of the network, such as Exfiltration to Code Repository or Exfiltration Over Web Service.

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
- T1700: https://attack.mitre.org/techniques/T1700
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
