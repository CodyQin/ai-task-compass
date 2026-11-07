# Worked examples and useful checks

All examples are **synthetic**. They illustrate expected reasoning, not model test results, customer deployments or a single correct classification.

## Example 1 — Weekly feedback report

**Request:** “I manually turn customer comments into a weekly report.”

**Useful next question:** “What must the report contain, and can you show one anonymized comment and its expected label?”

Suppose the user confirms predefined labels and a reviewed sample:

| Step | Provisional quadrant | Starting approach | What to check |
|---|---|---|---|
| Interpret comments and extract evidence | Q2 | Existing file-capable assistant; fixed output fields | Missed issues, wrong labels, unsupported claims |
| Count confirmed labels | Q1 | Spreadsheet or script | Duplicate handling and totals |
| Investigate an unexpected pattern | Possibly Q3 | Guided queries based on intermediate findings | Evidence vs speculation; next step may change |

**Pilot:** Choose an authorized small sample and a human reviewer; compare to the current process using agreed quality measures and total time, including corrections. Add a workflow only if repetition and quality justify it. No savings estimate is assumed.

## Example 2 — “We need a knowledge base”

Ask about the last real query, where the answer lived, and which version was authoritative. If policies conflict, establish ownership and valid versions before expecting retrieval to resolve the conflict. Search/retrieval may become Q2; fixing authoritative rules is a human responsibility. Do not recommend a vector database before clarifying the need.

## Example 3 — “Everyone is busy; we need AI”

Ask for a recent task, waiting/rework, frequency and output. With insufficient evidence, keep classification provisional or explore under Q4. Observe a small number of real occurrences first. A viable next action can be recording inputs, steps and delays; do not invent ROI or assume poor management.

## Other starting points

| Input | Useful behavior |
|---|---|
| Merge consistent tables with agreed rules | Consider Q1 and existing tools; confirm exceptions and checks |
| Known data, next investigation depends on findings | Consider Q3 per step; try guided tool analysis before orchestration |
| Discount computed, approval authority unclear | Clarify ownership/rules; do not let AI autonomously approve discounts |
| Tailor a resume and practice interviews | Split interpretation, truthful expression and practice; never invent experience |
| “I don't know; give me a first plan” | Provide explicit assumptions, unknowns and one small next step; avoid endless interrogation |

For actual trials record anonymized inputs, model/date, questions, corrections, evidence for classification, tool prerequisites, review cost and whether the next step was actionable. Structural checks are not evidence of model quality.


## Collection example: a creator workflow

Synthetic scenario, not Cody's observed result: “Producing videos takes too long; where can AI help?” Discovery asks about a recent episode and distinguishes research, fact-checking, structure, delivery and editing. Design may assist authorized-source organization and draft alternatives while retaining human editorial/factual responsibility. Evaluation compares traceable sources, omissions, unsupported content and editing effort before speed. A pilot covers one step with time/call limits; quality, audience response and revenue are separate.

Carry the same brief forward: “research organization only; sources required; no automatic publication; try one authorized sample.” Later modules must not silently turn this into an autonomous content factory.

## Collection example: an early venture

Synthetic input: “I want to sell an AI service but have not spoken with users.” Clarify a concrete user problem, current alternative, buyer and evidence; propose a low-cost learning test. Synthetic willingness-to-pay is not validation. Model procurement or precise revenue forecasting may be premature.
