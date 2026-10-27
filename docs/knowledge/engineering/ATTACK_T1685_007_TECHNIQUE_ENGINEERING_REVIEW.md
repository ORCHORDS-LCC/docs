# Impair Autonomous Defenses Technique Engineering Review

## Reference

- Technique: **T1685.007 — Impair Autonomous Defenses**

Adversaries may use methods like Indirect Prompt Injection to disrupt, disable, or otherwise impair autonomous defensive capabilities such as LLM-assisted processing of malware, artifacts, or activity. This behavior may cause a system to ignore data, fail to alert on malicious activity, abort analysis, or to be disabled completely. Adversaries may include content in malware implants that mimic an LLM prompt scaffold that contains fake system messages in order to convince the LLM that it has encountered an error. Depending on the type of error, the LLM may abort analysis, truncate, or refuse to continue. Adversaries may also embed prompts in malware intended to stop agents or systems from analyzing the malware.

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
- T1685.007: https://attack.mitre.org/techniques/T1685/007
- Reviewed: 2026-10-27
