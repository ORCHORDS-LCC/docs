# AN1448 Analytic 1448 Outcome Lesson

## Authoritative description

- Technique: **AN1448 — Analytic 1448**
- Platforms: Windows

A remote host sends a short sequence of failed connection attempts (RST/ICMP unreachable) to a set of closed ports. Within a brief window the endpoint (a) adds/enables a firewall rule or (b) a sniffer-backed process begins listening or opens a new socket, after which a successful connection occurs. Also detects Wake-on-LAN magic packets seen on local segment.

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
- AN1448: https://attack.mitre.org/detectionstrategies/DET0524#AN1448
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
