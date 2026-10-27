# Acquire Access Technique Engineering Review

## Reference

- Technique: **T1650 — Acquire Access**

Adversaries may purchase or otherwise acquire an existing access to a target system or network. A variety of online services and initial access broker networks are available to sell access to previously compromised systems. In some cases, adversary groups may form partnerships to share compromised systems with each other. Footholds to compromised systems may take a variety of forms, such as access to planted backdoors (e.g., Web Shell) or established access via External Remote Services. In some cases, access brokers will implant compromised systems with a “load” that can be used to install additional malware for paying customers. By leveraging existing access broker networks rather than developing or obtaining their own initial access capabilities, an adversary can potentially reduce the resources required to gain a foothold on a target network and focus their efforts on later stages of compromise. Adversaries may prioritize acquiring access to systems that have been determined to lack security monitoring or that have high privileges, or systems that belong to organizations in a particular sector. In some cases, purchasing access to an organization in sectors such as IT contracting, software development, or telecommunications may allow an adversary to compromise additional victims via a Trusted Relationship, Multi-Factor Authentication Interception, or even Supply Chain Compromise. **Note:** while this technique is distinct from other behaviors such as Purchase Technical Data and Credentials, they may often be used in conjunction (especially where the acquired foothold requires Valid Accounts).

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
- T1650: https://attack.mitre.org/techniques/T1650
- Reviewed: 2026-10-27
