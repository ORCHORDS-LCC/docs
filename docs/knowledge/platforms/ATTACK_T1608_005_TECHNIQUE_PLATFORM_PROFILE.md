# Link Target Technique Platform Profile

## Reference

- Technique: **T1608.005 — Link Target**
- Platforms named in the source: PRE

Adversaries may put in place resources that are referenced by a link that can be used during targeting. An adversary may rely upon a user clicking a malicious link in order to divulge information (including credentials) or to gain execution, as in Malicious Link. Links can be used for spearphishing, such as sending an email accompanied by social engineering text to coax the user to actively click or copy and paste a URL into a browser. Prior to a phish for information (as in Spearphishing Link) or a phish to gain initial access to a system (as in Spearphishing Link), an adversary must set up the resources for a link target for the spearphishing link. Typically, the resources for a link target will be an HTML page that may include some client-side script such as JavaScript to decide what content to serve to the user. Adversaries may clone legitimate sites to serve as the link target, this can include cloning of login pages of legitimate web services or organization login pages in an effort to harvest credentials during Spearphishing Link. Adversaries may also Upload Malware and have the link target point to malware for download/execution by the user. Adversaries may purchase domains similar to legitimate domains (ex: homoglyphs, typosquatting, different top-level domain, etc.) during acquisition of infrastructure (Domains) to help facilitate Malicious Link. Links can be written by adversaries to mask the true destination in order to deceive victims by abusing the URL schema and increasing the effectiveness of phishing. Adversaries may also use free or paid accounts on link shortening services and Platform-as-a-Service providers to host link targets while taking advantage of the widely trusted domains of those providers to avoid being blocked while redirecting victims to malicious pages. In addition, adversaries may serve a variety of malicious links through uniquely generated URIs/URLs (including one-time, single use links). Finally, adversaries may take advantage of the decentralized nature of the InterPlanetary File System (IPFS) to host link targets that are difficult to remove.

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
- T1608.005: https://attack.mitre.org/techniques/T1608/005
- Reviewed: 2026-10-27
