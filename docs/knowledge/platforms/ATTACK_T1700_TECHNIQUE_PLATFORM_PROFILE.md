# AI-Enabled Exfiltration Technique Platform Profile

## Reference

- Technique: **T1700 — AI-Enabled Exfiltration**
- Platforms named in the source: Windows, SaaS

Adversaries may utilize Direct Prompt Injection, Indirect Prompt Injection or other methods to instruct enterprise AI agents to exfiltrate data. When enterprise systems incorporate the use of AI assistants or other AI agents, adversaries may abuse these systems to weaponize sanctioned tools available to the agent. As an AI agent processes queries or ingests data, an injected prompt can cause the agent to use its tool connections in unauthorized or unintended ways. When AI agents are induced to exfiltrate data, other exfiltration techniques likely apply as well to transfer the information out of the network, such as Exfiltration to Code Repository or Exfiltration Over Web Service.

## Platform profile

1. Record the platforms in scope and the versions actually deployed.
2. Compare the deployed platform surface against the platforms the source names.
3. Record where the platform provides a native control for the technique, and where it does not.
4. Record the configuration evidence for the native control, where one exists.
5. Record the gap where the platform provides no native control, and the compensating detection.
6. Record the platform version, because platform behaviour changes between versions.

## Evidence

- the platform and version inventory for the scoped estate;
- the configuration export or screenshot for the native control;
- the detection evidence where the platform provides none.

## Limitations

A technique entry describes a class of abuse across platforms. The platform-specific exposure is a property of the deployment, established only by inventory and configuration evidence.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1700: https://attack.mitre.org/techniques/T1700
- Reviewed: 2026-10-27
