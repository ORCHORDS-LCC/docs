# User Training Technique Response Playbook

## Target technique

**M1017 — User Training**


User Training involves educating employees and contractors on recognizing, reporting, and preventing cyber threats that rely on human interaction, such as phishing, social engineering, and other manipulative techniques. Comprehensive training programs create a human firewall by empowering users to be an active component of the organization's cybersecurity defenses. This mitigation can be implemented through the following measures: Create Comprehensive Training Programs: - Design training modules tailored to the organization's risk profile, covering topics such as phishing, password management, and incident reporting. - Provide role-specific training for high-risk employees, such as helpdesk staff or executives. Use Simulated Exercises: - Conduct phishing simulations to measure user susceptibility and provide targeted follow-up training. - Run social engineering drills to evaluate employee responses and reinforce protocols. Leverage Gamification and Engagement: - Introduce interactive learning methods such as quizzes, gamified challenges, and rewards for successful detection and reporting of threats. Incorporate Security Policies into Onboarding: - Include cybersecurity training as part of the onboarding process for new employees. - Provide easy-to-understand materials outlining acceptable use policies and reporting procedures. Regular Refresher Courses: - Update training materials to include emerging threats and techniques used by adversaries. - Ensure all employees complete periodic refresher courses to stay informed. Emphasize Real-World Scenarios: - Use case studies of recent attacks to demonstrate the consequences of successful phishing or social engineering. - Discuss how specific employee actions can prevent or mitigate such attacks.

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
- M1017: https://attack.mitre.org/mitigations/M1017
- Reviewed: 2026-10-27
