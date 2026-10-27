# AI-Enabled Exfiltration Technique Response Playbook

## Target technique

**T1700 — AI-Enabled Exfiltration**

- Tactics: exfiltration
- Platforms: Windows, SaaS

Adversaries may utilize Direct Prompt Injection, Indirect Prompt Injection or other methods to instruct enterprise AI agents to exfiltrate data. When enterprise systems incorporate the use of AI assistants or other AI agents, adversaries may abuse these systems to weaponize sanctioned tools available to the agent. As an AI agent processes queries or ingests data, an injected prompt can cause the agent to use its tool connections in unauthorized or unintended ways. When AI agents are induced to exfiltrate data, other exfiltration techniques likely apply as well to transfer the information out of the network, such as Exfiltration to Code Repository or Exfiltration Over Web Service.

## Preconditions

- the estate in scope is identified, with the systems the technique could apply to;
- an owner is accountable for detection and response;
- current telemetry and configuration can be inspected;
- the technique is applicable or requires an applicability decision.

## Procedure

1. Confirm the scope and owner.
2. Read the current technique description and the associated detection guidance.
3. Inventory the telemetry that would carry the technique's indicators.
4. Inspect whether the indicators are present in the environment.
5. Exercise the detection path and confirm it produces the expected signal.
6. Record gaps in detection coverage and assign remediation owners.
7. Record justified non-applicability or accepted detection gaps separately.
8. Set the next event-driven or periodic verification trigger.

## Failure handling

If the detection path does not produce the expected signal, treat the coverage as unverified, preserve the test evidence, and route the gap through the appropriate remediation or risk process.

## Completion evidence

Scope, owner, source version, telemetry inspected, tests performed, findings, exceptions, remediation links, reviewer, and next trigger.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1700: https://attack.mitre.org/techniques/T1700
- Reviewed: 2026-10-27
