# Query Public AI Services Technique Platform Profile

## Reference

- Technique: **T1682 — Query Public AI Services**
- Platforms named in the source: PRE

Adversaries may query publicly accessible artificial intelligence (AI) services, such as large language models (LLMs), to support targeting and operations. In addition to searching websites or databases directly (i.e., Search Open Websites/Domains), adversaries may use AI services to synthesize, aggregate, and analyze publicly available information at scale. This may include identifying individuals or organizations to target, researching organizational structures and personnel, identifying technologies used by target organizations, researching business relationships to develop plausible pretexts for Social Engineering approaches, identifying contact information for use in Phishing or Phishing for Information, or gathering derogatory or sensitive information about individuals that may be used for extortion or coercion. Information gathered through AI services may be leveraged for other behaviors, such as establishing operational resources (i.e., Generate Content or Establish Accounts. For obtaining access to AI tools and services, see Artificial Intelligence.

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
- T1682: https://attack.mitre.org/techniques/T1682
- Reviewed: 2026-10-27
