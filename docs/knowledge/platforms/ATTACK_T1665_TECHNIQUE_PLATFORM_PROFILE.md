# Hide Infrastructure Technique Platform Profile

## Reference

- Technique: **T1665 — Hide Infrastructure**
- Platforms named in the source: ESXi, Linux, macOS, Network Devices, Windows

Adversaries may manipulate network traffic in order to hide and evade detection of their C2 infrastructure. This can be accomplished by identifying and filtering traffic from defensive tools, masking malicious domains to obfuscate the true destination from both automated scanning tools and security researchers, and otherwise hiding malicious artifacts to delay discovery and prolong the effectiveness of adversary infrastructure that could otherwise be identified, blocked, or taken down entirely. C2 networks may include the use of Proxy or VPNs to disguise IP addresses, which can allow adversaries to blend in with normal network traffic and bypass conditional access policies or anti-abuse protections. For example, an adversary may use a virtual private cloud to spoof their IP address to closer align with a victim's IP address ranges. This may also bypass security measures relying on geolocation of the source IP address. Adversaries may also attempt to filter network traffic in order to evade defensive tools in numerous ways, including blocking/redirecting common incident responder or security appliance user agents. Filtering traffic based on IP and geo-fencing may also avoid automated sandboxing or researcher activity (i.e., Virtualization/Sandbox Evasion). Hiding C2 infrastructure may also be supported by Resource Development activities such as Acquire Infrastructure and Compromise Infrastructure. For example, using widely trusted hosting services or domains such as prominent URL shortening providers or marketing services for C2 networks may enable adversaries to present benign content that later redirects victims to malicious web pages or infrastructure once specific conditions are met.

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
- T1665: https://attack.mitre.org/techniques/T1665
- Reviewed: 2026-10-27
