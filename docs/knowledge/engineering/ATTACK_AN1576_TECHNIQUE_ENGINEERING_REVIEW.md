# Analytic 1576 Technique Engineering Review

## Reference

- Technique: **AN1576 — Analytic 1576**

Detects creation or modification of `systemd` service units, addition of cron jobs that invoke binaries on boot, or suspicious writes to `/etc/init.d/`. Monitors `chmod +x` and `systemctl` execution paths, especially from non-root parent processes.

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
- AN1576: https://attack.mitre.org/detectionstrategies/DET0571#AN1576
- Reviewed: 2026-10-27
