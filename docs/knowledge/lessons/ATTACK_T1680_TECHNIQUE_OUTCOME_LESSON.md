# T1680 Local Storage Discovery Outcome Lesson

## Authoritative description

- Technique: **T1680 — Local Storage Discovery**
- Tactics: discovery
- Platforms: ESXi, IaaS, Linux, macOS, Windows

Adversaries may enumerate local drives, disks, and/or volumes and their attributes like total or free space and volume serial number. This can be done to prepare for ransomware-related encryption, to perform Lateral Movement, or as a precursor to Direct Volume Access. On ESXi systems, adversaries may use Hypervisor CLI commands such as `esxcli` to list storage connected to the host as well as `.vmdk` files. On Windows systems, adversaries can use `wmic logicaldisk get` to find information about local network drives. They can also use `Get-PSDrive` in PowerShell to retrieve drives and may additionally use Windows API functions such as `GetDriveType`. Linux has commands such as `parted`, `lsblk`, `fdisk`, `lshw`, and `df` that can list information about disk partitions such as size, type, file system types, and free space. The command `diskutil` on MacOS can be used to list disks while `system_profiler SPStorageDataType` can additionally show information such as a volume’s mount path, file system, and the type of drive in the system. Infrastructure as a Service (IaaS) cloud providers also have commands for storage discovery such as `describe volume` in AWS, `gcloud compute disks list` in GCP, and `az disk list` in Azure.

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
- T1680: https://attack.mitre.org/techniques/T1680
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
