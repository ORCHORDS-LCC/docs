# Content Injection Technique Platform Profile

## Reference

- Technique: **T1659 — Content Injection**
- Platforms named in the source: Linux, macOS, Windows

Adversaries may gain access and continuously communicate with victims by injecting malicious content into systems through online network traffic. Rather than luring victims to malicious payloads hosted on a compromised website (i.e., Drive-by Target followed by Drive-by Compromise), adversaries may initially access victims through compromised data-transfer channels where they can manipulate traffic and/or inject their own content. These compromised online network channels may also be used to deliver additional payloads (i.e., Ingress Tool Transfer) and other data to already compromised systems. Adversaries may inject content to victim systems in various ways, including: * From the middle, where the adversary is in-between legitimate online client-server communications (**Note:** this is similar but distinct from Adversary-in-the-Middle, which describes AiTM activity solely within an enterprise environment) * From the side, where malicious content is injected and races to the client as a fake response to requests of a legitimate online server Content injection is often the result of compromised upstream communication channels, for example at the level of an internet service provider (ISP) as is the case with "lawful interception.".

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
- T1659: https://attack.mitre.org/techniques/T1659
- Reviewed: 2026-10-27
