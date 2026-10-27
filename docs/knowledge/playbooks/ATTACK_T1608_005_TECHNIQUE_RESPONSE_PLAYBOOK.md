# Link Target Technique Response Playbook

## Target technique

**T1608.005 — Link Target**

- Tactics: resource-development
- Platforms: PRE

Adversaries may put in place resources that are referenced by a link that can be used during targeting. An adversary may rely upon a user clicking a malicious link in order to divulge information (including credentials) or to gain execution, as in Malicious Link. Links can be used for spearphishing, such as sending an email accompanied by social engineering text to coax the user to actively click or copy and paste a URL into a browser. Prior to a phish for information (as in Spearphishing Link) or a phish to gain initial access to a system (as in Spearphishing Link), an adversary must set up the resources for a link target for the spearphishing link. Typically, the resources for a link target will be an HTML page that may include some client-side script such as JavaScript to decide what content to serve to the user. Adversaries may clone legitimate sites to serve as the link target, this can include cloning of login pages of legitimate web services or organization login pages in an effort to harvest credentials during Spearphishing Link. Adversaries may also Upload Malware and have the link target point to malware for download/execution by the user. Adversaries may purchase domains similar to legitimate domains (ex: homoglyphs, typosquatting, different top-level domain, etc.) during acquisition of infrastructure (Domains) to help facilitate Malicious Link. Links can be written by adversaries to mask the true destination in order to deceive victims by abusing the URL schema and increasing the effectiveness of phishing. Adversaries may also use free or paid accounts on link shortening services and Platform-as-a-Service providers to host link targets while taking advantage of the widely trusted domains of those providers to avoid being blocked while redirecting victims to malicious pages. In addition, adversaries may serve a variety of malicious links through uniquely generated URIs/URLs (including one-time, single use links). Finally, adversaries may take advantage of the decentralized nature of the InterPlanetary File System (IPFS) to host link targets that are difficult to remove.

## Preconditions

- the estate in scope is identified, with the systems the technique could apply to;
- an owner is accountable for detection and response;
- current telemetry and configuration can be inspected;
- the technique is applicable or requires an applicability decision.

## Procedure

1. Confirm the scope and owner.
2. Read the current technique description and the associated detection guidance.
3. Inventory the telemetry that would carry the technique's indicators.
4. Inspect whether the indicators are present in the environment.
5. Exercise the detection path and confirm it produces the expected signal.
6. Record gaps in detection coverage and assign remediation owners.
7. Record justified non-applicability or accepted detection gaps separately.
8. Set the next event-driven or periodic verification trigger.

## Failure handling

If the detection path does not produce the expected signal, treat the coverage as unverified, preserve the test evidence, and route the gap through the appropriate remediation or risk process.

## Completion evidence

Scope, owner, source version, telemetry inspected, tests performed, findings, exceptions, remediation links, reviewer, and next trigger.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1608.005: https://attack.mitre.org/techniques/T1608/005
- Reviewed: 2026-10-27
