# Collect Data as Provided by Users Attack Pattern Assurance Profile

## Reference

- Attack pattern: **569 — Collect Data as Provided by Users**
- Status: Draft

## Pattern description

An attacker leverages a tool, device, or program to obtain specific information as provided by a user of the target system. This information is often needed by the attacker to launch a follow-on attack. This attack is different than Social Engineering as the adversary is not tricking or deceiving the user. Instead the adversary is putting a mechanism in place that captures the information that a user legitimately enters into a system. Deploying a keylogger, performing a UAC prompt, or wrapping the Windows default credential provider are all examples of such interactions.

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
- 569: https://capec.mitre.org/data/definitions/569.html
- Reviewed: 2026-10-27
