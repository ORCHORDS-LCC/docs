# Limit Hardware Installation Technique Response Playbook

## Target technique

**M1034 — Limit Hardware Installation**


Prevent unauthorized users or groups from installing or using hardware, such as external drives, peripheral devices, or unapproved internal hardware components, by enforcing hardware usage policies and technical controls. This includes disabling USB ports, restricting driver installation, and implementing endpoint security tools to monitor and block unapproved devices. This mitigation can be implemented through the following measures: Disable USB Ports and Hardware Installation Policies: - Use Group Policy Objects (GPO) to disable USB mass storage devices: - Navigate to Computer Configuration > Administrative Templates > System > Removable Storage Access. - Deny write and read access to USB devices. - Whitelist approved devices using unique serial numbers via Windows Device Installation Policies. Deploy Endpoint Protection and Device Control Solutions: - Use tools like Microsoft Defender for Endpoint, Symantec Endpoint Protection, or Tanium to monitor and block unauthorized hardware. - Implement device control policies to allow specific hardware types (e.g., keyboards, mice) and block others. Harden BIOS/UEFI and System Firmware: - Set strong passwords for BIOS/UEFI access. - Enable Secure Boot to prevent rogue hardware components from loading unauthorized firmware. Restrict Peripheral Devices and Drivers: - Use Windows Device Manager Policies to block installation of unapproved drivers. - Monitor hardware installation attempts through endpoint monitoring tools. Disable Bluetooth and Wireless Hardware: - Use GPO or MDM tools to disable Bluetooth and Wi-Fi interfaces across systems. - Restrict hardware pairing to approved devices only. Logging and Monitoring: - Enable logging for hardware installation events in Windows Event Logs (Event ID 20001 for Device Setup Manager). - Use SIEM solutions (e.g., Splunk, Elastic Stack) to detect unauthorized hardware installation activities. *Tools for Implementation* USB and Device Control: - Microsoft Group Policy Objects (GPO) - Microsoft Defender for Endpoint - Symantec Endpoint Protection - McAfee Device Control Endpoint Monitoring: - EDRs - OSSEC (open-source host-based IDS) Hardware Whitelisting: - BitLocker for external drives (Windows) - Windows Device Installation Policies - Device Control BIOS/UEFI Security: - Secure Boot (Windows/Linux) Firmware management tools like Dell Command Update or HP Sure Start.

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
- M1034: https://attack.mitre.org/mitigations/M1034
- Reviewed: 2026-10-27
