# Anthropic AI-orchestrated Campaign Technique Response Playbook

## Target technique

**C0062 — Anthropic AI-orchestrated Campaign**


The Anthropic AI-orchestrated Campaign was conducted in September 2025 by a likely China nexus espionage actor identified as GTG-1002. The Anthropic AI-orchestrated Campaign was a highly coordinated operation that manipulated Claude Code to perform reconnaissance, vulnerability discovery, exploitation, lateral movement, credential harvesting, data analysis, and exfiltration operations at approximately 30 entities in the technology, financial, chemical, and government sectors. During the Anthropic AI-orchestrated Campaign, human operators used Claude Code agents and Model Context Protocol (MCP) tools to automate cyber operations. Operators broke attacks into discrete tasks, used crafted prompts, and established personas to bypass AI guardrails, enabling the agents to execute the operations with minimal human involvement.

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
- C0062: https://attack.mitre.org/campaigns/C0062
- Reviewed: 2026-10-27
