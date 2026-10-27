# Restrict Web-Based Content Technique Response Playbook

## Target technique

**M1021 — Restrict Web-Based Content**


Restricting web-based content involves enforcing policies and technologies that limit access to potentially malicious websites, unsafe downloads, and unauthorized browser behaviors. This can include URL filtering, download restrictions, script blocking, and extension control to protect against exploitation, phishing, and malware delivery. This mitigation can be implemented through the following measures: Deploy Web Proxy Filtering: - Use solutions to filter web traffic based on categories, reputation, and content types. - Enforce policies that block unsafe websites or file types at the gateway level. Enable DNS-Based Filtering: - Implement tools to restrict access to domains associated with malware or phishing campaigns. - Use public DNS filtering services to enhance protection. Enforce Content Security Policies (CSP): - Configure CSP headers on internal and external web applications to restrict script execution, iframe embedding, and cross-origin requests. Control Browser Features: - Disable unapproved browser features like automatic downloads, developer tools, or unsafe scripting. - Enforce policies through tools like Group Policy Management to control browser settings. Monitor and Alert on Web-Based Threats: - Use SIEM tools to collect and analyze web proxy logs for signs of anomalous or malicious activity. - Configure alerts for access attempts to blocked domains or repeated file download failures.

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
- M1021: https://attack.mitre.org/mitigations/M1021
- Reviewed: 2026-10-27
