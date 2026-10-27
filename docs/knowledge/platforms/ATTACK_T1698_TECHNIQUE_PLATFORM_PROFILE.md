# Indirect Prompt Injection Technique Platform Profile

## Reference

- Technique: **T1698 — Indirect Prompt Injection**
- Platforms named in the source: Windows, SaaS

Adversaries may deliver malicious prompts to an LLM indirectly by embedding the prompts in content that the adversary expects may be processed by an LLM. These prompts can be included in web pages, documents, emails, tickets, code, or other sources that an agent, copilot, or other AI system may retrieve and process. When an LLM processes this content, the embedded instructions may cause the system to perform unintended behaviors. Adversaries may use indirect prompt injection to Impair Autonomous Defenses, and for unauthorized execution of any capabilities available to the LLM.

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
- T1698: https://attack.mitre.org/techniques/T1698
- Reviewed: 2026-10-27
