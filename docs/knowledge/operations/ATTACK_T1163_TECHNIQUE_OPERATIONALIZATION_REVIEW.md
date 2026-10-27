# Rc.common Technique Operationalization Review

## Reference

- Technique: **T1163 — Rc.common**

During the boot process, macOS executes source /etc/rc.common, which is a shell script containing various utility functions. This file also defines routines for processing command-line arguments and for gathering system settings, and is thus recommended to include in the start of Startup Item Scripts . In macOS and OS X, this is now a deprecated technique in favor of launch agents and launch daemons, but is currently still used. Adversaries can use the rc.common file as a way to hide code for persistence that will execute on each reboot as the root user .

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
- T1163: https://attack.mitre.org/techniques/T1163
- Reviewed: 2026-10-27
