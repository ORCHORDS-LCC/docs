# Evil Twin Technique Operationalization Review

## Reference

- Technique: **T1557.004 — Evil Twin**

Adversaries may host seemingly genuine Wi-Fi access points to deceive users into connecting to malicious networks as a way of supporting follow-on behaviors such as Network Sniffing, Transmitted Data Manipulation, or Input Capture. By using a Service Set Identifier (SSID) of a legitimate Wi-Fi network, fraudulent Wi-Fi access points may trick devices or users into connecting to malicious Wi-Fi networks. Adversaries may provide a stronger signal strength or block access to Wi-Fi access points to coerce or entice victim devices into connecting to malicious networks. A Wi-Fi Pineapple – a network security auditing and penetration testing tool – may be deployed in Evil Twin attacks for ease of use and broader range. Custom certificates may be used in an attempt to intercept HTTPS traffic. Similarly, adversaries may also listen for client devices sending probe requests for known or previously connected networks (Preferred Network Lists or PNLs). When a malicious access point receives a probe request, adversaries can respond with the same SSID to imitate the trusted, known network. Victim devices are led to believe the responding access point is from their PNL and initiate a connection to the fraudulent network. Upon logging into the malicious Wi-Fi access point, a user may be directed to a fake login page or captive portal webpage to capture the victim’s credentials. Once a user is logged into the fraudulent Wi-Fi network, the adversary may able to monitor network activity, manipulate data, or steal additional credentials. Locations with high concentrations of public Wi-Fi access, such as airports, coffee shops, or libraries, may be targets for adversaries to set up illegitimate Wi-Fi access points.

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
- T1557.004: https://attack.mitre.org/techniques/T1557/004
- Reviewed: 2026-10-27
