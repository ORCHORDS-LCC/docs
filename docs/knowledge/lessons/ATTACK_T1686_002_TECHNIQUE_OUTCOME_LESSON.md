# T1686.002 Network Device Firewall Outcome Lesson

## Authoritative description

- Technique: **T1686.002 — Network Device Firewall**
- Tactics: defense-impairment
- Platforms: Network Devices

Adversaries may disable network device-based firewall mechanisms entirely or add, delete, or modify particular rules in order to bypass controls limiting network usage. Adversaries may obtain access to devices such as routers, switches, or other perimeter/network devices and change access control lists (ACLs), security zones, or policy rules to permit otherwise blocked traffic. For example, adversaries may add new network firewall rules to allow access to all internal network subnets without restrictions. Allowing access to internal network subsets may enable unrestricted inbound/outbound connectivity or open paths for command and control and lateral movement. Adversaries may obtain access to network device management interfaces via Valid Accounts or by exploiting vulnerabilities. In some cases, threat actors may target firewalls and other network infrastructure that are exposed to the internet by leveraging weaknesses in public-facing applications (Exploit Public-Facing Application). Adversaries may also modify host networking configurations that indirectly manipulate system firewalls, such as adjusting interface bandwidth or network connection request thresholds.

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
- T1686.002: https://attack.mitre.org/techniques/T1686/002
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
