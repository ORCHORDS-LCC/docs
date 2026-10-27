# XSS Targeting Non-Script Elements Attack Pattern Assurance Profile

## Reference

- Attack pattern: **18 — XSS Targeting Non-Script Elements**
- Status: Draft

## Pattern description

This attack is a form of Cross-Site Scripting (XSS) where malicious scripts are embedded in elements that are not expected to host scripts such as image tags (<img>), comments in XML documents (< !-CDATA->), etc. These tags may not be subject to the same input validation, output validation, and other content filtering and checking routines, so this can create an opportunity for an adversary to tunnel through the application's elements and launch a XSS attack through other elements. As with all remote attacks, it is important to differentiate the ability to launch an attack (such as probing an internal network for unpatched servers) and the ability of the remote adversary to collect and interpret the output of said attack.

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
- 18: https://capec.mitre.org/data/definitions/18.html
- Reviewed: 2026-10-27
