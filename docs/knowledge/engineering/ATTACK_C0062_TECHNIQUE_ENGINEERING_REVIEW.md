# Anthropic AI-orchestrated Campaign Technique Engineering Review

## Reference

- Technique: **C0062 — Anthropic AI-orchestrated Campaign**

The Anthropic AI-orchestrated Campaign was conducted in September 2025 by a likely China nexus espionage actor identified as GTG-1002. The Anthropic AI-orchestrated Campaign was a highly coordinated operation that manipulated Claude Code to perform reconnaissance, vulnerability discovery, exploitation, lateral movement, credential harvesting, data analysis, and exfiltration operations at approximately 30 entities in the technology, financial, chemical, and government sectors. During the Anthropic AI-orchestrated Campaign, human operators used Claude Code agents and Model Context Protocol (MCP) tools to automate cyber operations. Operators broke attacks into discrete tasks, used crafted prompts, and established personas to bypass AI guardrails, enabling the agents to execute the operations with minimal human involvement.

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
- C0062: https://attack.mitre.org/campaigns/C0062
- Reviewed: 2026-10-27
