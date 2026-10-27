# Rc.common Technique Engineering Review

## Reference

- Technique: **T1163 — Rc.common**

During the boot process, macOS executes source /etc/rc.common, which is a shell script containing various utility functions. This file also defines routines for processing command-line arguments and for gathering system settings, and is thus recommended to include in the start of Startup Item Scripts . In macOS and OS X, this is now a deprecated technique in favor of launch agents and launch daemons, but is currently still used. Adversaries can use the rc.common file as a way to hide code for persistence that will execute on each reboot as the root user .

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
- T1163: https://attack.mitre.org/techniques/T1163
- Reviewed: 2026-10-27
