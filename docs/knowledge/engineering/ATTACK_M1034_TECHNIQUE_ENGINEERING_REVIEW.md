# Limit Hardware Installation Technique Engineering Review

## Reference

- Technique: **M1034 — Limit Hardware Installation**

Prevent unauthorized users or groups from installing or using hardware, such as external drives, peripheral devices, or unapproved internal hardware components, by enforcing hardware usage policies and technical controls. This includes disabling USB ports, restricting driver installation, and implementing endpoint security tools to monitor and block unapproved devices. This mitigation can be implemented through the following measures: Disable USB Ports and Hardware Installation Policies: - Use Group Policy Objects (GPO) to disable USB mass storage devices: - Navigate to Computer Configuration > Administrative Templates > System > Removable Storage Access. - Deny write and read access to USB devices. - Whitelist approved devices using unique serial numbers via Windows Device Installation Policies. Deploy Endpoint Protection and Device Control Solutions: - Use tools like Microsoft Defender for Endpoint, Symantec Endpoint Protection, or Tanium to monitor and block unauthorized hardware. - Implement device control policies to allow specific hardware types (e.g., keyboards, mice) and block others. Harden BIOS/UEFI and System Firmware: - Set strong passwords for BIOS/UEFI access. - Enable Secure Boot to prevent rogue hardware components from loading unauthorized firmware. Restrict Peripheral Devices and Drivers: - Use Windows Device Manager Policies to block installation of unapproved drivers. - Monitor hardware installation attempts through endpoint monitoring tools. Disable Bluetooth and Wireless Hardware: - Use GPO or MDM tools to disable Bluetooth and Wi-Fi interfaces across systems. - Restrict hardware pairing to approved devices only. Logging and Monitoring: - Enable logging for hardware installation events in Windows Event Logs (Event ID 20001 for Device Setup Manager). - Use SIEM solutions (e.g., Splunk, Elastic Stack) to detect unauthorized hardware installation activities. *Tools for Implementation* USB and Device Control: - Microsoft Group Policy Objects (GPO) - Microsoft Defender for Endpoint - Symantec Endpoint Protection - McAfee Device Control Endpoint Monitoring: - EDRs - OSSEC (open-source host-based IDS) Hardware Whitelisting: - BitLocker for external drives (Windows) - Windows Device Installation Policies - Device Control BIOS/UEFI Security: - Secure Boot (Windows/Linux) Firmware management tools like Dell Command Update or HP Sure Start.

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
- M1034: https://attack.mitre.org/mitigations/M1034
- Reviewed: 2026-10-27
