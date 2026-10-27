# Local Account Technique Response Playbook

## Target technique

**T1136.001 — Local Account**

- Tactics: persistence
- Platforms: Containers, ESXi, Linux, macOS, Network Devices, Windows

Adversaries may create a local account to maintain access to victim systems. Local accounts are those configured by an organization for use by users, remote support, services, or for administration on a single system or service. For example, with a sufficient level of access, the Windows net user /add command can be used to create a local account. In Linux, the `useradd` command can be used, while on macOS systems, the dscl -create command can be used. Local accounts may also be added to network devices, often via common Network Device CLI commands such as username, to ESXi servers via `esxcli system account add`, or to Kubernetes clusters using the `kubectl` utility. Adversaries may also create new local accounts on network firewall management consoles – for example, by exploiting a vulnerable firewall management system, threat actors may be able to establish super-admin accounts that could be used to modify firewall rules and gain further access to the network. Such accounts may be used to establish secondary credentialed access that do not require persistent remote access tools to be deployed on the system.

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
- T1136.001: https://attack.mitre.org/techniques/T1136/001
- Reviewed: 2026-10-27
