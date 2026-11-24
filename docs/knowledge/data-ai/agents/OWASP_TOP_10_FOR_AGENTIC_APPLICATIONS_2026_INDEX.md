---
title: "OWASP Top 10 for Agentic Applications 2026 Knowledge Index"
owner: "AI Security"
status: "approved"
classification: "public"
last-reviewed: "2026-11-24"
review-cycle: "180 days"
next-review: "2027-05-23"
---

# OWASP Top 10 for Agentic Applications 2026 Knowledge Index

## Purpose

This index maps the published OWASP Top 10 for Agentic Applications 2026 risk categories to reusable ORCHORDS knowledge cards. It is a navigation aid for design reviews and threat models. It is not a certification, an OWASP publication, or a replacement for the referenced guide.

The OWASP GenAI Security Project published the 2026 agentic list on 2025-12-09 after community review. Use the primary source for the full risk descriptions, attack scenarios, and mitigations.

## Risk map

| Risk | Practice focus | Representative knowledge cards |
| --- | --- | --- |
| ASI01 Agent Goal Hijack | Untrusted content changes an agent's objective or instruction hierarchy. | [Tool Output Instruction Isolation](OWASP_ASI01_TOOL_OUTPUT_INSTRUCTION_ISOLATION.md) · [Goal Checkpoint Revalidation](OWASP_ASI01_GOAL_CHECKPOINT_REVALIDATION.md) |
| ASI02 Tool Misuse and Exploitation | Legitimate tool capabilities are used outside their intended scope. | [Tool Capability Allowlisting](OWASP_ASI02_TOOL_CAPABILITY_ALLOWLISTING.md) · [Two-Phase Destructive Confirmation](OWASP_ASI02_DESTRUCTIVE_ACTION_TWO_PHASE_CONFIRMATION.md) |
| ASI03 Identity and Privilege Abuse | Dynamic trust and delegation are abused to exceed the granted authority. | [Non-Transitive Delegation](OWASP_ASI03_NON_TRANSITIVE_DELEGATION.md) · [Short-Lived Credentials](OWASP_ASI03_SHORT_LIVED_CREDENTIALS.md) |
| ASI04 Agentic Supply Chain Vulnerabilities | Agents, tools, plugins, or their dependencies are compromised before use. | [Dependency Digest Pinning](OWASP_ASI04_DEPENDENCY_DIGEST_PINNING.md) · [Compromised Tool Revocation](OWASP_ASI04_COMPROMISED_TOOL_REVOCATION.md) |
| ASI05 Unexpected Code Execution (RCE) | Generated or invoked code executes beyond the intended boundary. | [Sandbox Execution](OWASP_ASI05_SANDBOXED_EXECUTION.md) · [Deny-by-Default Network Egress](OWASP_ASI05_NETWORK_EGRESS_DENY_BY_DEFAULT.md) |
| ASI06 Memory & Context Poisoning | Stored or retrieved context is altered to influence later decisions. | [Memory Write Authorization](OWASP_ASI06_MEMORY_WRITE_AUTHORIZATION.md) · [Poisoned Memory Quarantine](OWASP_ASI06_POISONED_MEMORY_QUARANTINE.md) |
| ASI07 Insecure Inter-Agent Communication | Multi-agent messages are spoofed, read, replayed, or trusted without proof. | [Mutual Authentication Between Agents](OWASP_ASI07_MUTUAL_AUTHENTICATION_BETWEEN_AGENTS.md) · [Replay Protection](OWASP_ASI07_REPLAY_PROTECTION.md) |
| ASI08 Cascading Failures | One agent's failure propagates through dependent agents or tools. | [Cascade Simulation Testing](OWASP_ASI08_CASCADE_SIMULATION_TESTING.md) · [Fanout Limits](OWASP_ASI08_FANOUT_LIMITS.md) |
| ASI09 Human-Agent Trust Exploitation | Approval interfaces or agent output cause people to authorize unsafe actions. | [Approval Context Completeness](OWASP_ASI09_APPROVAL_CONTEXT_COMPLETENESS.md) · [Human Override Auditing](OWASP_ASI09_HUMAN_OVERRIDE_AUDITING.md) |
| ASI10 Rogue Agents | An agent acts outside its recorded policy or expected behavior baseline. | [Kill Switch Independence](OWASP_ASI10_KILL_SWITCH_INDEPENDENCE.md) · [Plan/Action Divergence Detection](OWASP_ASI10_PLAN_ACTION_DIVERGENCE_DETECTION.md) |

## How to use this index

1. Bound the review to the agent's tools, identities, memory, messages, and human approval points.
2. Select the relevant ASI rows and link the corresponding knowledge cards in the design record.
3. Record which controls are present, which are planned, and which are explicitly out of scope.
4. Record residual risk in the system's normal risk register; do not infer assurance from the existence of a card.
5. Recheck the primary source when the list is revised or when a mapped control changes.

## Scope note

The practice-focus column summarizes the operational concern addressed by the linked cards. It is not a verbatim reproduction of OWASP risk definitions. For precise wording, attack scenarios, and mitigations, use the official publication.

## Sources

- OWASP GenAI Security Project — Top 10 for Agentic Applications 2026: https://genai.owasp.org/top-10-for-agentic-applications-2026/
- OWASP GenAI Security Project — Top 10 for Agentic Applications for 2026 resource page: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- OWASP GenAI Security Project — Release announcement: https://genai.owasp.org/2025/12/09/owasp-genai-security-project-releases-top-10-risks-and-mitigations-for-agentic-ai-security/
