# T1059.012 Hypervisor CLI Outcome Lesson

## Authoritative description

- Technique: **T1059.012 — Hypervisor CLI**
- Tactics: execution
- Platforms: ESXi

Adversaries may abuse hypervisor command line interpreters (CLIs) to execute malicious commands. Hypervisor CLIs typically enable a wide variety of functionality for managing both the hypervisor itself and the guest virtual machines it hosts. For example, on ESXi systems, tools such as `esxcli` and `vim-cmd` allow administrators to configure firewall rules and log forwarding on the hypervisor, list virtual machines, start and stop virtual machines, and more. Adversaries may be able to leverage these tools in order to support further actions, such as File and Directory Discovery or Data Encrypted for Impact.

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
- T1059.012: https://attack.mitre.org/techniques/T1059/012
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
