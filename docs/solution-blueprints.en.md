# Four starting blueprints: input to acceptance

[Overview](../README.md) · [中文](solution-blueprints.zh-CN.md)

These are **synthetic design blueprints**, not deployed customer cases, importable workflows or demonstrated returns. Platforms overlap; no quadrant mandates a product.

| Route | Inputs and flow | Start / conditional upgrade | Acceptance |
|---|---|---|---|
| A: Rule-based reports | Agreed table schema/rules → validate → clean/merge/calculate → exceptions → review | Spreadsheet/script; [n8n](https://docs.n8n.io/) only for justified recurring integrations | Totals, duplicates, units, traced exceptions; no silent failure |
| B: Feedback reports | Authorized text/labels → model extracts evidence/nulls → review → deterministic counting → draft | Existing chat + spreadsheet; [Dify](https://docs.dify.ai/en/home) for application workflows, or n8n if system handoffs dominate | Omissions, unsupported facts, multi-label counting, review time |
| C: Knowledge QA | Authorized/versioned sources → access control → allowed retrieval → cited response → conflict/no-answer escalation | Small-file assisted search; Dify retrieval app when repeated shared use justifies it | Retrieval vs answer quality separately, permissions, stale/conflicting sources |
| D: Adaptive investigation | Clear target/read-only tools → hypothesis → query/calculate → evidence check → next action → budget/stop → sourced conclusion | Human-guided tools; [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview) for justified state/recovery/intervention, or Dify agent node for a visual app | Supported conclusions, correct calls, budget limits, stopping/intervention |

A may fit Q1. B may combine Q2 understanding and Q1 counting. C can start at Q2, but source conflicts need an authority. D can fit Q3 with available data; unclear goals require Q4 clarification first. Adaptive work need not use an LLM agent.

Official capability entry points checked 2026-11-07. Coze, FastGPT, Make and Zapier may fit existing environments; no exhaustive comparison is claimed. Recommend at most two explained routes with account, data, deployment, maintenance, price and license prerequisites. This repository's MIT license does not license external tools.
