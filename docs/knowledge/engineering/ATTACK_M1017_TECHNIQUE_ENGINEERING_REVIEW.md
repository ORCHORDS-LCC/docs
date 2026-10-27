# User Training Technique Engineering Review

## Reference

- Technique: **M1017 — User Training**

User Training involves educating employees and contractors on recognizing, reporting, and preventing cyber threats that rely on human interaction, such as phishing, social engineering, and other manipulative techniques. Comprehensive training programs create a human firewall by empowering users to be an active component of the organization's cybersecurity defenses. This mitigation can be implemented through the following measures: Create Comprehensive Training Programs: - Design training modules tailored to the organization's risk profile, covering topics such as phishing, password management, and incident reporting. - Provide role-specific training for high-risk employees, such as helpdesk staff or executives. Use Simulated Exercises: - Conduct phishing simulations to measure user susceptibility and provide targeted follow-up training. - Run social engineering drills to evaluate employee responses and reinforce protocols. Leverage Gamification and Engagement: - Introduce interactive learning methods such as quizzes, gamified challenges, and rewards for successful detection and reporting of threats. Incorporate Security Policies into Onboarding: - Include cybersecurity training as part of the onboarding process for new employees. - Provide easy-to-understand materials outlining acceptable use policies and reporting procedures. Regular Refresher Courses: - Update training materials to include emerging threats and techniques used by adversaries. - Ensure all employees complete periodic refresher courses to stay informed. Emphasize Real-World Scenarios: - Use case studies of recent attacks to demonstrate the consequences of successful phishing or social engineering. - Discuss how specific employee actions can prevent or mitigate such attacks.

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
- M1017: https://attack.mitre.org/mitigations/M1017
- Reviewed: 2026-10-27
