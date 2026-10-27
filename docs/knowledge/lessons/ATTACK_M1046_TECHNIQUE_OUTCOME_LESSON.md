# M1046 Boot Integrity Outcome Lesson

## Authoritative description

- Technique: **M1046 — Boot Integrity**

Boot Integrity ensures that a system starts securely by verifying the integrity of its boot process, operating system, and associated components. This mitigation focuses on leveraging secure boot mechanisms, hardware-rooted trust, and runtime integrity checks to prevent tampering during the boot sequence. It is designed to thwart adversaries attempting to modify system firmware, bootloaders, or critical OS components. This mitigation can be implemented through the following measures: Implementation of Secure Boot: - Implementation: Enable UEFI Secure Boot on all systems and configure it to allow only signed bootloaders and operating systems. - Use Case: An adversary attempts to replace the system’s bootloader with a malicious version to gain persistence. Secure Boot prevents the untrusted bootloader from executing, halting the attack. Utilization of TPMs: - Implementation: Configure systems to use TPM-based attestation for boot integrity, ensuring that any modification to the firmware, bootloader, or OS is detected. - Use Case: A compromised firmware component alters the boot sequence. The TPM detects the change and triggers an alert, allowing the organization to respond before further damage. Enable Bootloader Passwords: - Implementation: Protect BIOS/UEFI settings with a strong password and limit physical access to devices. - Use Case: An attacker with physical access attempts to disable Secure Boot or modify the boot sequence. The password prevents unauthorized changes. Runtime Integrity Monitoring: - Implementation: Deploy solutions to verify the integrity of critical files and processes after boot. - Use Case: A malware infection modifies kernel modules post-boot. Runtime integrity monitoring detects the modification and prevents the malicious module from loading.

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
- M1046: https://attack.mitre.org/mitigations/M1046
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
