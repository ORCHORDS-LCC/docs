# Generate Content Technique Platform Profile

## Reference

- Technique: **T1683 — Generate Content**
- Platforms named in the source: PRE

Adversaries may create or generate content to support targeting and operations. This content may be used to establish personas, impersonate known individuals or organizations, and support Social Engineering, fraud, or influence activities. Written materials, audio, images, video, or other media may be developed and tailored to the target and objective. Content development may occur prior to or during an operation. Adversaries may develop or generate content in-house, source it through third parties, or produce it using AI-assisted tools. Adversaries may use AI to research targets, develop pretexts, and better understand the organizations and individuals they intend to target or deceive prior to generating content (i.e., Query Public AI Services); for obtaining access to AI tools used in content generation, see Artificial Intelligence. Content may be leveraged in support of techniques such as Phishing, Phishing for Information, Social Engineering, Financial Theft, or Establish Accounts. Generated or developed content does not include malicious code or scripts (i.e., Develop Capabilities and Artificial Intelligence).

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
- T1683: https://attack.mitre.org/techniques/T1683
- Reviewed: 2026-10-27
