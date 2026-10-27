# Steal Web Session Cookie Technique Operationalization Review

## Reference

- Technique: **T1539 — Steal Web Session Cookie**

An adversary may steal web application or service session cookies and use them to gain access to web applications or Internet services as an authenticated user without needing credentials. Web applications and services often use session cookies as an authentication token after a user has authenticated to a website. Cookies are often valid for an extended period of time, even if the web application is not actively used. Cookies can be found on disk, in the process memory of the browser, and in network traffic to remote systems. Additionally, other applications on the targets machine might store sensitive authentication cookies in memory (e.g. apps which authenticate to cloud services). Session cookies can be used to bypasses some multi-factor authentication protocols. There are several examples of malware targeting cookies from web browsers on the local system. Adversaries may also steal cookies by injecting malicious JavaScript content into websites or relying on User Execution by tricking victims into running malicious JavaScript in their browser. There are also open source frameworks such as `Evilginx2` and `Muraena` that can gather session cookies through a malicious proxy (e.g., Adversary-in-the-Middle) that can be set up by an adversary and used in phishing campaigns. After an adversary acquires a valid cookie, they can then perform a Web Session Cookie technique to login to the corresponding web application.

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
- T1539: https://attack.mitre.org/techniques/T1539
- Reviewed: 2026-10-27
