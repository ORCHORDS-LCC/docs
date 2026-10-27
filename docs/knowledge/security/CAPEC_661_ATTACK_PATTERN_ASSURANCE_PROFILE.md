# Root/Jailbreak Detection Evasion via Debugging Attack Pattern Assurance Profile

## Reference

- Attack pattern: **661 — Root/Jailbreak Detection Evasion via Debugging**
- Status: Stable

## Pattern description

An adversary inserts a debugger into the program entry point of a mobile application to modify the application binary, with the goal of evading Root/Jailbreak detection. Mobile device users often Root/Jailbreak their devices in order to gain administrative control over the mobile operating system and/or to install third-party mobile applications that are not provided by authorized application stores (e.g. Google Play Store and Apple App Store). Rooting/Jailbreaking a mobile device also provides users with access to system debuggers and disassemblers, which can be leveraged to exploit applications by dumping the application's memory at runtime in order to remove or bypass signature verification methods. This further allows the adversary to evade Root/Jailbreak detection mechanisms, which can result in execution of administrative commands, obtaining confidential data, impersonating legitimate users of the application, and more.

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
- 661: https://capec.mitre.org/data/definitions/661.html
- Reviewed: 2026-10-27
