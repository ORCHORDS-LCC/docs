# S0377 Ebury Outcome Lesson

## Authoritative description

- Technique: **S0377 — Ebury**
- Platforms: Linux

Ebury is an OpenSSH backdoor and credential stealer targeting Linux servers and container hosts developed by Windigo. Ebury is primarily installed through modifying shared libraries (`.so` files) executed by the legitimate OpenSSH program. First seen in 2009, Ebury has been used to maintain a botnet of servers, deploy additional malware, and steal cryptocurrency wallets, credentials, and credit card details.

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
- S0377: https://attack.mitre.org/software/S0377
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
