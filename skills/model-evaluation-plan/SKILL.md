---
name: model-evaluation-plan
description: Design a task-specific comparison of feasible models or AI workflows using business acceptance, representative cases, evidence and full cost; does not claim to run tests or rank untested models.
---


# Model and system evaluation · 模型与系统评测

Respond in the user's language. Start from the required output and acceptance owner. Evaluate the delivered system (model, prompt, tools, retrieval, configuration and data), not brand reputation or fluent prose alone.

Filter candidates by authorized data, region/access, required modalities/tools, budget and maintainability. Prefer at most two feasible candidates at first. State unverified current capabilities or pricing rather than inventing them.

Define reference outputs or rubrics before comparison: important omissions, unsupported claims, schema/tool errors, severe failures, time and human correction. Include typical, missing, conflicting and consequential edge cases. Use authorized/anonymized inputs and retain held-out checks separate from examples used to tune prompts. Sample size and repetitions depend on risk and budget; small convenience samples do not establish population accuracy.

Record model/system versions, date, prompt version, settings, permissions, cases, completion/acceptance, severe errors, calls/retries, tokens, elapsed time, actual fees and human review. Count failed/retried work, not just a successful run. Human or deterministic review is needed for consequential errors; a model judge alone is not an oracle. Self-reported confidence is not automatically calibrated.

Pass quality requirements first, then compare total cost per accepted delivery with clear accounting. With no accepted deliveries, do not divide by zero or show a favorable unit cost. Separate monetized staff capacity from cash expense. Route/escalate only with observable error checks and fallbacks.

Output the evaluation plan, case/rubric table, run log schema, selection conditions and unresolved questions. A plan or filled synthetic example is not an executed evaluation. Do not incur API charges or run external tests without task authorization. If real results are provided, analyze them with limitations and recommend continue/revise/stop.
