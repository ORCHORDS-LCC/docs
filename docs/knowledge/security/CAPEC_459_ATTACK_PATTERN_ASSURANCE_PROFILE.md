# Creating a Rogue Certification Authority Certificate Attack Pattern Assurance Profile

## Reference

- Attack pattern: **459 — Creating a Rogue Certification Authority Certificate**
- Status: Draft

## Pattern description

An adversary exploits a weakness resulting from using a hashing algorithm with weak collision resistance to generate certificate signing requests (CSR) that contain collision blocks in their "to be signed" parts. The adversary submits one CSR to be signed by a trusted certificate authority then uses the signed blob to make a second certificate appear signed by said certificate authority. Due to the hash collision, both certificates, though different, hash to the same value and so the signed blob works just as well in the second certificate. The net effect is that the adversary's second X.509 certificate, which the Certification Authority has never seen, is now signed and validated by that Certification Authority.

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
- 459: https://capec.mitre.org/data/definitions/459.html
- Reviewed: 2026-10-27
