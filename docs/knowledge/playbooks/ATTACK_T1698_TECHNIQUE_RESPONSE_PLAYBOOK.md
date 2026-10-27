# Indirect Prompt Injection Technique Response Playbook

## Target technique

**T1698 — Indirect Prompt Injection**

- Tactics: execution
- Platforms: Windows, SaaS

Adversaries may deliver malicious prompts to an LLM indirectly by embedding the prompts in content that the adversary expects may be processed by an LLM. These prompts can be included in web pages, documents, emails, tickets, code, or other sources that an agent, copilot, or other AI system may retrieve and process. When an LLM processes this content, the embedded instructions may cause the system to perform unintended behaviors. Adversaries may use indirect prompt injection to Impair Autonomous Defenses, and for unauthorized execution of any capabilities available to the LLM.

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
- T1698: https://attack.mitre.org/techniques/T1698
- Reviewed: 2026-10-27
