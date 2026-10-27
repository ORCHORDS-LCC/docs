# Boot Integrity Technique Response Playbook

## Target technique

**M1046 — Boot Integrity**


Boot Integrity ensures that a system starts securely by verifying the integrity of its boot process, operating system, and associated components. This mitigation focuses on leveraging secure boot mechanisms, hardware-rooted trust, and runtime integrity checks to prevent tampering during the boot sequence. It is designed to thwart adversaries attempting to modify system firmware, bootloaders, or critical OS components. This mitigation can be implemented through the following measures: Implementation of Secure Boot: - Implementation: Enable UEFI Secure Boot on all systems and configure it to allow only signed bootloaders and operating systems. - Use Case: An adversary attempts to replace the system’s bootloader with a malicious version to gain persistence. Secure Boot prevents the untrusted bootloader from executing, halting the attack. Utilization of TPMs: - Implementation: Configure systems to use TPM-based attestation for boot integrity, ensuring that any modification to the firmware, bootloader, or OS is detected. - Use Case: A compromised firmware component alters the boot sequence. The TPM detects the change and triggers an alert, allowing the organization to respond before further damage. Enable Bootloader Passwords: - Implementation: Protect BIOS/UEFI settings with a strong password and limit physical access to devices. - Use Case: An attacker with physical access attempts to disable Secure Boot or modify the boot sequence. The password prevents unauthorized changes. Runtime Integrity Monitoring: - Implementation: Deploy solutions to verify the integrity of critical files and processes after boot. - Use Case: A malware infection modifies kernel modules post-boot. Runtime integrity monitoring detects the modification and prevents the malicious module from loading.

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
- M1046: https://attack.mitre.org/mitigations/M1046
- Reviewed: 2026-10-27
