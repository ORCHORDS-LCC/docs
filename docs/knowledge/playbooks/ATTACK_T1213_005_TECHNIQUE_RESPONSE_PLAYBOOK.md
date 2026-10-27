# Messaging Applications Technique Response Playbook

## Target technique

**T1213.005 — Messaging Applications**

- Tactics: collection
- Platforms: Office Suite, SaaS

Adversaries may leverage chat and messaging applications, such as Microsoft Teams, Google Chat, and Slack, to mine valuable information. The following is a brief list of example information that may hold potential value to an adversary and may also be found on messaging applications: * Testing / development credentials (i.e., Chat Messages) * Source code snippets * Links to network shares and other internal resources * Proprietary data * Discussions about ongoing incident response efforts In addition to exfiltrating data from messaging applications, adversaries may leverage data from chat messages in order to improve their targeting - for example, by learning more about an environment or evading ongoing incident response efforts.

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
- T1213.005: https://attack.mitre.org/techniques/T1213/005
- Reviewed: 2026-10-27
