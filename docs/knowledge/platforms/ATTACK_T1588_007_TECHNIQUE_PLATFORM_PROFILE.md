# Artificial Intelligence Technique Platform Profile

## Reference

- Technique: **T1588.007 — Artificial Intelligence**
- Platforms named in the source: PRE

Adversaries may obtain access to generative artificial intelligence (AI) tools, such as large language models (LLMs), to aid various techniques during targeting. These tools may be used to inform, bolster, and enable a variety of malicious tasks, including creating scripts, assisting social engineering, developing payloads, and to Query Public AI Services in support of Reconnaissance. For example, by utilizing a publicly available LLM an adversary is essentially outsourcing or automating certain tasks to the tool. Using AI, the adversary may draft and Generate Content in a variety of written languages to be used in Phishing/Phishing for Information campaigns. The same publicly available tool may further enable vulnerability or other offensive research supporting Develop Capabilities. AI tools may also automate technical tasks by generating, refining, or otherwise enhancing (e.g., Obfuscated Files or Information) malicious scripts and payloads. Finally, AI-generated text, images, audio, and video may be used for fraud, Impersonation, and other malicious activities.

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
- T1588.007: https://attack.mitre.org/techniques/T1588/007
- Reviewed: 2026-10-27
