# DC0074 Driver Metadata Outcome Lesson

## Authoritative description

- Technique: **DC0074 — Driver Metadata**

To contextual data about a driver, including its attributes, functionality, and activity. This can involve details such as the driver's origin, integrity, cryptographic signature, issues reported during its use, and runtime behavior. Examples include metadata captured during driver integrity checks, hash validation, or error reporting. Examples: - Driver Signature Validation: A driver is validated to ensure it is signed by a trusted Certificate Authority (CA). - Driver Hash Verification: The hash of a driver is compared to a known good hash stored in a database. - Driver Compatibility Issues: A driver error is logged due to compatibility issues with a particular version of the operating system. - Vulnerable Driver Identification: Metadata indicates the driver version is outdated or contains a known vulnerability. - Monitoring Driver Integrity: Drivers are monitored for any unauthorized modifications to their binary or associated files. This data component can be collected through the following measures: Windows - Windows Event Logs: - Event ID 3000-3006: Logs metadata about driver signature validation. - Event ID 2000-2011 (Windows Defender Application Control): Tracks driver integrity and policy enforcement. - Sysmon Logs: Configure Sysmon to capture driver loading metadata (Event ID 6). - Driver Verifier: Use Driver Verifier to collect diagnostic and performance data about drivers, including stability and compatibility metrics. - PowerShell: Use commands to retrieve metadata about installed drivers: `Get-WindowsDriver -Online | Select-Object Driver, ProviderName, Version` Linux - Auditd: Configure audit rules to monitor driver interactions and collect metadata: `auditctl -w /lib/modules/ -p rwxa -k driver_metadata` - dmesg: Use `dmesg` to extract kernel logs with driver metadata: `dmesg | grep "module"` - lsmod and modinfo: Commands to list loaded modules and retrieve metadata about drivers: `lsmod` | `modinfo <module_name>` macOS - Unified Logs: Collect metadata from system logs about kernel extensions (kexts): `log show --predicate 'eventMessage contains "kext load"' --info` - kextstat: Command to retrieve information about loaded kernel extensions: `kextstat` SIEM Tools - Ingest Driver Metadata: Collect driver metadata logs from Sysmon, Auditd, or macOS logs into SIEMs like Splunk or Elastic. Vulnerability Management Tools - Use these tools to collect metadata about vulnerable drivers across enterprise systems.

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
- DC0074: https://attack.mitre.org/datacomponents/DC0074
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
