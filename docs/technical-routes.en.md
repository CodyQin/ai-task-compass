# Choose a technical route from the business problem

[首页 / Overview](../README.md) · [中文](technical-routes.zh-CN.md) · [English](technical-routes.en.md) · [交互路线导航 / Navigator](https://codyqin.github.io/ai-task-compass/solution-navigator.html)

A decision and learning map, not a technology ranking. Start small, combine routes only when useful, and allow no-AI outcomes. Official documentation has been reviewed; integrations and business outcomes are not claimed as tested.

RAG is an architectural approach; LangChain is a framework (including harness capabilities), LangGraph addresses orchestration, a harness surrounds the model loop, DeepSeek is a model-service candidate, and MCP is a connection standard. They overlap and compose; none is a mandatory layer in every project.

## Rules and ordinary automation

- **Problem：**Reports, fixed calculations, recurring handoffs
- **Use when：**Known rules and directly checkable outputs
- **Avoid / resolve first：**Clarify missing rules; add interpretation only where needed
- **Start / upgrade：**Existing spreadsheet/script; workflow only for justified integrations
- **Prerequisites：**Keys, units, exceptions and owner
- **Small learning exercise：**Check a small table with known answers
- **Acceptance：**Totals, exceptions, duplicates and rework
- **资料 / Resources：**[n8n](https://docs.n8n.io/)

## Prompts and structured outputs

- **Problem：**Feedback labeling, field extraction, drafts
- **Use when：**Stable output contract with variable text
- **Avoid / resolve first：**Do not guess missing facts, consequential decisions or arithmetic
- **Start / upgrade：**Existing chat plus schema; Dify for a justified repeatable app
- **Prerequisites：**Schema, nulls, evidence and review
- **Small learning exercise：**Extract fixed fields from authorized samples and review
- **Acceptance：**Omissions, unsupported facts, schema and edits
- **资料 / Resources：**[Dify](https://docs.dify.ai/en/home) · [DeepSeek](https://api-docs.deepseek.com/) · [Qwen / Model Studio](https://www.alibabacloud.com/help/en/model-studio/models)

## Document parsing and multimodal input

- **Problem：**Scans, images, tables, audio/video sources
- **Use when：**Needed information is in non-text formats
- **Avoid / resolve first：**Skip OCR when clean structured data already exists
- **Start / upgrade：**Parse into reviewable text/fields before business processing
- **Prerequisites：**Rights, formats, language, units and source location
- **Small learning exercise：**Check one difficult document against its source
- **Acceptance：**Recognition, table alignment, units and missing fields
- **资料 / Resources：**[LlamaIndex](https://developers.llamaindex.ai/python/framework/) · [Qwen / Model Studio](https://www.alibabacloud.com/help/en/model-studio/models)

## RAG and knowledge applications

- **Problem：**Repeated QA over policies or internal material
- **Use when：**Answers must use maintained authorized sources
- **Avoid / resolve first：**Resolve authority/missing facts; try simple file reading for small collections
- **Start / upgrade：**Small-file trial; Dify for apps or LlamaIndex for code-based retrieval
- **Prerequisites：**Owner, version, access, citations and no-answer behavior
- **Small learning exercise：**Test answerable, absent and conflicting questions; score retrieval and generation separately
- **Acceptance：**Evidence retrieval, citations, stale data and access violations
- **资料 / Resources：**[Dify](https://docs.dify.ai/en/home) · [LlamaIndex](https://developers.llamaindex.ai/python/framework/)

## Structured data and business analysis

- **Problem：**Metrics, database queries, operational investigation
- **Use when：**Defined metrics, authorized data and read-only access
- **Avoid / resolve first：**No undefined metrics or causal conclusions from correlation alone
- **Start / upgrade：**Spreadsheet/BI/manual query first; add restricted tools and explanation if useful
- **Prerequisites：**Definitions, keys, units, access, query bounds and review
- **Small learning exercise：**Check known queries before investigating anomalies
- **Acceptance：**Numbers, access, query cost and supported interpretation
- **资料 / Resources：**[Workflows and agents](https://www.anthropic.com/research/building-effective-agents) · [LangChain](https://docs.langchain.com/oss/python/langchain/overview)

## Cross-system workflows

- **Problem：**Triggers, approvals, notifications, batch processing
- **Use when：**Predefined steps/branches with worthwhile repetition
- **Avoid / resolve first：**Start smaller for one-off work or unclear access/recovery
- **Start / upgrade：**Existing automation first; n8n for handoffs, Dify for AI app flows
- **Prerequisites：**Interfaces, identity, idempotency, retries, alerts, maintenance
- **Small learning exercise：**Try one bounded path without production writes
- **Acceptance：**Duplicate execution, recovery, exceptions, intervention
- **资料 / Resources：**[n8n](https://docs.n8n.io/) · [Dify](https://docs.dify.ai/en/home)

## Tool use and MCP

- **Problem：**Access authorized systems and deterministic tools
- **Use when：**A real need for live tools with defined access
- **Avoid / resolve first：**MCP is not authorization, a security boundary or mandatory for every integration
- **Start / upgrade：**Start with one read-only tool; consider MCP for supported interoperability
- **Prerequisites：**Validation, least privilege, timeout, audit, approvals
- **Small learning exercise：**Test one restricted read tool and invalid-input failure
- **Acceptance：**Arguments, access, errors and blocked dangerous actions
- **资料 / Resources：**[MCP](https://modelcontextprotocol.io/docs/getting-started/intro) · [LangChain](https://docs.langchain.com/oss/python/langchain/overview) · [OWASP GenAI risks](https://genai.owasp.org/llm-top-10/)

## Adaptive agents

- **Problem：**Investigations and multi-step evidence-led tasks
- **Use when：**Checkable target with evidence-dependent next actions
- **Avoid / resolve first：**Avoid unnecessary autonomy for fixed rules or undetectable failures
- **Start / upgrade：**Human-guided tools first; LangChain or Dify agents when justified
- **Prerequisites：**Tools, acceptance, iteration/cost limits, logs, intervention
- **Small learning exercise：**Try one goal with restricted tools and an action/evidence trace
- **Acceptance：**Acceptance, wrong actions, budget, evidence, consistency
- **资料 / Resources：**[LangChain](https://docs.langchain.com/oss/python/langchain/overview) · [Dify](https://docs.dify.ai/en/home) · [Workflows and agents](https://www.anthropic.com/research/building-effective-agents)

## Stateful orchestration

- **Problem：**Pause/resume, human approvals, stateful branching
- **Use when：**Concrete state, interruption or recovery requirements
- **Avoid / resolve first：**Skip persistent orchestration for a simple one-off chat
- **Start / upgrade：**Define state/nodes; compare LangGraph or simpler platform flows
- **Prerequisites：**Persistence, checkpoints, concurrency, versioning, operations
- **Small learning exercise：**Interrupt and resume a sample; verify no duplicate actions
- **Acceptance：**State loss, recovery, duplicated effects, approvals
- **资料 / Resources：**[LangGraph](https://docs.langchain.com/oss/python/langgraph/overview)

## Harness, context and memory

- **Problem：**Long tasks, session continuity, tool loops, progress/context
- **Use when：**Observed continuity, context growth or progress failures
- **Avoid / resolve first：**Do not build a separate harness if existing tooling suffices
- **Start / upgrade：**Use existing runtime; add state, context policy, checks, budgets and intervention
- **Prerequisites：**Goals, progress, context policy, access, recovery
- **Small learning exercise：**Stop after one segment and check documented resumption
- **Acceptance：**Goal loss, false completion, repeated actions, context cost
- **资料 / Resources：**[Long-running harness design](https://www.anthropic.com/research/effective-harnesses-for-long-running-agents) · [LangChain](https://docs.langchain.com/oss/python/langchain/overview) · [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview)

## Model customization and fine-tuning

- **Problem：**Stable task still fails after simpler improvements
- **Use when：**Authorized training data, independent eval and clear target
- **Avoid / resolve first：**Not a substitute for live knowledge, missing data or a real use case
- **Start / upgrade：**Diagnose failure first; consider PEFT with held-out checks only if justified
- **Prerequisites：**Quality, rights, compute, versions, regressions, upkeep
- **Small learning exercise：**Start with error/data analysis and a bounded experiment plan
- **Acceptance：**Held-out performance, generalization, cost, regressions
- **资料 / Resources：**[PEFT](https://huggingface.co/docs/peft/index) · [Agent evaluations](https://www.anthropic.com/research/demystifying-evals-for-ai-agents)

## Delivery, observability and maintenance

- **Problem：**Recurring shared use, incident diagnosis, updates/rollback
- **Use when：**Moving from demo to service with ownership and traceability
- **Avoid / resolve first：**Do not declare production readiness without operational controls
- **Start / upgrade：**Start with logs/review; consider observability tooling as scale warrants
- **Prerequisites：**Retention, redaction, versions, budgets, alerts, rollback
- **Small learning exercise：**Replay one failure and version change; check diagnosis/recovery
- **Acceptance：**Regressions, latency, failures, full cost, adoption, incidents
- **资料 / Resources：**[Langfuse](https://langfuse.com/docs) · [OWASP GenAI risks](https://genai.owasp.org/llm-top-10/) · [Agent evaluations](https://www.anthropic.com/research/demystifying-evals-for-ai-agents)

Reference review: 2026-11-07. Recheck region, fees, licensing and deployment conditions. Guidance does not mean an installed/importable implementation. Third-party licenses are independent of this repository MIT license.
