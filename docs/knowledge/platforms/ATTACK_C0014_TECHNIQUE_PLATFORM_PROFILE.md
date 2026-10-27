# Operation Wocao Technique Platform Profile

## Reference

- Technique: **C0014 — Operation Wocao**
- Platforms named in the source: not stated

Operation Wocao was a cyber espionage campaign that targeted organizations around the world, including in Brazil, China, France, Germany, Italy, Mexico, Portugal, Spain, the United Kingdom, and the United States. The suspected China-based actors compromised government organizations and managed service providers, as well as aviation, construction, energy, finance, health care, insurance, offshore engineering, software development, and transportation companies. Security researchers assessed the Operation Wocao actors used similar TTPs and tools as APT20, suggesting a possible overlap. Operation Wocao was named after an observed command line entry by one of the threat actors, possibly out of frustration from losing webshell access.

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
- C0014: https://attack.mitre.org/campaigns/C0014
- Reviewed: 2026-10-27
