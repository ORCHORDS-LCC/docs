# Medusa Ransomware Technique Platform Profile

## Reference

- Technique: **S1244 — Medusa Ransomware**
- Platforms named in the source: not stated

Medusa Ransomware has been utilized in attacks since at least 2021. Medusa Ransomware has been known to be utilized in conjunction with living off the land techniques and remote management software. Medusa Ransomware has been used in campaigns associated with “double extortion” ransomware activity, where data is exfiltrated from victim environments prior to encryption, with threats to publish files if a ransom is not paid. Medusa Ransomware software was initially a closed ransomware variant which later evolved to a Ransomware as a Service (RaaS). Medusa Ransomware has impacted victims from a diverse range of sectors within a multitude of countries, and it is assessed Medusa Ransomware is used in an opportunistic manner.

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
- S1244: https://attack.mitre.org/software/S1244
- Reviewed: 2026-10-27
