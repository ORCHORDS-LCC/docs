# Clear Linux or Mac System Logs Technique Operationalization Review

## Reference

- Technique: **T1070.002 — Clear Linux or Mac System Logs**

Adversaries may clear system logs to hide evidence of an intrusion. macOS and Linux both keep track of system or user-initiated actions via system logs. The majority of native system logging is stored under the <code>/var/log/</code> directory. Subfolders in this directory categorize logs by their related functions, such as: * <code>/var/log/messages:</code>: General and system-related messages * <code>/var/log/secure</code> or <code>/var/log/auth.log</code>: Authentication logs * <code>/var/log/utmp</code> or <code>/var/log/wtmp</code>: Login records * <code>/var/log/kern.log</code>: Kernel logs * <code>/var/log/cron.log</code>: Crond logs * <code>/var/log/maillog</code>: Mail server logs * <code>/var/log/httpd/</code>: Web server access and error logs.

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
- T1070.002: https://attack.mitre.org/techniques/T1070/002
- Reviewed: 2026-10-27
