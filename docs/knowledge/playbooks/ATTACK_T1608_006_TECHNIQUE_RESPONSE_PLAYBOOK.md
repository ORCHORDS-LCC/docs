# SEO Poisoning Technique Response Playbook

## Target technique

**T1608.006 — SEO Poisoning**

- Tactics: resource-development
- Platforms: PRE

Adversaries may poison mechanisms that influence search engine optimization (SEO) to further lure staged capabilities towards potential victims. Search engines typically display results to users based on purchased ads as well as the site’s ranking/score/reputation calculated by their web crawlers and algorithms. To help facilitate Drive-by Compromise, adversaries may stage content that explicitly manipulates SEO rankings in order to promote sites hosting their malicious payloads (such as Drive-by Target) within search engines. Poisoning SEO rankings may involve various tricks, such as stuffing keywords (including in the form of hidden text) into compromised sites. These keywords could be related to the interests/browsing habits of the intended victim(s) as well as more broad, seasonably popular topics (e.g. elections, trending news). In addition to internet search engines (such as Google), adversaries may also aim to manipulate specific in-site searches for developer platforms (such as GitHub) to deceive users towards Supply Chain Compromise lures. In-site searches will rank search results according to their own algorithms and metrics such as popularity which may be targeted and gamed by malicious actors. Adversaries may also purchase or plant incoming links to staged capabilities in order to boost the site’s calculated relevance and reputation. SEO poisoning may also be combined with evasive redirects and other cloaking mechanisms (such as measuring mouse movements or serving content based on browser user agents, user language/localization settings, or HTTP headers) in order to feed SEO inputs while avoiding scrutiny from defenders.

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
- T1608.006: https://attack.mitre.org/techniques/T1608/006
- Reviewed: 2026-10-27
