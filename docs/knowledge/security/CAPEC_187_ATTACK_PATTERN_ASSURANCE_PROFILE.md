# Malicious Automated Software Update via Redirection Attack Pattern Assurance Profile

## Reference

- Attack pattern: **187 — Malicious Automated Software Update via Redirection**
- Status: Draft

## Pattern description

An attacker exploits two layers of weaknesses in server or client software for automated update mechanisms to undermine the integrity of the target code-base. The first weakness involves a failure to properly authenticate a server as a source of update or patch content. This type of weakness typically results from authentication mechanisms which can be defeated, allowing a hostile server to satisfy the criteria that establish a trust relationship. The second weakness is a systemic failure to validate the identity and integrity of code downloaded from a remote location, hence the inability to distinguish malicious code from a legitimate update.

## Assurance profile

1. Determine whether the attack pattern is in scope for the systems and data being protected, and record the reason.
2. Review the pattern's prerequisites: the access, position, or precondition it requires.
3. Identify the observable indicators the pattern would produce in logs, telemetry, or configuration.
4. Define the control that prevents the pattern and the control that would detect it.
5. Define the verification method and the evidence that would demonstrate either prevention or detection.
6. Record the residual risk where only detection, not prevention, can be achieved.

## Verification evidence

- a scope decision recording why the pattern is or is not applicable;
- the indicator list mapped to the telemetry that would carry it;
- the control mapping with the evidence that supports it;
- a test or exercise record for the detection path.

## Limitations

An attack-pattern entry describes a class of abuse. Applicability and exposure are properties of a system, established only by evidence.

## Source

- MITRE CAPEC catalog: https://capec.mitre.org/data/xml/capec_latest.xml
- 187: https://capec.mitre.org/data/definitions/187.html
- Reviewed: 2026-10-27
