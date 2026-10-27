# DC0004 Firmware Modification Outcome Lesson

## Authoritative description

- Technique: **DC0004 — Firmware Modification**

Changes made to firmware, which may include its settings, configurations, or underlying data. This can encompass alterations to the Master Boot Record (MBR), Volume Boot Record (VBR), or other firmware components critical to system boot and functionality. Such modifications are often indicators of adversary activity, including malware persistence and system compromise. Examples: - Changes to Master Boot Record (MBR): Modifying the MBR to load malicious code during the boot process. - Changes to Volume Boot Record (VBR): Altering the VBR to redirect boot processes to malicious locations. - Firmware Configuration Changes: Modifying BIOS/UEFI settings such as disabling Secure Boot. - Firmware Image Tampering: Updating firmware with a malicious or unauthorized image. - Logs or Errors Indicating Firmware Changes: Logs showing unauthorized firmware updates or checksum mismatches. This data component can be collected through the following measures: - BIOS/UEFI Logs: Enable and monitor BIOS/UEFI logs to capture settings changes or firmware updates. - Firmware Integrity Monitoring: Use tools or firmware security features to detect changes to firmware components. - Endpoint Detection and Response (EDR) Solutions: Many EDR platforms can detect abnormal firmware activity, such as changes to MBR/VBR or unauthorized firmware updates. - File System Monitoring: Monitor changes to MBR/VBR-related files using tools like Sysmon or auditd. - Windows Example (Sysmon): Monitor Event ID 7 (Raw disk access). - Linux Example (auditd): `auditctl -w /dev/sda -p wa -k firmware_modification` - Network Traffic Analysis: Capture firmware updates downloaded over the network, particularly from untrusted sources. Use network monitoring tools like Zeek or Wireshark to analyze firmware-related traffic. - Secure Boot Logs: Collect and analyze Secure Boot logs for signs of tampering or unauthorized configurations. Example: Use PowerShell to retrieve Secure Boot settings on Windows: `Confirm-SecureBootUEFI` - Vendor-Specific Firmware Tools: Many hardware vendors provide tools for firmware integrity checks.Examples: - Intel Platform Firmware Resilience (PFR). - Lenovo UEFI diagnostics.

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
- DC0004: https://attack.mitre.org/datacomponents/DC0004
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
