# Audio-Visual Content Technique Platform Profile

## Reference

- Technique: **T1683.002 — Audio-Visual Content**
- Platforms named in the source: PRE

Adversaries may create or manipulate audio, image, and video content to support targeting and malicious operations. Adversaries may also use synthetic voice recordings, real-time altered audio or video during live interactions, fabricated profile photos and identity documents, or video content depicting fabricated or impersonated individuals. Content may be produced manually through editing tools, generated using AI-assisted tools, or produced using third-party synthetic services. AI-assisted tools have enabled adversaries to produce synthetic media at scale and generate content that is more difficult to identify as inauthentic. Audio-visual content produced through these methods may be used in support of other techniques, such as Phishing, Spearphishing via Service, Phishing for Information, Internal Spearphishing, Social Engineering, Financial Theft, or Establish Accounts.

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
- T1683.002: https://attack.mitre.org/techniques/T1683/002
- Reviewed: 2026-10-27
