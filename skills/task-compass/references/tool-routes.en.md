# Tool routes, not a product ranking

Reference date: 2026-11-06 (Los Angeles). Recheck official capabilities, license, region availability, pricing, deployment and data policies before adoption. These are starting candidates, not a complete comparison.

| Need | Start small | Upgrade condition | Candidate / reference |
|---|---|---|---|
| Known rules and calculations | Existing spreadsheet, built-in functions or a small script | Many files, scheduling or system integration | Excel/WPS or Python; define validation and exception handling first |
| Triggers, handoffs, notifications | Existing system automation | Several integrations, authentication and failure recovery | [n8n docs](https://docs.n8n.io/): workflows can include AI; workflow does not mean agent |
| Understand, extract or label files | A compatible chat assistant with anonymized samples | Repeated use, larger collections, access/version requirements | Validate parsing, missing values and evidence before building infrastructure |
| Knowledge retrieval and AI workflows | A narrowly scoped question using available tools | Clear sources, application access and operational ownership | [Dify docs](https://docs.dify.ai/en/home): retrieval does not guarantee correct answers |
| Adaptive multi-step tool use | Guided conversation and explicit tools, observed manually | Persistent state, interruption, recovery and repeated autonomous steps | [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview): orchestration/runtime; still needs requirements, development and evaluation |
| Unfamiliar or ambiguous work | Interviews, source-based research and small experiments | Repeatable process and acceptance criteria emerge | [Building effective agents](https://www.anthropic.com/research/building-effective-agents): conceptual guidance; its 2024 tool landscape is not a current catalog |

Keep at most two relevant routes in a recommendation. Coze, FastGPT, Make and Zapier may fit particular environments; this project has not comprehensively verified or compared them. Third-party licenses are independent of this repository's MIT license.

**Synthetic example:** For weekly feedback, start with anonymized text and agreed labels; ask for category, original evidence and uncertainties; review missed and incorrect labels. Consider a workflow only after repeated runs have acceptable quality. Add retrieval or access/version management when the sources justify it. No measured improvement is claimed.


## 深入资料 / Further reading

- [为什么是两个维度 / Methodology](https://github.com/CodyQin/ai-task-compass/blob/main/docs/methodology.en.md)
- [老板与产品经理 / Business & PM playbook](https://github.com/CodyQin/ai-task-compass/blob/main/docs/business-playbook.en.md)
- [模型选择与评测 / Model selection](https://github.com/CodyQin/ai-task-compass/blob/main/docs/model-selection.en.md)
- [起步方案 / Blueprints](https://github.com/CodyQin/ai-task-compass/blob/main/docs/solution-blueprints.en.md)
- [业务测算器 / Business calculator](https://codyqin.github.io/ai-task-compass/business-calculator.html)
