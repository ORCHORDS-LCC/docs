# Impair Autonomous Defenses Technique Response Playbook

## Target technique

**T1685.007 — Impair Autonomous Defenses**

- Tactics: defense-impairment
- Platforms: Windows, SaaS

Adversaries may use methods like Indirect Prompt Injection to disrupt, disable, or otherwise impair autonomous defensive capabilities such as LLM-assisted processing of malware, artifacts, or activity. This behavior may cause a system to ignore data, fail to alert on malicious activity, abort analysis, or to be disabled completely. Adversaries may include content in malware implants that mimic an LLM prompt scaffold that contains fake system messages in order to convince the LLM that it has encountered an error. Depending on the type of error, the LLM may abort analysis, truncate, or refuse to continue. Adversaries may also embed prompts in malware intended to stop agents or systems from analyzing the malware.

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
- T1685.007: https://attack.mitre.org/techniques/T1685/007
- Reviewed: 2026-10-27
