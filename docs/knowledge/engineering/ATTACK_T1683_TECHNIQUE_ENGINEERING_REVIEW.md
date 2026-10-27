# Generate Content Technique Engineering Review

## Reference

- Technique: **T1683 — Generate Content**

Adversaries may create or generate content to support targeting and operations. This content may be used to establish personas, impersonate known individuals or organizations, and support Social Engineering, fraud, or influence activities. Written materials, audio, images, video, or other media may be developed and tailored to the target and objective. Content development may occur prior to or during an operation. Adversaries may develop or generate content in-house, source it through third parties, or produce it using AI-assisted tools. Adversaries may use AI to research targets, develop pretexts, and better understand the organizations and individuals they intend to target or deceive prior to generating content (i.e., Query Public AI Services); for obtaining access to AI tools used in content generation, see Artificial Intelligence. Content may be leveraged in support of techniques such as Phishing, Phishing for Information, Social Engineering, Financial Theft, or Establish Accounts. Generated or developed content does not include malicious code or scripts (i.e., Develop Capabilities and Artificial Intelligence).

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
- T1683: https://attack.mitre.org/techniques/T1683
- Reviewed: 2026-10-27
