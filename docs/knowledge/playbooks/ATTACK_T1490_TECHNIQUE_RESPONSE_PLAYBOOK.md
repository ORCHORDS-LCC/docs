# Inhibit System Recovery Technique Response Playbook

## Target technique

**T1490 — Inhibit System Recovery**

- Tactics: impact
- Platforms: Containers, ESXi, IaaS, Linux, macOS, Network Devices, Windows

Adversaries may delete or remove built-in data and turn off services designed to aid in the recovery of a corrupted system to prevent recovery. This may deny access to available backups and recovery options. Operating systems may contain features that can help fix corrupted systems, such as a backup catalog, volume shadow copies, and automatic repair features. Adversaries may disable or delete system recovery features to augment the effects of Data Destruction and Data Encrypted for Impact. Furthermore, adversaries may disable recovery notifications, then corrupt backups. A number of native Windows utilities have been used by adversaries to disable or delete system recovery features: * vssadmin.exe can be used to delete all volume shadow copies on a system - vssadmin.exe delete shadows /all /quiet * Windows Management Instrumentation can be used to delete volume shadow copies - wmic shadowcopy delete * wbadmin.exe can be used to delete the Windows Backup Catalog - wbadmin.exe delete catalog -quiet * bcdedit.exe can be used to disable automatic Windows recovery features by modifying boot configuration data - bcdedit.exe /set {default} bootstatuspolicy ignoreallfailures & bcdedit /set {default} recoveryenabled no * REAgentC.exe can be used to disable Windows Recovery Environment (WinRE) repair/recovery options of an infected system * diskshadow.exe can be used to delete all volume shadow copies on a system - diskshadow delete shadows all On network devices, adversaries may leverage Disk Wipe to delete backup firmware images and reformat the file system, then System Shutdown/Reboot to reload the device. Together this activity may leave network devices completely inoperable and inhibit recovery operations. On ESXi servers, adversaries may delete or encrypt snapshots of virtual machines to support Data Encrypted for Impact, preventing them from being leveraged as backups (e.g., via ` vim-cmd vmsvc/snapshot.removeall`). Adversaries may also delete “online” backups that are connected to their network – whether via network storage media or through folders that sync to cloud services. In cloud environments, adversaries may disable versioning and backup policies and delete snapshots, database backups, machine images, and prior versions of objects designed to be used in disaster recovery scenarios.

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
- T1490: https://attack.mitre.org/techniques/T1490
- Reviewed: 2026-10-27
