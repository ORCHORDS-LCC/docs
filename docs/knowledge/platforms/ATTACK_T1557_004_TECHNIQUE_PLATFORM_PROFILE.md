# Evil Twin Technique Platform Profile

## Reference

- Technique: **T1557.004 — Evil Twin**
- Platforms named in the source: Network Devices

Adversaries may host seemingly genuine Wi-Fi access points to deceive users into connecting to malicious networks as a way of supporting follow-on behaviors such as Network Sniffing, Transmitted Data Manipulation, or Input Capture. By using a Service Set Identifier (SSID) of a legitimate Wi-Fi network, fraudulent Wi-Fi access points may trick devices or users into connecting to malicious Wi-Fi networks. Adversaries may provide a stronger signal strength or block access to Wi-Fi access points to coerce or entice victim devices into connecting to malicious networks. A Wi-Fi Pineapple – a network security auditing and penetration testing tool – may be deployed in Evil Twin attacks for ease of use and broader range. Custom certificates may be used in an attempt to intercept HTTPS traffic. Similarly, adversaries may also listen for client devices sending probe requests for known or previously connected networks (Preferred Network Lists or PNLs). When a malicious access point receives a probe request, adversaries can respond with the same SSID to imitate the trusted, known network. Victim devices are led to believe the responding access point is from their PNL and initiate a connection to the fraudulent network. Upon logging into the malicious Wi-Fi access point, a user may be directed to a fake login page or captive portal webpage to capture the victim’s credentials. Once a user is logged into the fraudulent Wi-Fi network, the adversary may able to monitor network activity, manipulate data, or steal additional credentials. Locations with high concentrations of public Wi-Fi access, such as airports, coffee shops, or libraries, may be targets for adversaries to set up illegitimate Wi-Fi access points.

## Platform profile

1. Record the platforms in scope and the versions actually deployed.
2. Compare the deployed platform surface against the platforms the source names.
3. Record where the platform provides a native control for the technique, and where it does not.
4. Record the configuration evidence for the native control, where one exists.
5. Record the gap where the platform provides no native control, and the compensating detection.
6. Record the platform version, because platform behaviour changes between versions.

## Evidence

- the platform and version inventory for the scoped estate;
- the configuration export or screenshot for the native control;
- the detection evidence where the platform provides none.

## Limitations

A technique entry describes a class of abuse across platforms. The platform-specific exposure is a property of the deployment, established only by inventory and configuration evidence.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1557.004: https://attack.mitre.org/techniques/T1557/004
- Reviewed: 2026-10-27
