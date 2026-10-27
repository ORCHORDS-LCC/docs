# Pre-compromise Technique Response Playbook

## Target technique

**M1056 — Pre-compromise**


Pre-compromise mitigations involve proactive measures and defenses implemented to prevent adversaries from successfully identifying and exploiting weaknesses during the Reconnaissance and Resource Development phases of an attack. These activities focus on reducing an organization's attack surface, identify adversarial preparation efforts, and increase the difficulty for attackers to conduct successful operations. This mitigation can be implemented through the following measures: Limit Information Exposure: - Regularly audit and sanitize publicly available data, including job posts, websites, and social media. - Use tools like OSINT monitoring platforms (e.g., SpiderFoot, Recon-ng) to identify leaked information. Protect Domain and DNS Infrastructure: - Enable DNSSEC and use WHOIS privacy protection. - Monitor for domain hijacking or lookalike domains using services like RiskIQ or DomainTools. External Monitoring: - Use tools like Shodan, Censys to monitor your external attack surface. - Deploy external vulnerability scanners to proactively address weaknesses. Threat Intelligence: - Leverage platforms like MISP, Recorded Future, or Anomali to track adversarial infrastructure, tools, and activity. Content and Email Protections: - Use email security solutions like Proofpoint, Microsoft Defender for Office 365, or Mimecast. - Enforce SPF/DKIM/DMARC policies to protect against email spoofing. Training and Awareness: - Educate employees on identifying phishing attempts, securing their social media, and avoiding information leaks.

## Preconditions

- the estate in scope is identified, with the systems the technique could apply to;
- an owner is accountable for detection and response;
- current telemetry and configuration can be inspected;
- the technique is applicable or requires an applicability decision.

## Procedure

1. Confirm the scope and owner.
2. Read the current technique description and the associated detection guidance.
3. Inventory the telemetry that would carry the technique's indicators.
4. Inspect whether the indicators are present in the environment.
5. Exercise the detection path and confirm it produces the expected signal.
6. Record gaps in detection coverage and assign remediation owners.
7. Record justified non-applicability or accepted detection gaps separately.
8. Set the next event-driven or periodic verification trigger.

## Failure handling

If the detection path does not produce the expected signal, treat the coverage as unverified, preserve the test evidence, and route the gap through the appropriate remediation or risk process.

## Completion evidence

Scope, owner, source version, telemetry inspected, tests performed, findings, exceptions, remediation links, reviewer, and next trigger.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- M1056: https://attack.mitre.org/mitigations/M1056
- Reviewed: 2026-10-27
