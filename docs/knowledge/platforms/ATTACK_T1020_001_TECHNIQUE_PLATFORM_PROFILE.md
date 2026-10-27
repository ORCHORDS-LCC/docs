# Traffic Duplication Technique Platform Profile

## Reference

- Technique: **T1020.001 — Traffic Duplication**
- Platforms named in the source: Network Devices, IaaS

Adversaries may leverage traffic mirroring in order to automate data exfiltration over compromised infrastructure. Traffic mirroring is a native feature for some devices, often used for network analysis. For example, devices may be configured to forward network traffic to one or more destinations for analysis by a network analyzer or other monitoring device. Adversaries may abuse traffic mirroring to mirror or redirect network traffic through other infrastructure they control. Malicious modifications to network devices to enable traffic redirection may be possible through ROMMONkit or Patch System Image. Many cloud-based environments also support traffic mirroring. For example, AWS Traffic Mirroring, GCP Packet Mirroring, and Azure vTap allow users to define specified instances to collect traffic from and specified targets to send collected traffic to. Adversaries may use traffic duplication in conjunction with Network Sniffing, Input Capture, or Adversary-in-the-Middle depending on the goals and objectives of the adversary.

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
- T1020.001: https://attack.mitre.org/techniques/T1020/001
- Reviewed: 2026-10-27
