# Publish/Subscribe Protocols Technique Platform Profile

## Reference

- Technique: **T1071.005 — Publish/Subscribe Protocols**
- Platforms named in the source: macOS, Linux, Windows, Network Devices

Adversaries may communicate using publish/subscribe (pub/sub) application layer protocols to avoid detection/network filtering by blending in with existing traffic. Commands to the remote system, and often the results of those commands, will be embedded within the protocol traffic between the client and server. Protocols such as MQTT, XMPP, AMQP, and STOMP use a publish/subscribe design, with message distribution managed by a centralized broker. Publishers categorize their messages by topics, while subscribers receive messages according to their subscribed topics. An adversary may abuse publish/subscribe protocols to communicate with systems under their control from behind a message broker while also mimicking normal, expected traffic.

## Platform profile

1. Record the platforms in scope and the versions actually deployed.
2. Compare the deployed platform surface against the platforms the source names.
3. Record where the platform provides a native control for the technique, and where it does not.
4. Record the configuration evidence for the native control, where one exists.
5. Record the gap where the platform provides no native control, and the compensating detection.
6. Record the platform version, because platform behaviour changes between versions.

## Evidence

- the platform and version inventory for the scoped estate;
- the configuration export or screenshot for the native control;
- the detection evidence where the platform provides none.

## Limitations

A technique entry describes a class of abuse across platforms. The platform-specific exposure is a property of the deployment, established only by inventory and configuration evidence.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1071.005: https://attack.mitre.org/techniques/T1071/005
- Reviewed: 2026-10-27
