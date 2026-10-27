# T1557.003 DHCP Spoofing Outcome Lesson

## Authoritative description

- Technique: **T1557.003 — DHCP Spoofing**
- Tactics: credential-access, collection
- Platforms: Linux, Windows, macOS

Adversaries may redirect network traffic to adversary-owned systems by spoofing Dynamic Host Configuration Protocol (DHCP) traffic and acting as a malicious DHCP server on the victim network. By achieving the adversary-in-the-middle (AiTM) position, adversaries may collect network communications, including passed credentials, especially those sent over insecure, unencrypted protocols. This may also enable follow-on behaviors such as Network Sniffing or Transmitted Data Manipulation. DHCP is based on a client-server model and has two functionalities: a protocol for providing network configuration settings from a DHCP server to a client and a mechanism for allocating network addresses to clients. The typical server-client interaction is as follows: 1. The client broadcasts a `DISCOVER` message. 2. The server responds with an `OFFER` message, which includes an available network address. 3. The client broadcasts a `REQUEST` message, which includes the network address offered. 4. The server acknowledges with an `ACK` message and the client receives the network configuration parameters. Adversaries may spoof as a rogue DHCP server on the victim network, from which legitimate hosts may receive malicious network configurations. For example, malware can act as a DHCP server and provide adversary-owned DNS servers to the victimized computers. Through the malicious network configurations, an adversary may achieve the AiTM position, route client traffic through adversary-controlled systems, and collect information from the client network. DHCPv6 clients can receive network configuration information without being assigned an IP address by sending a INFORMATION-REQUEST (code 11) message to the All_DHCP_Relay_Agents_and_Servers multicast address. Adversaries may use their rogue DHCP server to respond to this request message with malicious network configurations. Rather than establishing an AiTM position, adversaries may also abuse DHCP spoofing to perform a DHCP exhaustion attack (i.e, Service Exhaustion Flood) by generating many broadcast DISCOVER messages to exhaust a network’s DHCP allocation pool.

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
- T1557.003: https://attack.mitre.org/techniques/T1557/003
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
