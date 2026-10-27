# Upload Malware Technique Response Playbook

## Target technique

**T1608.001 — Upload Malware**

- Tactics: resource-development
- Platforms: PRE

Adversaries may upload malware to third-party or adversary controlled infrastructure to make it accessible during targeting. Malicious software can include payloads, droppers, post-compromise tools, backdoors, and a variety of other malicious content. Adversaries may upload malware to support their operations, such as making a payload available to a victim network to enable Ingress Tool Transfer by placing it on an Internet accessible web server. Malware may be placed on infrastructure that was previously purchased/rented by the adversary (Acquire Infrastructure) or was otherwise compromised by them (Compromise Infrastructure). Malware can also be staged on web services, such as GitHub or Pastebin; hosted on the InterPlanetary File System (IPFS), where decentralized content storage makes the removal of malicious files difficult; or saved on the blockchain as smart contracts, which are resilient against takedowns that would affect traditional infrastructure. Adversaries may upload backdoored files, such as software packages, application binaries, virtual machine images, or container images, to third-party software stores, package libraries, extension marketplaces, or repositories (ex: GitHub, CNET, AWS Community AMIs, Docker Hub, PyPi, NPM). By chance encounter, victims may directly download/install these backdoored files via User Execution. Masquerading, including typosquatting legitimate software, may increase the chance of users mistakenly executing these files.

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
- T1608.001: https://attack.mitre.org/techniques/T1608/001
- Reviewed: 2026-10-27
