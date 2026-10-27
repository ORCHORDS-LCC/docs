# Multi-hop Proxy Technique Platform Profile

## Reference

- Technique: **T1090.003 — Multi-hop Proxy**
- Platforms named in the source: ESXi, Linux, macOS, Network Devices, Windows

Adversaries may chain together multiple proxies to disguise the source of malicious traffic. Typically, a defender will be able to identify the last proxy traffic traversed before it enters their network; the defender may or may not be able to identify any previous proxies before the last-hop proxy. This technique makes identifying the original source of the malicious traffic even more difficult by requiring the defender to trace malicious traffic through several proxies to identify its source. For example, adversaries may construct or use onion routing networks – such as the publicly available Tor network – to transport encrypted C2 traffic through a compromised population, allowing communication with any device within the network. Adversaries may also use operational relay box (ORB) networks composed of virtual private servers (VPS), Internet of Things (IoT) devices, smart devices, and end-of-life routers to obfuscate their operations. In the case of network infrastructure, it is possible for an adversary to leverage multiple compromised devices to create a multi-hop proxy chain (i.e., Network Devices). By leveraging Patch System Image on routers, adversaries can add custom code to the affected network devices that will implement onion routing between those nodes. This method is dependent upon the Network Boundary Bridging method allowing the adversaries to cross the protected network boundary of the Internet perimeter and into the organization’s Wide-Area Network (WAN). Protocols such as ICMP may be used as a transport. Similarly, adversaries may abuse peer-to-peer (P2P) and blockchain-oriented infrastructure to implement routing between a decentralized network of peers.

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
- T1090.003: https://attack.mitre.org/techniques/T1090/003
- Reviewed: 2026-10-27
