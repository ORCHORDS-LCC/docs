# Impair Autonomous Defenses Technique Platform Profile

## Reference

- Technique: **T1685.007 — Impair Autonomous Defenses**
- Platforms named in the source: Windows, SaaS

Adversaries may use methods like Indirect Prompt Injection to disrupt, disable, or otherwise impair autonomous defensive capabilities such as LLM-assisted processing of malware, artifacts, or activity. This behavior may cause a system to ignore data, fail to alert on malicious activity, abort analysis, or to be disabled completely. Adversaries may include content in malware implants that mimic an LLM prompt scaffold that contains fake system messages in order to convince the LLM that it has encountered an error. Depending on the type of error, the LLM may abort analysis, truncate, or refuse to continue. Adversaries may also embed prompts in malware intended to stop agents or systems from analyzing the malware.

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
- T1685.007: https://attack.mitre.org/techniques/T1685/007
- Reviewed: 2026-10-27
