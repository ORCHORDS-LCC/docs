# Local Storage Discovery Technique Platform Profile

## Reference

- Technique: **T1680 — Local Storage Discovery**
- Platforms named in the source: ESXi, IaaS, Linux, macOS, Windows

Adversaries may enumerate local drives, disks, and/or volumes and their attributes like total or free space and volume serial number. This can be done to prepare for ransomware-related encryption, to perform Lateral Movement, or as a precursor to Direct Volume Access. On ESXi systems, adversaries may use Hypervisor CLI commands such as `esxcli` to list storage connected to the host as well as `.vmdk` files. On Windows systems, adversaries can use `wmic logicaldisk get` to find information about local network drives. They can also use `Get-PSDrive` in PowerShell to retrieve drives and may additionally use Windows API functions such as `GetDriveType`. Linux has commands such as `parted`, `lsblk`, `fdisk`, `lshw`, and `df` that can list information about disk partitions such as size, type, file system types, and free space. The command `diskutil` on MacOS can be used to list disks while `system_profiler SPStorageDataType` can additionally show information such as a volume’s mount path, file system, and the type of drive in the system. Infrastructure as a Service (IaaS) cloud providers also have commands for storage discovery such as `describe volume` in AWS, `gcloud compute disks list` in GCP, and `az disk list` in Azure.

## Platform profile

1. Record the platforms in scope and the versions actually deployed.
2. Compare the deployed platform surface against the platforms the source names.
3. Record where the platform provides a native control for the technique, and where it does not.
4. Record the configuration evidence for the native control, where one exists.
5. Record the gap where the platform provides no native control, and the compensating detection.
6. Record the platform version, because platform behaviour changes between versions.

## Evidence

- the platform and version inventory for the scoped estate;
- the configuration export or screenshot for the native control;
- the detection evidence where the platform provides none.

## Limitations

A technique entry describes a class of abuse across platforms. The platform-specific exposure is a property of the deployment, established only by inventory and configuration evidence.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1680: https://attack.mitre.org/techniques/T1680
- Reviewed: 2026-10-27
