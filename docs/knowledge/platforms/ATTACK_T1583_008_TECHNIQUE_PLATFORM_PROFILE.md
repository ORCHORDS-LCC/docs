# Malvertising Technique Platform Profile

## Reference

- Technique: **T1583.008 — Malvertising**
- Platforms named in the source: PRE

Adversaries may purchase online advertisements that can be abused to distribute malware to victims. Ads can be purchased to plant as well as favorably position artifacts in specific locations online, such as prominently placed within search engine results. These ads may make it more difficult for users to distinguish between actual search results and advertisements. Purchased ads may also target specific audiences using the advertising network’s capabilities, potentially further taking advantage of the trust inherently given to search engines and popular websites. Adversaries may purchase ads and other resources to help distribute artifacts containing malicious code to victims. Purchased ads may attempt to impersonate or spoof well-known brands. For example, these spoofed ads may trick victims into clicking the ad which could then send them to a malicious domain that may be a clone of official websites containing trojanized versions of the advertised software. Adversary’s efforts to create malicious domains and purchase advertisements may also be automated at scale to better resist cleanup efforts. Malvertising may be used to support Drive-by Target and Drive-by Compromise, potentially requiring limited interaction from the user if the ad contains code/exploits that infect the target system's web browser. Adversaries may also employ several techniques to evade detection by the advertising network. For example, adversaries may dynamically route ad clicks to send automated crawler/policy enforcer traffic to benign sites while validating potential targets then sending victims referred from real ad clicks to malicious pages. This infection vector may therefore remain hidden from the ad network as well as any visitor not reaching the malicious sites with a valid identifier from clicking on the advertisement. Other tricks, such as intentional typos to avoid brand reputation monitoring, may also be used to evade automated detection.

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
- T1583.008: https://attack.mitre.org/techniques/T1583/008
- Reviewed: 2026-10-27
