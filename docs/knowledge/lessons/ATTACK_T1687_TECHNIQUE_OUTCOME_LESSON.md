# T1687 Exploitation for Defense Impairment Outcome Lesson

## Authoritative description

- Technique: **T1687 — Exploitation for Defense Impairment**
- Tactics: defense-impairment
- Platforms: IaaS, Linux, macOS, SaaS, Windows

Adversaries may exploit vulnerabilities in security software, infrastructure, or defensive components to degrade, disable, or otherwise continue to impair their ability to prevent, detect, or respond to malicious activity. Adversaries may exploit a system or application vulnerability to directly interfere with defensive mechanisms. Exploitation occurs when an adversary takes advantage of a programming error in software, services, or the operating system to execute adversary-controlled code, often with the goal of weakening or disabling protections. Vulnerabilities may exist in security tools such as antivirus, endpoint detection and response (EDR), firewalls, or other monitoring solutions. Adversaries may use prior reconnaissance or perform discovery activities (e.g., Software Discovery) to identify defensive tools present in an environment and target them for exploitation. Successful exploitation may allow adversaries to terminate security processes, disable protections, bypass enforcement mechanisms, or reduce the effectiveness of defensive controls. In some cases, vulnerabilities in cloud-based or SaaS infrastructure may also be leveraged to bypass built-in security boundaries or disrupt visibility and enforcement across environments.

## Reusable lesson

This technique should be treated as an explicit review question when it is relevant to the system or organisation, rather than assumed to be covered by a generic control statement or by tooling that reports a related signal.

## Apply the lesson

1. Define the real scope before judging coverage.
2. Inspect current technical, process, governance, or operational evidence.
3. Separate documented intent from verified behaviour.
4. Record partial coverage and unresolved gaps instead of converting them into a pass.
5. Revisit when the underlying scope, threat environment, technology, suppliers, or mission materially changes.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1687: https://attack.mitre.org/techniques/T1687
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
