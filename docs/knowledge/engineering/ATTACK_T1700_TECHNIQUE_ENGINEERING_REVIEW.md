# AI-Enabled Exfiltration Technique Engineering Review

## Reference

- Technique: **T1700 — AI-Enabled Exfiltration**

Adversaries may utilize Direct Prompt Injection, Indirect Prompt Injection or other methods to instruct enterprise AI agents to exfiltrate data. When enterprise systems incorporate the use of AI assistants or other AI agents, adversaries may abuse these systems to weaponize sanctioned tools available to the agent. As an AI agent processes queries or ingests data, an injected prompt can cause the agent to use its tool connections in unauthorized or unintended ways. When AI agents are induced to exfiltrate data, other exfiltration techniques likely apply as well to transfer the information out of the network, such as Exfiltration to Code Repository or Exfiltration Over Web Service.

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
- T1700: https://attack.mitre.org/techniques/T1700
- Reviewed: 2026-10-27
