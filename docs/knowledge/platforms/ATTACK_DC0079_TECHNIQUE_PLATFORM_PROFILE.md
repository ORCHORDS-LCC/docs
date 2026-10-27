# Driver Load Technique Platform Profile

## Reference

- Technique: **DC0079 — Driver Load**
- Platforms named in the source: not stated

The process of attaching a driver, which is a software component that allows the operating system and applications to interact with hardware devices, to either user-mode or kernel-mode of a system. This can include benign actions (e.g., hardware drivers) or malicious behavior (e.g., rootkits or unsigned drivers). Examples: - Legitimate Driver Loading: A new graphics driver from a vendor like NVIDIA or AMD is loaded into the system. - Unsigned Driver Loading: A driver without a valid digital signature is loaded into the kernel. - Rootkit Installation: A malicious rootkit driver is loaded to manipulate kernel-mode processes. - Anti-Virus or EDR Driver Loading: An Endpoint Detection and Response (EDR) solution loads its driver to monitor system activities. - Driver Misuse: A legitimate driver is loaded and exploited to execute malicious actions, such as using vulnerable drivers for bypassing defenses (e.g., Bring Your Own Vulnerable Driver (BYOVD) attacks).

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
- DC0079: https://attack.mitre.org/datacomponents/DC0079
- Reviewed: 2026-10-27
