# T1136.001 Local Account Outcome Lesson

## Authoritative description

- Technique: **T1136.001 — Local Account**
- Tactics: persistence
- Platforms: Containers, ESXi, Linux, macOS, Network Devices, Windows

Adversaries may create a local account to maintain access to victim systems. Local accounts are those configured by an organization for use by users, remote support, services, or for administration on a single system or service. For example, with a sufficient level of access, the Windows <code>net user /add</code> command can be used to create a local account. In Linux, the `useradd` command can be used, while on macOS systems, the <code>dscl -create</code> command can be used. Local accounts may also be added to network devices, often via common Network Device CLI commands such as <code>username</code>, to ESXi servers via `esxcli system account add`, or to Kubernetes clusters using the `kubectl` utility. Adversaries may also create new local accounts on network firewall management consoles – for example, by exploiting a vulnerable firewall management system, threat actors may be able to establish super-admin accounts that could be used to modify firewall rules and gain further access to the network. Such accounts may be used to establish secondary credentialed access that do not require persistent remote access tools to be deployed on the system.

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
- T1136.001: https://attack.mitre.org/techniques/T1136/001
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
