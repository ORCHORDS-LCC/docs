# Signing Malicious Code Attack Pattern Assurance Profile

## Reference

- Attack pattern: **206 — Signing Malicious Code**
- Status: Draft

## Pattern description

The adversary extracts credentials used for code signing from a production environment and then uses these credentials to sign malicious content with the developer's key. Many developers use signing keys to sign code or hashes of code. When users or applications verify the signatures are accurate they are led to believe that the code came from the owner of the signing key and that the code has not been modified since the signature was applied. If the adversary has extracted the signing credentials then they can use those credentials to sign their own code bundles. Users or tools that verify the signatures attached to the code will likely assume the code came from the legitimate developer and install or run the code, effectively allowing the adversary to execute arbitrary code on the victim's computer. This differs from CAPEC-673, because the adversary is performing the code signing.

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
- 206: https://capec.mitre.org/data/definitions/206.html
- Reviewed: 2026-10-27
