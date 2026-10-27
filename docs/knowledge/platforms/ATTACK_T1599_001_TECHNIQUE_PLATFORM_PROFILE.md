# Network Address Translation Traversal Technique Platform Profile

## Reference

- Technique: **T1599.001 — Network Address Translation Traversal**
- Platforms named in the source: Network Devices

Adversaries may bridge network boundaries by modifying a network device’s Network Address Translation (NAT) configuration. Malicious modifications to NAT may enable an adversary to bypass restrictions on traffic routing that otherwise separate trusted and untrusted networks. Network devices such as routers and firewalls that connect multiple networks together may implement NAT during the process of passing packets between networks. When performing NAT, the network device will rewrite the source and/or destination addresses of the IP address header. Some network designs require NAT for the packets to cross the border device. A typical example of this is environments where internal networks make use of non-Internet routable addresses. When an adversary gains control of a network boundary device, they may modify NAT configurations to send traffic between two separated networks, or to obscure their activities. In network designs that require NAT to function, such modifications enable the adversary to overcome inherent routing limitations that would normally prevent them from accessing protected systems behind the border device. In network designs that do not require NAT, adversaries may use address translation to further obscure their activities, as changing the addresses of packets that traverse a network boundary device can make monitoring data transmissions more challenging for defenders. Adversaries may use Patch System Image to change the operating system of a network device, implementing their own custom NAT mechanisms to further obscure their activities.

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
- T1599.001: https://attack.mitre.org/techniques/T1599/001
- Reviewed: 2026-10-27
