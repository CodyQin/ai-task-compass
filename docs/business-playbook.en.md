# Business owner and product manager playbook

[Overview](../README.md) · [中文](business-playbook.zh-CN.md) · [Worksheet](../WORKSHEET.md) · [Calculator](../business-calculator.html)

The project supplies planning protocols, references, design blueprints and pilot tools, not an already integrated business platform.

## Owner: define value and constraints

Identify who receives what and delivers which outcome. Record a recent occurrence, frequency, execution/review/rework time and quality baseline. Mark estimates. Define business acceptance, authorized data, region, budget, existing tools and maintenance ownership. Released employee time is capacity, not automatically cash savings. Consider process/rule fixes and existing software before procurement.

## PM: specify a bounded product

Map input → action → check → handoff, including waits and exceptions. Classify steps separately. Each step needs user, trigger, authorized/versioned inputs, output fields, evidence, prohibited invention, exception handling, intervention, acceptance, logs and owner. Unknowns remain unknown; ask only questions that change a decision.

Compare a simple existing-tool route and, only if justified, an engineering route. Explain prerequisites, effort, benefit assumptions and stop conditions. Do not collapse value, feasibility, risk and data readiness into a fake scientific score.

## Minimal pilot PRD

```text
Problem, user and measurable baseline:
In-scope step and explicitly excluded actions:
Authorized input, versions and output/evidence schema:
Typical, exceptional, missing and conflicting test cases:
Acceptance owner and business-approved quality/time thresholds:
Human approvals, failure recovery, retries and call budget:
Access controls, logging, retention, maintainer and rollback:
Review date and continue/revise/stop conditions:
```

## Measure, then expand

Measure quality (omissions, unsupported facts, severity, editing), total time (preparation, execution, review, rework) and cash separately. Count model calls, token usage, retries, retrieval and human intervention. One chat's token bill is not full operating cost.

Use the [calculator](../business-calculator.html) for conditional estimates in one consistent currency. It is local, with no model calls or task upload. ROI is not a promise. Quality failure cannot be offset merely by faster output.

Start with authorized samples and human observation. Expand only with acceptance, logs, intervention and ownership. Re-run retained cases when prompts, models or data change. A successful demo is not evidence of production reliability.

Next: [blueprints](solution-blueprints.en.md), [model selection](model-selection.en.md), [evaluation CSV](../templates/model-evaluation.csv). Blueprints are illustrative designs, not ready-to-import deployments.
