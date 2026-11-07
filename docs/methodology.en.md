# Why these two dimensions?

[Overview](../README.md) · [中文](methodology.zh-CN.md)

This is an engineering heuristic, not a theorem, validated taxonomy or claim of original research.

**Information-processing need:** Can known inputs, rules and conditions be processed directly, or is interpretation, retrieval or clarification needed? Distinguish variable expression, missing facts and conflicting/untrusted sources. A model or retrieval system does not automatically resolve the latter two.

**Control-path predictability:** Can the next action and branches be specified before execution, or does new evidence require a judgment about what to investigate next? Fixed workflows may contain many branches, loops and retries. Complexity and branching alone do not justify agents. Adaptive work can also use conventional search, optimization or human expertise.

These axes address different implementation choices: information handling and control. They need not be statistically independent. Two binary simplifications produce four combinations; the thresholds are chosen, not discovered natural laws. Unknowns, intermediate states and mixed task steps remain valid.

| | Predefined path | Adaptive path |
|---|---|---|
| Information directly processable | Q1: agreed table rules | Q3: evidence-led investigation with available data |
| Interpretation / clarification needed | Q2: fixed-field extraction from varied text | Q4: unclear task requiring exploration |

## Research versus project synthesis

- **Main conceptual reference:** Perrow (1967), [A Framework for the Comparative Analysis of Organizations](https://www.jstor.org/stable/2091811), studies exceptions and analyzability of search. It motivates considering more than one task property. Our axes and labels are not his original variables or taxonomy.
- **Additional mechanism:** Galbraith (1974), [Organization Design: An Information Processing View](https://jaygalbraith.com/wp-content/uploads/2024/03/infoprocess1974.pdf), relates task uncertainty to information processing during execution. It does not establish our exact matrix.
- **Engineering bridge:** [Building effective agents](https://www.anthropic.com/research/building-effective-agents) distinguishes predefined workflows from model-directed processes. It explains the control distinction, not this project's four-quadrant taxonomy. The 2024 product landscape is dated.

Primary material checked 2026-11-07. Explanations are paraphrases; papers are not redistributed. Research inspiration, project adaptation and unvalidated claims are explicitly separated.

## Boundaries

Quadrants do not determine ROI, risk, permission to act or truth. Structured data can be false; model confidence is not automatically calibrated. An adaptive algorithm need not be an LLM agent. If the axes cannot be distinguished for a task, split it again instead of forcing a label. Separately decide business value, evidence quality and execution controls.
