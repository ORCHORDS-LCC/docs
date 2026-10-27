# Drive-by Target Technique Operationalization Review

## Reference

- Technique: **T1608.004 — Drive-by Target**

Adversaries may prepare an operational environment to infect systems that visit a website over the normal course of browsing. Endpoint systems may be compromised through browsing to adversary controlled sites, as in Drive-by Compromise. In such cases, the user's web browser is typically targeted for exploitation (often not requiring any extra user interaction once landing on the site), but adversaries may also set up websites for non-exploitation behavior such as Application Access Token. Prior to Drive-by Compromise, adversaries must stage resources needed to deliver that exploit to users who browse to an adversary controlled site. Drive-by content can be staged on adversary controlled infrastructure that has been acquired (Acquire Infrastructure) or previously compromised (Compromise Infrastructure). Adversaries may upload or inject malicious web content, such as JavaScript, into websites. This may be done in a number of ways, including: * Inserting malicious scripts into web pages or other user controllable web content such as forum posts * Modifying script files served to websites from publicly writeable cloud storage buckets * Crafting malicious web advertisements and purchasing ad space on a website through legitimate ad providers (i.e., Malvertising) In addition to staging content to exploit a user's web browser, adversaries may also stage scripting content to profile the user's browser (as in Gather Victim Host Information) to ensure it is vulnerable prior to attempting exploitation. Websites compromised by an adversary and used to stage a drive-by may be ones visited by a specific community, such as government, a particular industry, or region, where the goal is to compromise a specific user or set of users based on a shared interest. This kind of targeted campaign is referred to a strategic web compromise or watering hole attack. Adversaries may purchase domains similar to legitimate domains (ex: homoglyphs, typosquatting, different top-level domain, etc.) during acquisition of infrastructure (Domains) to help facilitate Drive-by Compromise.

## Operationalization review

1. Record the operational scope: which services, environments, and data the technique could affect.
2. Record the runbook that would be executed, and its owner.
3. Record the telemetry the runbook depends on, and whether it is retained long enough to investigate.
4. Record the detection that would surface the technique before or after it has an effect.
5. Record the recovery path, and the evidence that recovery has been rehearsed.
6. Record the residual operational risk where the runbook depends on a manual step.

## Review evidence

- the runbook and its owner;
- the telemetry retention and coverage record;
- the detection mapping;
- the exercise or rehearsal record.

## Limitations

An operationalization review describes the runbook and the evidence around it. It does not claim the technique has been prevented or detected in a live environment.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1608.004: https://attack.mitre.org/techniques/T1608/004
- Reviewed: 2026-10-27
