# Remote Desktop Software Technique Operationalization Review

## Reference

- Technique: **T1219.002 — Remote Desktop Software**

An adversary may use legitimate desktop support software to establish an interactive command and control channel to target systems within networks. Desktop support software provides a graphical interface for remotely controlling another computer, transmitting the display output, keyboard input, and mouse control between devices using various protocols. Desktop support software, such as `VNC`, `Team Viewer`, `AnyDesk`, `ScreenConnect`, `LogMein`, `AmmyyAdmin`, and other remote monitoring and management (RMM) tools, are commonly used as legitimate technical support software and may be allowed by application control within a target environment. Remote access modules/features may also exist as part of otherwise existing software such as Zoom or Google Chrome’s Remote Desktop.

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
- T1219.002: https://attack.mitre.org/techniques/T1219/002
- Reviewed: 2026-10-27
