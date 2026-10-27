# Inhibit System Recovery Technique Engineering Review

## Reference

- Technique: **T1490 — Inhibit System Recovery**

Adversaries may delete or remove built-in data and turn off services designed to aid in the recovery of a corrupted system to prevent recovery. This may deny access to available backups and recovery options. Operating systems may contain features that can help fix corrupted systems, such as a backup catalog, volume shadow copies, and automatic repair features. Adversaries may disable or delete system recovery features to augment the effects of Data Destruction and Data Encrypted for Impact. Furthermore, adversaries may disable recovery notifications, then corrupt backups. A number of native Windows utilities have been used by adversaries to disable or delete system recovery features: * vssadmin.exe can be used to delete all volume shadow copies on a system - vssadmin.exe delete shadows /all /quiet * Windows Management Instrumentation can be used to delete volume shadow copies - wmic shadowcopy delete * wbadmin.exe can be used to delete the Windows Backup Catalog - wbadmin.exe delete catalog -quiet * bcdedit.exe can be used to disable automatic Windows recovery features by modifying boot configuration data - bcdedit.exe /set {default} bootstatuspolicy ignoreallfailures & bcdedit /set {default} recoveryenabled no * REAgentC.exe can be used to disable Windows Recovery Environment (WinRE) repair/recovery options of an infected system * diskshadow.exe can be used to delete all volume shadow copies on a system - diskshadow delete shadows all On network devices, adversaries may leverage Disk Wipe to delete backup firmware images and reformat the file system, then System Shutdown/Reboot to reload the device. Together this activity may leave network devices completely inoperable and inhibit recovery operations. On ESXi servers, adversaries may delete or encrypt snapshots of virtual machines to support Data Encrypted for Impact, preventing them from being leveraged as backups (e.g., via ` vim-cmd vmsvc/snapshot.removeall`). Adversaries may also delete “online” backups that are connected to their network – whether via network storage media or through folders that sync to cloud services. In cloud environments, adversaries may disable versioning and backup policies and delete snapshots, database backups, machine images, and prior versions of objects designed to be used in disaster recovery scenarios.

## Engineering review

1. Identify the engineering boundary where the technique would apply: the component, the service, or the deployment.
2. Review the design decision that would prevent the technique, and record the alternative considered.
3. Review the implementation evidence for the preventive control.
4. Review the test coverage that would fail if the control regressed.
5. Review the observability: which signal would show the control is not operating.
6. Record the residual risk where prevention is not achievable, and the detection that compensates.

## Review evidence

- the design record for the preventive decision;
- the implementation or configuration evidence;
- the test record showing the control is exercised;
- the observability mapping.

## Limitations

An engineering review describes what the design and the implementation evidence show. It does not claim the technique has been addressed in production.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1490: https://attack.mitre.org/techniques/T1490
- Reviewed: 2026-10-27
