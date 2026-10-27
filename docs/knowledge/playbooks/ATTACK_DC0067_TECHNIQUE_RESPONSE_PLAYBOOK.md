# Logon Session Creation Technique Response Playbook

## Target technique

**DC0067 — Logon Session Creation**


The successful establishment of a new user session following a successful authentication attempt. This typically signifies that a user has provided valid credentials or authentication tokens, and the system has initiated a session associated with that user account. This data is crucial for tracking authentication events and identifying potential unauthorized access. Examples: - Windows Systems - Event ID: 4624 - Logon Type: 2 (Interactive) or 10 (Remote Interactive via RDP). - Account Name: JohnDoe - Source Network Address: 192.168.1.100 - Authentication Package: NTLM - Linux Systems - /var/log/utmp or /var/log/wtmp: - Log format: login user [tty] from [source_ip] - User: jane - IP: 10.0.0.5 - Timestamp: 2024-12-28 08:30:00 - macOS Systems - /var/log/asl.log or unified logging framework: - Log: com.apple.securityd: Authentication succeeded for user 'admin' - Cloud Environments - Azure Sign-In Logs: - Activity: Sign-in successful - Client App: Browser - Location: Unknown (Country: X) - Google Workspace - Activity: Login - Event Type: successful_login - Source IP: 203.0.113.55.

## Preconditions

- the estate in scope is identified, with the systems the technique could apply to;
- an owner is accountable for detection and response;
- current telemetry and configuration can be inspected;
- the technique is applicable or requires an applicability decision.

## Procedure

1. Confirm the scope and owner.
2. Read the current technique description and the associated detection guidance.
3. Inventory the telemetry that would carry the technique's indicators.
4. Inspect whether the indicators are present in the environment.
5. Exercise the detection path and confirm it produces the expected signal.
6. Record gaps in detection coverage and assign remediation owners.
7. Record justified non-applicability or accepted detection gaps separately.
8. Set the next event-driven or periodic verification trigger.

## Failure handling

If the detection path does not produce the expected signal, treat the coverage as unverified, preserve the test evidence, and route the gap through the appropriate remediation or risk process.

## Completion evidence

Scope, owner, source version, telemetry inspected, tests performed, findings, exceptions, remediation links, reviewer, and next trigger.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- DC0067: https://attack.mitre.org/datacomponents/DC0067
- Reviewed: 2026-10-27
