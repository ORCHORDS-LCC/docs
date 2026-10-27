# Udev Rules Technique Operationalization Review

## Reference

- Technique: **T1546.017 — Udev Rules**

Adversaries may maintain persistence through executing malicious content triggered using udev rules. Udev is the Linux kernel device manager that dynamically manages device nodes, handles access to pseudo-device files in the `/dev` directory, and responds to hardware events, such as when external devices like hard drives or keyboards are plugged in or removed. Udev uses rule files with `match keys` to specify the conditions a hardware event must meet and `action keys` to define the actions that should follow. Root permissions are required to create, modify, or delete rule files located in `/etc/udev/rules.d/`, `/run/udev/rules.d/`, `/usr/lib/udev/rules.d/`, `/usr/local/lib/udev/rules.d/`, and `/lib/udev/rules.d/`. Rule priority is determined by both directory and by the digit prefix in the rule filename. Adversaries may abuse the udev subsystem by adding or modifying rules in udev rule files to execute malicious content. For example, an adversary may configure a rule to execute their binary each time the pseudo-device file, such as `/dev/random`, is accessed by an application. Although udev is limited to running short tasks and is restricted by systemd-udevd's sandbox (blocking network and filesystem access), attackers may use scripting commands under the action key `RUN+=` to detach and run the malicious content’s process in the background to bypass these controls.

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
- T1546.017: https://attack.mitre.org/techniques/T1546/017
- Reviewed: 2026-10-27
