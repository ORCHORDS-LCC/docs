# Analytic 1293 Technique Engineering Review

## Reference

- Technique: **AN1293 — Analytic 1293**

Defenders may observe adversary attempts to patch system images by monitoring for anomalous file transfers (TFTP, SCP, FTP) of image files, unauthorized CLI commands altering boot system variables, integrity check mismatches between running and baseline OS images, and runtime memory manipulation attempts. Suspicious sequences include uploading a new image, modifying boot parameters, and subsequent reload/reboot of the device. In-memory patching attempts may manifest as debug commands or boot loader manipulation inconsistent with normal administrative activity.

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
- AN1293: https://attack.mitre.org/detectionstrategies/DET0469#AN1293
- Reviewed: 2026-10-27
