# Virtual Machine Discovery Technique Response Playbook

## Target technique

**T1673 — Virtual Machine Discovery**

- Tactics: discovery
- Platforms: ESXi, Linux, macOS, Windows

An adversary may attempt to enumerate running virtual machines (VMs) after gaining access to a host or hypervisor. For example, adversaries may enumerate a list of VMs on an ESXi hypervisor using a Hypervisor CLI such as `esxcli` or `vim-cmd` (e.g. `esxcli vm process list or vim-cmd vmsvc/getallvms`). Adversaries may also directly leverage a graphical user interface, such as VMware vCenter, in order to view virtual machines on a host. Adversaries may use the information from Virtual Machine Discovery during discovery to shape follow-on behaviors. Subsequently discovered VMs may be leveraged for follow-on activities such as Service Stop or Data Encrypted for Impact.

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
- T1673: https://attack.mitre.org/techniques/T1673
- Reviewed: 2026-10-27
