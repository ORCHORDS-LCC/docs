# Compromise Software Dependencies and Development Tools Technique Response Playbook

## Target technique

**T1195.001 — Compromise Software Dependencies and Development Tools**

- Tactics: initial-access
- Platforms: Linux, macOS, Windows

Adversaries may manipulate software dependencies and development tools prior to receipt by a final consumer for the purpose of data or system compromise. Applications often depend on external software to function properly. Popular open source projects that are used as dependencies in many applications, such as pip and NPM packages, may be targeted as a means to add malicious code to users of the dependency. This may also include abandoned packages, which in some cases could be re-registered by threat actors after being removed by adversaries. Adversaries may also employ "typosquatting" or name-confusion by choosing names similar to existing popular libraries or packages in order to deceive a user. Additionally, CI/CD pipeline components, such as GitHub Actions, may be targeted in order to gain access to the building, testing, and deployment cycles of an application. By adding malicious code into a GitHub action, a threat actor may be able to collect runtime credentials (e.g., via Proc Filesystem) or insert further malicious components into the build pipelines for a second-order supply chain compromise. As GitHub Actions are often dependent on other GitHub Actions, threat actors may be able to infect a large number of repositories via the compromise of a single Action. Adversaries may also target the configuration and instruction files consumed by integrated development environments and AI coding agents. Project files such as tasks.json may execute commands when a developer opens or builds a project, while agent skill files (SKILL.md) supply an agent with instructions and resources that it loads on demand and runs with the permissions of the agent process. To encourage downloads, adversaries may publish these files under benign-appearing or typo-squatted names, upload unmodified copies of the genuine skills first so the listings accumulate installs before the content behind them is weaponized, or may place the malicious instructions in a secondary document that the reviewed entry point references. Because these artifacts are natural language or configuration rather than executable code, they may pass registry screening and signature-based scanning. Targeting may be specific to a desired victim set or may be distributed to a broad set of consumers but only move on to additional tactics on specific victims.

## Preconditions

- the estate in scope is identified, with the systems the technique could apply to;
- an owner is accountable for detection and response;
- current telemetry and configuration can be inspected;
- the technique is applicable or requires an applicability decision.

## Procedure

1. Confirm the scope and owner.
2. Read the current technique description and the associated detection guidance.
3. Inventory the telemetry that would carry the technique's indicators.
4. Inspect whether the indicators are present in the environment.
5. Exercise the detection path and confirm it produces the expected signal.
6. Record gaps in detection coverage and assign remediation owners.
7. Record justified non-applicability or accepted detection gaps separately.
8. Set the next event-driven or periodic verification trigger.

## Failure handling

If the detection path does not produce the expected signal, treat the coverage as unverified, preserve the test evidence, and route the gap through the appropriate remediation or risk process.

## Completion evidence

Scope, owner, source version, telemetry inspected, tests performed, findings, exceptions, remediation links, reviewer, and next trigger.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1195.001: https://attack.mitre.org/techniques/T1195/001
- Reviewed: 2026-10-27
