# T1650 Acquire Access Outcome Lesson

## Authoritative description

- Technique: **T1650 — Acquire Access**
- Tactics: resource-development
- Platforms: PRE

Adversaries may purchase or otherwise acquire an existing access to a target system or network. A variety of online services and initial access broker networks are available to sell access to previously compromised systems. In some cases, adversary groups may form partnerships to share compromised systems with each other. Footholds to compromised systems may take a variety of forms, such as access to planted backdoors (e.g., Web Shell) or established access via External Remote Services. In some cases, access brokers will implant compromised systems with a “load” that can be used to install additional malware for paying customers. By leveraging existing access broker networks rather than developing or obtaining their own initial access capabilities, an adversary can potentially reduce the resources required to gain a foothold on a target network and focus their efforts on later stages of compromise. Adversaries may prioritize acquiring access to systems that have been determined to lack security monitoring or that have high privileges, or systems that belong to organizations in a particular sector. In some cases, purchasing access to an organization in sectors such as IT contracting, software development, or telecommunications may allow an adversary to compromise additional victims via a Trusted Relationship, Multi-Factor Authentication Interception, or even Supply Chain Compromise. **Note:** while this technique is distinct from other behaviors such as Purchase Technical Data and Credentials, they may often be used in conjunction (especially where the acquired foothold requires Valid Accounts).

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
- T1650: https://attack.mitre.org/techniques/T1650
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
