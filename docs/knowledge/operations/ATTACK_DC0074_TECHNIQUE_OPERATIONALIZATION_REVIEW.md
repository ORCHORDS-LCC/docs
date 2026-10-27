# Driver Metadata Technique Operationalization Review

## Reference

- Technique: **DC0074 — Driver Metadata**

To contextual data about a driver, including its attributes, functionality, and activity. This can involve details such as the driver's origin, integrity, cryptographic signature, issues reported during its use, and runtime behavior. Examples include metadata captured during driver integrity checks, hash validation, or error reporting. Examples: - Driver Signature Validation: A driver is validated to ensure it is signed by a trusted Certificate Authority (CA). - Driver Hash Verification: The hash of a driver is compared to a known good hash stored in a database. - Driver Compatibility Issues: A driver error is logged due to compatibility issues with a particular version of the operating system. - Vulnerable Driver Identification: Metadata indicates the driver version is outdated or contains a known vulnerability. - Monitoring Driver Integrity: Drivers are monitored for any unauthorized modifications to their binary or associated files. This data component can be collected through the following measures: Windows - Windows Event Logs: - Event ID 3000-3006: Logs metadata about driver signature validation. - Event ID 2000-2011 (Windows Defender Application Control): Tracks driver integrity and policy enforcement. - Sysmon Logs: Configure Sysmon to capture driver loading metadata (Event ID 6). - Driver Verifier: Use Driver Verifier to collect diagnostic and performance data about drivers, including stability and compatibility metrics. - PowerShell: Use commands to retrieve metadata about installed drivers: `Get-WindowsDriver -Online | Select-Object Driver, ProviderName, Version` Linux - Auditd: Configure audit rules to monitor driver interactions and collect metadata: `auditctl -w /lib/modules/ -p rwxa -k driver_metadata` - dmesg: Use `dmesg` to extract kernel logs with driver metadata: `dmesg | grep "module"` - lsmod and modinfo: Commands to list loaded modules and retrieve metadata about drivers: `lsmod` | `modinfo <module_name>` macOS - Unified Logs: Collect metadata from system logs about kernel extensions (kexts): `log show --predicate 'eventMessage contains "kext load"' --info` - kextstat: Command to retrieve information about loaded kernel extensions: `kextstat` SIEM Tools - Ingest Driver Metadata: Collect driver metadata logs from Sysmon, Auditd, or macOS logs into SIEMs like Splunk or Elastic. Vulnerability Management Tools - Use these tools to collect metadata about vulnerable drivers across enterprise systems.

## Operationalization review

1. Record the operational scope: which services, environments, and data the technique could affect.
2. Record the runbook that would be executed, and its owner.
3. Record the telemetry the runbook depends on, and whether it is retained long enough to investigate.
4. Record the detection that would surface the technique before or after it has an effect.
5. Record the recovery path, and the evidence that recovery has been rehearsed.
6. Record the residual operational risk where the runbook depends on a manual step.

## Review evidence

- the runbook and its owner;
- the telemetry retention and coverage record;
- the detection mapping;
- the exercise or rehearsal record.

## Limitations

An operationalization review describes the runbook and the evidence around it. It does not claim the technique has been prevented or detected in a live environment.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- DC0074: https://attack.mitre.org/datacomponents/DC0074
- Reviewed: 2026-10-27
