# T1673 Virtual Machine Discovery Outcome Lesson

## Authoritative description

- Technique: **T1673 — Virtual Machine Discovery**
- Tactics: discovery
- Platforms: ESXi, Linux, macOS, Windows

An adversary may attempt to enumerate running virtual machines (VMs) after gaining access to a host or hypervisor. For example, adversaries may enumerate a list of VMs on an ESXi hypervisor using a Hypervisor CLI such as `esxcli` or `vim-cmd` (e.g. `esxcli vm process list or vim-cmd vmsvc/getallvms`). Adversaries may also directly leverage a graphical user interface, such as VMware vCenter, in order to view virtual machines on a host. Adversaries may use the information from Virtual Machine Discovery during discovery to shape follow-on behaviors. Subsequently discovered VMs may be leveraged for follow-on activities such as Service Stop or Data Encrypted for Impact.

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
- T1673: https://attack.mitre.org/techniques/T1673
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
