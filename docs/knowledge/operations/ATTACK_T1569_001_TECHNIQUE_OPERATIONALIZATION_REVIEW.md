# Launchctl Technique Operationalization Review

## Reference

- Technique: **T1569.001 — Launchctl**

Adversaries may abuse launchctl to execute commands or programs. Launchctl interfaces with launchd, the service management framework for macOS. Launchctl supports taking subcommands on the command-line, interactively, or even redirected from standard input. Adversaries use launchctl to execute commands and programs as Launch Agents or Launch Daemons. Common subcommands include: <code>launchctl load</code>,<code>launchctl unload</code>, and <code>launchctl start</code>. Adversaries can use scripts or manually run the commands <code>launchctl load -w "%s/Library/LaunchAgents/%s"</code> or <code>/bin/launchctl load</code> to execute Launch Agents or Launch Daemons.

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
- T1569.001: https://attack.mitre.org/techniques/T1569/001
- Reviewed: 2026-10-27
