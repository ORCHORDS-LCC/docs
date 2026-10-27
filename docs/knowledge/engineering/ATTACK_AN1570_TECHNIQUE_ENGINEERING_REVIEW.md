# Analytic 1570 Technique Engineering Review

## Reference

- Technique: **AN1570 — Analytic 1570**

Defenders may observe adversary attempts to downgrade system images by monitoring for anomalous file transfers of OS image files (via TFTP, FTP, SCP), configuration changes pointing boot system variables to older image files, unexpected OS version strings after reboot, and checksum mismatches against approved baseline images. Suspicious chains include transfer of an older image, alteration of boot configuration, and reboot/reload of the device. Adversaries may also tamper with CLI output to disguise downgrade attempts, requiring independent validation of OS version and integrity.

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
- AN1570: https://attack.mitre.org/detectionstrategies/DET0569#AN1570
- Reviewed: 2026-10-27
