# Pre-compromise Technique Engineering Review

## Reference

- Technique: **M1056 — Pre-compromise**

Pre-compromise mitigations involve proactive measures and defenses implemented to prevent adversaries from successfully identifying and exploiting weaknesses during the Reconnaissance and Resource Development phases of an attack. These activities focus on reducing an organization's attack surface, identify adversarial preparation efforts, and increase the difficulty for attackers to conduct successful operations. This mitigation can be implemented through the following measures: Limit Information Exposure: - Regularly audit and sanitize publicly available data, including job posts, websites, and social media. - Use tools like OSINT monitoring platforms (e.g., SpiderFoot, Recon-ng) to identify leaked information. Protect Domain and DNS Infrastructure: - Enable DNSSEC and use WHOIS privacy protection. - Monitor for domain hijacking or lookalike domains using services like RiskIQ or DomainTools. External Monitoring: - Use tools like Shodan, Censys to monitor your external attack surface. - Deploy external vulnerability scanners to proactively address weaknesses. Threat Intelligence: - Leverage platforms like MISP, Recorded Future, or Anomali to track adversarial infrastructure, tools, and activity. Content and Email Protections: - Use email security solutions like Proofpoint, Microsoft Defender for Office 365, or Mimecast. - Enforce SPF/DKIM/DMARC policies to protect against email spoofing. Training and Awareness: - Educate employees on identifying phishing attempts, securing their social media, and avoiding information leaks.

## Engineering review

1. Identify the engineering boundary where the technique would apply: the component, the service, or the deployment.
2. Review the design decision that would prevent the technique, and record the alternative considered.
3. Review the implementation evidence for the preventive control.
4. Review the test coverage that would fail if the control regressed.
5. Review the observability: which signal would show the control is not operating.
6. Record the residual risk where prevention is not achievable, and the detection that compensates.

## Review evidence

- the design record for the preventive decision;
- the implementation or configuration evidence;
- the test record showing the control is exercised;
- the observability mapping.

## Limitations

An engineering review describes what the design and the implementation evidence show. It does not claim the technique has been addressed in production.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- M1056: https://attack.mitre.org/mitigations/M1056
- Reviewed: 2026-10-27
