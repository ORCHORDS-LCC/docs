# T1071.005 Publish/Subscribe Protocols Outcome Lesson

## Authoritative description

- Technique: **T1071.005 — Publish/Subscribe Protocols**
- Tactics: command-and-control
- Platforms: macOS, Linux, Windows, Network Devices

Adversaries may communicate using publish/subscribe (pub/sub) application layer protocols to avoid detection/network filtering by blending in with existing traffic. Commands to the remote system, and often the results of those commands, will be embedded within the protocol traffic between the client and server. Protocols such as <code>MQTT</code>, <code>XMPP</code>, <code>AMQP</code>, and <code>STOMP</code> use a publish/subscribe design, with message distribution managed by a centralized broker. Publishers categorize their messages by topics, while subscribers receive messages according to their subscribed topics. An adversary may abuse publish/subscribe protocols to communicate with systems under their control from behind a message broker while also mimicking normal, expected traffic.

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
- T1071.005: https://attack.mitre.org/techniques/T1071/005
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
