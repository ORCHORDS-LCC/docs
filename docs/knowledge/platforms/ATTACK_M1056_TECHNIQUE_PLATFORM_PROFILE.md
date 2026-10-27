# Pre-compromise Technique Platform Profile

## Reference

- Technique: **M1056 — Pre-compromise**
- Platforms named in the source: not stated

Pre-compromise mitigations involve proactive measures and defenses implemented to prevent adversaries from successfully identifying and exploiting weaknesses during the Reconnaissance and Resource Development phases of an attack. These activities focus on reducing an organization's attack surface, identify adversarial preparation efforts, and increase the difficulty for attackers to conduct successful operations. This mitigation can be implemented through the following measures: Limit Information Exposure: - Regularly audit and sanitize publicly available data, including job posts, websites, and social media. - Use tools like OSINT monitoring platforms (e.g., SpiderFoot, Recon-ng) to identify leaked information. Protect Domain and DNS Infrastructure: - Enable DNSSEC and use WHOIS privacy protection. - Monitor for domain hijacking or lookalike domains using services like RiskIQ or DomainTools. External Monitoring: - Use tools like Shodan, Censys to monitor your external attack surface. - Deploy external vulnerability scanners to proactively address weaknesses. Threat Intelligence: - Leverage platforms like MISP, Recorded Future, or Anomali to track adversarial infrastructure, tools, and activity. Content and Email Protections: - Use email security solutions like Proofpoint, Microsoft Defender for Office 365, or Mimecast. - Enforce SPF/DKIM/DMARC policies to protect against email spoofing. Training and Awareness: - Educate employees on identifying phishing attempts, securing their social media, and avoiding information leaks.

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
- M1056: https://attack.mitre.org/mitigations/M1056
- Reviewed: 2026-10-27
