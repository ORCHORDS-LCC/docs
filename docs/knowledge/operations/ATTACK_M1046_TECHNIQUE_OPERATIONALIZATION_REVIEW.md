# Boot Integrity Technique Operationalization Review

## Reference

- Technique: **M1046 — Boot Integrity**

Boot Integrity ensures that a system starts securely by verifying the integrity of its boot process, operating system, and associated components. This mitigation focuses on leveraging secure boot mechanisms, hardware-rooted trust, and runtime integrity checks to prevent tampering during the boot sequence. It is designed to thwart adversaries attempting to modify system firmware, bootloaders, or critical OS components. This mitigation can be implemented through the following measures: Implementation of Secure Boot: - Implementation: Enable UEFI Secure Boot on all systems and configure it to allow only signed bootloaders and operating systems. - Use Case: An adversary attempts to replace the system’s bootloader with a malicious version to gain persistence. Secure Boot prevents the untrusted bootloader from executing, halting the attack. Utilization of TPMs: - Implementation: Configure systems to use TPM-based attestation for boot integrity, ensuring that any modification to the firmware, bootloader, or OS is detected. - Use Case: A compromised firmware component alters the boot sequence. The TPM detects the change and triggers an alert, allowing the organization to respond before further damage. Enable Bootloader Passwords: - Implementation: Protect BIOS/UEFI settings with a strong password and limit physical access to devices. - Use Case: An attacker with physical access attempts to disable Secure Boot or modify the boot sequence. The password prevents unauthorized changes. Runtime Integrity Monitoring: - Implementation: Deploy solutions to verify the integrity of critical files and processes after boot. - Use Case: A malware infection modifies kernel modules post-boot. Runtime integrity monitoring detects the modification and prevents the malicious module from loading.

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
- M1046: https://attack.mitre.org/mitigations/M1046
- Reviewed: 2026-10-27
