# Vulnerabilities Technique Response Playbook

## Target technique

**T1588.006 — Vulnerabilities**

- Tactics: resource-development
- Platforms: PRE

Adversaries may acquire information about vulnerabilities that can be used during targeting. A vulnerability is a weakness in computer hardware or software that can, potentially, be exploited by an adversary to cause unintended or unanticipated behavior to occur. Adversaries may find vulnerability information by searching open databases or gaining access to closed vulnerability databases. An adversary may monitor vulnerability disclosures/databases to understand the state of existing, as well as newly discovered, vulnerabilities. There is usually a delay between when a vulnerability is discovered and when it is made public. An adversary may target the systems of those known to conduct vulnerability research (including commercial vendors). Knowledge of a vulnerability may cause an adversary to search for an existing exploit (i.e. Exploits) or to attempt to develop one themselves (i.e. Exploits).

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
- T1588.006: https://attack.mitre.org/techniques/T1588/006
- Reviewed: 2026-10-27
