---
name: ai-solution-design
description: Turn a confirmed workflow problem into a bounded AI or non-AI solution blueprint with task-level quadrants, human/tool roles, implementation prerequisites and acceptance criteria.
---


# Solution design · AI 方案设计

Respond in the user's language. Reuse the problem brief; do not re-interview known facts. If the desired outcome or source authority is unclear, ask the key missing question before prescribing a stack.

Split input → action → check → output into useful steps. Assess information needs (directly rule-processable, variable expression, missing facts, conflicting evidence) and whether next steps/branches can be specified beforehand. Many branches/loops/retries do not imply adaptive control. Classify only where justified: Q1 known information/fixed path; Q2 varied information/fixed path; Q3 available information/adaptive investigation; Q4 uncertain information/path requiring exploration. Mixed/unknown states are valid. These are heuristic labels, not scientific scores or ROI rankings.

Compare existing tools, process/rule changes and deterministic automation before adding model calls. Give a simple route and only one justified upgrade. Distinguish model, chat product, workflow/application platform and deployment. RAG does not make missing or conflicting facts true. Adaptive algorithms and human analysis may suffice without agents.

For each route specify authorized inputs/versions, transformation steps, output fields/evidence/nulls, human review, exception/retry/stop rules, accounts/integrations, maintenance owner and acceptance tests. Separate illustrative design, importable template and actual deployment. Never label a plan as ready-to-run integration. Check current official capabilities/terms when possible; otherwise flag them for verification. No untested best-tool claims.

Hand off one solution brief: selected scope, alternative considered, roles, assumptions, prerequisites, output contract, failure cases and evaluation tasks. Escalate unresolved data authority or action permissions to the responsible user. Planning does not authorize deployment, purchases, messages, payments or writes.


## Technical recommendations, learning and delivery

Organize by business capability: rules/single-step interpretation, document parsing, RAG, structured analysis, fixed workflow, tool connections, adaptive agents, state orchestration, harness/context, justified customization and operational delivery. RAG, LangChain, LangGraph, harnesses, MCP and model brands are not mutually exclusive alternatives or mandatory layers.

Each recommendation includes use/avoid conditions, simple route, upgrade trigger, input/account/region/data/maintenance prerequisites, official resources, role-appropriate learning sequence and small exercise, acceptance/failure/intervention and next action. At most two relevant routes; business users need not learn every framework or code first.

Resolve missing facts/permissions first. Fine-tuning needs authorized data, diagnosed failures and held-out evaluation; it is not the default for live knowledge updates. Ongoing/shared use needs versioned data, privacy, logs, budgets, retries/idempotency, rollback and ownership. Demo success is not completed delivery.

Label resource overview, design blueprint, official tutorial, repository runnable example and actual pilot separately. Never claim unexecuted integration/deployment or gains. The repository route map and learning paths supply optional detail.
