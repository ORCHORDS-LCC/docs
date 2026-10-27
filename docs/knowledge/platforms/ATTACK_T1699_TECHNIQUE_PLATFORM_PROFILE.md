# Direct Prompt Injection Technique Platform Profile

## Reference

- Technique: **T1699 — Direct Prompt Injection**
- Platforms named in the source: Windows, SaaS

Adversaries may input malicious prompts directly into an LLM’s user interface. The prompts can be designed to bypass safeguards, manipulate context, override previous instructions, or coerce the LLM into unauthorized behavior. Adversaries may use direct prompt injection to Generate Content prohibited by the LLM's guardrails or to induce the system to utilize its capabilities in unintended or prohibited ways. Adversaries may achieve this by instructing the LLM to ignore previous instructions or safety rules, or by impersonating a role such as a researcher or privileged user.

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
- T1699: https://attack.mitre.org/techniques/T1699
- Reviewed: 2026-10-27
