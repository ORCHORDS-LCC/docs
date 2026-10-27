# Masquerade Account Name Technique Response Playbook

## Target technique

**T1036.010 — Masquerade Account Name**

- Tactics: stealth
- Platforms: Containers, IaaS, Identity Provider, Linux, macOS, Office Suite, SaaS, Windows

Adversaries may match or approximate the names of legitimate accounts to make newly created ones appear benign. This will typically occur during Create Account, although accounts may also be renamed at a later date. This may also coincide with Account Access Removal if the actor first deletes an account before re-creating one with the same name. Often, adversaries will attempt to masquerade as service accounts, such as those associated with legitimate software, data backups, or container cluster management. They may also give accounts generic, trustworthy names, such as “admin”, “help”, or “root.” Sometimes adversaries may model account names off of those already existing in the system, as a follow-on behavior to Account Discovery. Note that this is distinct from Impersonation, which describes impersonating specific trusted individuals or organizations, rather than user or service account names.

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
- T1036.010: https://attack.mitre.org/techniques/T1036/010
- Reviewed: 2026-10-27
