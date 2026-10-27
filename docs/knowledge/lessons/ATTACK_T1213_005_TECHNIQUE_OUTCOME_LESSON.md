# T1213.005 Messaging Applications Outcome Lesson

## Authoritative description

- Technique: **T1213.005 — Messaging Applications**
- Tactics: collection
- Platforms: Office Suite, SaaS

Adversaries may leverage chat and messaging applications, such as Microsoft Teams, Google Chat, and Slack, to mine valuable information. The following is a brief list of example information that may hold potential value to an adversary and may also be found on messaging applications: * Testing / development credentials (i.e., Chat Messages) * Source code snippets * Links to network shares and other internal resources * Proprietary data * Discussions about ongoing incident response efforts In addition to exfiltrating data from messaging applications, adversaries may leverage data from chat messages in order to improve their targeting - for example, by learning more about an environment or evading ongoing incident response efforts.

## Reusable lesson

This technique should be treated as an explicit review question when it is relevant to the system or organisation, rather than assumed to be covered by a generic control statement or by tooling that reports a related signal.

## Apply the lesson

1. Define the real scope before judging coverage.
2. Inspect current technical, process, governance, or operational evidence.
3. Separate documented intent from verified behaviour.
4. Record partial coverage and unresolved gaps instead of converting them into a pass.
5. Revisit when the underlying scope, threat environment, technology, suppliers, or mission materially changes.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1213.005: https://attack.mitre.org/techniques/T1213/005
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
