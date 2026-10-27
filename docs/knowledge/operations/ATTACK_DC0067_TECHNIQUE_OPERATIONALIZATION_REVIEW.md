# Logon Session Creation Technique Operationalization Review

## Reference

- Technique: **DC0067 — Logon Session Creation**

The successful establishment of a new user session following a successful authentication attempt. This typically signifies that a user has provided valid credentials or authentication tokens, and the system has initiated a session associated with that user account. This data is crucial for tracking authentication events and identifying potential unauthorized access. Examples: - Windows Systems - Event ID: 4624 - Logon Type: 2 (Interactive) or 10 (Remote Interactive via RDP). - Account Name: JohnDoe - Source Network Address: 192.168.1.100 - Authentication Package: NTLM - Linux Systems - /var/log/utmp or /var/log/wtmp: - Log format: login user [tty] from [source_ip] - User: jane - IP: 10.0.0.5 - Timestamp: 2024-12-28 08:30:00 - macOS Systems - /var/log/asl.log or unified logging framework: - Log: com.apple.securityd: Authentication succeeded for user 'admin' - Cloud Environments - Azure Sign-In Logs: - Activity: Sign-in successful - Client App: Browser - Location: Unknown (Country: X) - Google Workspace - Activity: Login - Event Type: successful_login - Source IP: 203.0.113.55.

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
- DC0067: https://attack.mitre.org/datacomponents/DC0067
- Reviewed: 2026-10-27
