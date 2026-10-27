# vSphere Installation Bundles Technique Response Playbook

## Target technique

**T1505.006 — vSphere Installation Bundles**

- Tactics: persistence
- Platforms: ESXi

Adversaries may abuse vSphere Installation Bundles (VIBs) to establish persistent access to ESXi hypervisors. VIBs are collections of files used for software distribution and virtual system management in VMware environments. Since ESXi uses an in-memory filesystem where changes made to most files are stored in RAM rather than in persistent storage, these modifications are lost after a reboot. However, VIBs can be used to create startup tasks, apply custom firewall rules, or deploy binaries that persist across reboots. Typically, administrators use VIBs for updates and system maintenance. VIBs can be broken down into three components: * VIB payload: a `.vgz` archive containing the directories and files to be created and executed on boot when the VIBs are loaded. * Signature file: verifies the host acceptance level of a VIB, indicating what testing and validation has been done by VMware or its partners before publication of a VIB. By default, ESXi hosts require a minimum acceptance level of PartnerSupported for VIB installation, meaning the VIB is published by a trusted VMware partner. However, privileged users can change the default acceptance level using the `esxcli` command line interface. Additionally, VIBs are able to be installed regardless of acceptance level by using the <code> esxcli software vib install --force</code> command. * XML descriptor file: a configuration file containing associated VIB metadata, such as the name of the VIB and its dependencies. Adversaries may leverage malicious VIB packages to maintain persistent access to ESXi hypervisors, allowing system changes to be executed upon each bootup of ESXi – such as using `esxcli` to enable firewall rules for backdoor traffic, creating listeners on hard coded ports, and executing backdoors. Adversaries may also masquerade their malicious VIB files as PartnerSupported by modifying the XML descriptor file.

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
- T1505.006: https://attack.mitre.org/techniques/T1505/006
- Reviewed: 2026-10-27
