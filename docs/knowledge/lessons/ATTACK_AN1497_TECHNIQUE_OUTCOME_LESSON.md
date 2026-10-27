# AN1497 Analytic 1497 Outcome Lesson

## Authoritative description

- Technique: **AN1497 — Analytic 1497**
- Platforms: Linux

Processes (e.g., bash, python, custom binaries) dynamically linking libcrypto/libssl for RSA key exchange, then creating external connections with abnormal certificate validation or handshake anomalies. Defender observes syscall traces and outbound asymmetric key exchanges from non-SSL-native processes.

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
- AN1497: https://attack.mitre.org/detectionstrategies/DET0543#AN1497
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
