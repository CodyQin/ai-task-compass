# Model selection: pass business acceptance, then compare total cost

[Overview](../README.md) · [中文](model-selection.zh-CN.md) · [Evaluation CSV](../templates/model-evaluation.csv)

Separate chat product, underlying model, orchestration platform and deployment. A quadrant does not prescribe a model; API and chat features may differ. Filter for access, region, data policy, deployment, budget and maintenance first.

| Task | Candidate capability | Check |
|---|---|---|
| Known-rule calculations | Existing spreadsheet/code; optional AI-assisted construction | Numeric/boundary correctness; recurring model call may be unnecessary |
| Extraction/classification | Affordable general text model with language/format support | Omissions, multi-labels, nulls, evidence, schema |
| Images/PDF/tables | Document parsing or multimodal capability | OCR, cross-page tables, units, missing fields |
| Retrieval QA | Retrieval/access/version layer plus grounded answering | Retrieval quality separately from answer quality; conflict/no-answer behavior |
| Adaptive analysis/tools | Reasoning, valid tool use, budgets and recovery | Task completion, wrong actions, iterations, time, intervention |

Find current candidates in official [Qwen / Model Studio](https://www.alibabacloud.com/help/en/model-studio/models), [DeepSeek](https://api-docs.deepseek.com/) and [Claude](https://platform.claude.com/docs/en/about-claude/models/overview) catalogs. These are entry points, not exhaustive rankings or performance recommendations. Check live versions, terms, regional availability and prices before adoption. Reference date: 2026-11-07. Existing chat tools may suffice; no new API purchase is required.

## Small comparison protocol

Use authorized representative cases, including missing/conflicting data and important exceptions. Define reference answers or acceptance rubrics before testing. Compare at most two feasible candidates with the same task, data, tool permissions and budget; record versions, parameters, date and prompt version. Repeat as needed to see variability. Keep development examples separate from held-out checks. Small samples are exploratory, not population accuracy claims.

Log completion, severe omissions, unsupported facts, schema/tool errors, acceptance, elapsed time, input/output tokens, retries, human review minutes and actual charges. Pass the quality gate before cost ranking.

Full cost per accepted delivery = all batch costs (including failed/retried model calls, tools and attributable human review) / accepted deliveries. With zero accepted deliveries, do not report a favorable average. Report failures and severity too. Monetized staff time is a resource estimate, not automatically cash expense; avoid double-counting in financial ROI.

Escalate models, retrieval or process complexity only when a simpler route fails acceptance. Routing needs real error detection and fallback, not uncalibrated self-reported confidence.

Reference: [Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents). This project's protocol and CSV are practical adaptations, not model certifications.
