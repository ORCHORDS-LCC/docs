---
title: "OWASP Top 10 for LLM Applications 2026 Knowledge Index"
owner: "AI Security"
status: "approved"
classification: "public"
last-reviewed: "2026-11-24"
review-cycle: "180 days"
next-review: "2027-05-23"
---

# OWASP Top 10 for LLM Applications 2026 Knowledge Index

## Purpose

This index maps the published OWASP Top 10 for LLM Applications 2026 categories to reusable ORCHORDS knowledge cards. It is a navigation aid for design reviews, threat models, and gap assessments. It is not an OWASP publication and does not imply certification.

The 2026 edition introduces updated rankings and new categories such as Hidden Context Exposure and Vector and Embedding Weaknesses. Use the primary source for the full descriptions, attack scenarios, and mitigations.

## Risk map

| Risk | Practice focus | Representative knowledge cards |
| --- | --- | --- |
| LLM01:2026 Prompt Injection | Untrusted input changes model behavior or instruction priority. | [Prompt Injection Defense Strategies](ai-ml/prompt-injection-defense-strategies.md) · [LLM Prompt Injection Trust Boundaries](../security/engineering/llm-prompt-injection-trust-boundaries.md) |
| LLM02:2026 Sensitive Information Disclosure | Model output or application behavior reveals protected data. | [Agent Prompt Leakage Defense](agents/AGENT_PROMPT_LEAKAGE_DEFENSE.md) · [AI Gateway PII Scrubbing](ai-ml/ai-gateway-pii-scrubbing-request-response.md) |
| LLM03:2026 Excessive Agency | Model-driven actions exceed the authority the application intended to grant. | [Agent Tool Authorization and Least Privilege](agents/TOOL_AUTHORIZATION_LEAST_PRIVILEGE.md) · [Agent Guardrails 2026](../security/engineering/agent-guardrails-2026.md) |
| LLM04:2026 Supply Chain | Models, dependencies, tools, or distribution paths are compromised. | [Dependency Supply Chain Security for npm](../security/engineering/dependency-supply-chain-security-npm.md) · [AI Supply Chain Attacks 2026](../lessons/articles/ai-supply-chain-attacks-2026.md) |
| LLM05:2026 Data and Model Poisoning | Training, fine-tuning, retrieval, or context data is manipulated. | [LLM Context Poisoning Detection](ai-ml/llm-context-poisoning-detection-workers.md) · [Agent Memory Poisoning Detection](agents/AGENT_MEMORY_POISONING_DETECTION.md) |
| LLM06:2026 Unbounded Consumption | Model usage drives uncontrolled cost, latency, or resource exhaustion. | [LLM Cost Optimization](ai-ml/llm-cost-optimization.md) · [LLM Rate Limit Handling](ai-ml/llm-rate-limit-handling.md) |
| LLM07:2026 Misinformation | Generated claims are presented or propagated without adequate validation. | [Election Misinformation Detection](../reference/issues/election-misinformation-detection-workers-ai.md) · [Misinformation Labeling Pipeline](../reference/issues/misinformation-labeling-pipeline-ugc.md) |
| LLM08:2026 Hidden Context Exposure | Hidden system instructions or operational context are extracted, inferred, or reconstructed. Secrets and authorization decisions must not depend on hidden context staying secret. | [Multi-Turn Context Integrity](agents/AGENT_MULTI_TURN_CONTEXT_INTEGRITY.md) · [LLM Context Window Management](ai-ml/llm-context-window-management.md) |
| LLM09:2026 Vector and Embedding Weaknesses | Similarity search and embedding stores leak, poison, jam, or expose data across trust boundaries. | [Vectorize Multi-Tenant Namespace Partitioning](ai-ml/vectorize-multi-tenant-namespace-partitioning.md) · [Embedding Index Provenance](agents/OWASP_ASI06_EMBEDDING_INDEX_PROVENANCE.md) |
| LLM10:2026 Improper Output Handling | Downstream systems trust model output without sufficient validation or sanitization. | [LLM Output Validation](ai-ml/llm-output-validation.md) · [Structured Output with Constrained Decoding](ai-ml/llm-structured-output-constrained-decoding.md) |

## How to use this index

1. Identify which LLM behaviors and supporting systems are in scope for the review.
2. Select the relevant risk rows and open the linked cards before writing findings.
3. Keep LLM-specific risks separate from agentic risks; use the [Agentic Applications 2026 index](agents/OWASP_TOP_10_FOR_AGENTIC_APPLICATIONS_2026_INDEX.md) when autonomy, delegation, memory, or inter-agent communication dominates the risk.
4. Record controls, gaps, and residual risk in the system's normal risk register.
5. Recheck the primary source when the list or a mapped control changes.

## Scope note

The practice-focus column summarizes the operational concern addressed by the linked cards. It is not a verbatim reproduction of OWASP risk definitions. For precise wording, attack scenarios, and mitigations, use the official publication.

## Sources

- OWASP GenAI Security Project — Top 10 for LLM Applications 2026: https://genai.owasp.org/top-10-for-llm-applications-2026/
- OWASP GenAI Security Project — OWASP GenAI LLM Top 10 2026 resource page: https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/
- OWASP GenAI Security Project — 2026 LLM Top 10 announcement: https://genai.owasp.org/2026/09/01/owasp-genai-security-project-unveils-2026-top-10-for-llm-applications-new-agent-control-standard-and-sponsors-as-community-tops-30000-members/
- OWASP GenAI Security Project — LLM08:2026 Hidden Context Exposure: https://genai.owasp.org/llm2026/llm082026-hidden-context-exposure/
- OWASP GenAI Security Project — LLM09:2026 Vector and Embedding Weaknesses: https://genai.owasp.org/llm2026/llm092026-vector-and-embedding-weaknesses/
