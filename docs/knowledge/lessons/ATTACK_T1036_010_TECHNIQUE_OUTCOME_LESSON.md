# T1036.010 Masquerade Account Name Outcome Lesson

## Authoritative description

- Technique: **T1036.010 — Masquerade Account Name**
- Tactics: stealth
- Platforms: Containers, IaaS, Identity Provider, Linux, macOS, Office Suite, SaaS, Windows

Adversaries may match or approximate the names of legitimate accounts to make newly created ones appear benign. This will typically occur during Create Account, although accounts may also be renamed at a later date. This may also coincide with Account Access Removal if the actor first deletes an account before re-creating one with the same name. Often, adversaries will attempt to masquerade as service accounts, such as those associated with legitimate software, data backups, or container cluster management. They may also give accounts generic, trustworthy names, such as “admin”, “help”, or “root.” Sometimes adversaries may model account names off of those already existing in the system, as a follow-on behavior to Account Discovery. Note that this is distinct from Impersonation, which describes impersonating specific trusted individuals or organizations, rather than user or service account names.

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
- T1036.010: https://attack.mitre.org/techniques/T1036/010
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
