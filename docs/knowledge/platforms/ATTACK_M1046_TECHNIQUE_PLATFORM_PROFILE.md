# Boot Integrity Technique Platform Profile

## Reference

- Technique: **M1046 — Boot Integrity**
- Platforms named in the source: not stated

Boot Integrity ensures that a system starts securely by verifying the integrity of its boot process, operating system, and associated components. This mitigation focuses on leveraging secure boot mechanisms, hardware-rooted trust, and runtime integrity checks to prevent tampering during the boot sequence. It is designed to thwart adversaries attempting to modify system firmware, bootloaders, or critical OS components. This mitigation can be implemented through the following measures: Implementation of Secure Boot: - Implementation: Enable UEFI Secure Boot on all systems and configure it to allow only signed bootloaders and operating systems. - Use Case: An adversary attempts to replace the system’s bootloader with a malicious version to gain persistence. Secure Boot prevents the untrusted bootloader from executing, halting the attack. Utilization of TPMs: - Implementation: Configure systems to use TPM-based attestation for boot integrity, ensuring that any modification to the firmware, bootloader, or OS is detected. - Use Case: A compromised firmware component alters the boot sequence. The TPM detects the change and triggers an alert, allowing the organization to respond before further damage. Enable Bootloader Passwords: - Implementation: Protect BIOS/UEFI settings with a strong password and limit physical access to devices. - Use Case: An attacker with physical access attempts to disable Secure Boot or modify the boot sequence. The password prevents unauthorized changes. Runtime Integrity Monitoring: - Implementation: Deploy solutions to verify the integrity of critical files and processes after boot. - Use Case: A malware infection modifies kernel modules post-boot. Runtime integrity monitoring detects the modification and prevents the malicious module from loading.

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
- M1046: https://attack.mitre.org/mitigations/M1046
- Reviewed: 2026-10-27
