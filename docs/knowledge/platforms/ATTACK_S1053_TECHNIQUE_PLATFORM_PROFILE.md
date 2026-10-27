# AvosLocker Technique Platform Profile

## Reference

- Technique: **S1053 — AvosLocker**
- Platforms named in the source: Linux, Windows

AvosLocker is ransomware written in C++ that has been offered via the Ransomware-as-a-Service (RaaS) model. It was first observed in June 2021 and has been used against financial services, critical manufacturing, government facilities, and other critical infrastructure sectors in the United States. As of March 2022, AvosLocker had also been used against organizations in Belgium, Canada, China, Germany, Saudi Arabia, Spain, Syria, Taiwan, Turkey, the United Arab Emirates, and the United Kingdom.

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
- S1053: https://attack.mitre.org/software/S1053
- Reviewed: 2026-10-27
