# Databases Technique Response Playbook

## Target technique

**T1213.006 — Databases**

- Tactics: collection
- Platforms: IaaS, Linux, macOS, SaaS, Windows

Adversaries may leverage databases to mine valuable information. These databases may be hosted on-premises or in the cloud (both in platform-as-a-service and software-as-a-service environments). Examples of databases from which information may be collected include MySQL, PostgreSQL, MongoDB, Amazon Relational Database Service, Azure SQL Database, Google Firebase, and Snowflake. Databases may include a variety of information of interest to adversaries, such as usernames, hashed passwords, personally identifiable information, and financial data. Data collected from databases may be used for Lateral Movement, Command and Control, or Exfiltration. Data exfiltrated from databases may also be used to extort victims or may be sold for profit.

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
- T1213.006: https://attack.mitre.org/techniques/T1213/006
- Reviewed: 2026-10-27
