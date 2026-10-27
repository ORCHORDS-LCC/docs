# Direct Prompt Injection Technique Response Playbook

## Target technique

**T1699 — Direct Prompt Injection**

- Tactics: execution
- Platforms: Windows, SaaS

Adversaries may input malicious prompts directly into an LLM’s user interface. The prompts can be designed to bypass safeguards, manipulate context, override previous instructions, or coerce the LLM into unauthorized behavior. Adversaries may use direct prompt injection to Generate Content prohibited by the LLM's guardrails or to induce the system to utilize its capabilities in unintended or prohibited ways. Adversaries may achieve this by instructing the LLM to ignore previous instructions or safety rules, or by impersonating a role such as a researcher or privileged user.

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
- T1699: https://attack.mitre.org/techniques/T1699
- Reviewed: 2026-10-27
