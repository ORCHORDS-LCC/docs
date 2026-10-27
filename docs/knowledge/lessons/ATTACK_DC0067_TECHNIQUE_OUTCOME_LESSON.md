# DC0067 Logon Session Creation Outcome Lesson

## Authoritative description

- Technique: **DC0067 — Logon Session Creation**

The successful establishment of a new user session following a successful authentication attempt. This typically signifies that a user has provided valid credentials or authentication tokens, and the system has initiated a session associated with that user account. This data is crucial for tracking authentication events and identifying potential unauthorized access. Examples: - Windows Systems - Event ID: 4624 - Logon Type: 2 (Interactive) or 10 (Remote Interactive via RDP). - Account Name: JohnDoe - Source Network Address: 192.168.1.100 - Authentication Package: NTLM - Linux Systems - /var/log/utmp or /var/log/wtmp: - Log format: login user [tty] from [source_ip] - User: jane - IP: 10.0.0.5 - Timestamp: 2024-12-28 08:30:00 - macOS Systems - /var/log/asl.log or unified logging framework: - Log: com.apple.securityd: Authentication succeeded for user 'admin' - Cloud Environments - Azure Sign-In Logs: - Activity: Sign-in successful - Client App: Browser - Location: Unknown (Country: X) - Google Workspace - Activity: Login - Event Type: successful_login - Source IP: 203.0.113.55.

## Reusable lesson

This technique should be treated as an explicit review question when it is relevant to the system or organisation, rather than assumed to be covered by a generic control statement or by tooling that reports a related signal.

## Apply the lesson

1. Define the real scope before judging coverage.
2. Inspect current technical, process, governance, or operational evidence.
3. Separate documented intent from verified behaviour.
4. Record partial coverage and unresolved gaps instead of converting them into a pass.
5. Revisit when the underlying scope, threat environment, technology, suppliers, or mission materially changes.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- DC0067: https://attack.mitre.org/datacomponents/DC0067
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
