# AI Task Compass — detailed guide

[Repository overview](https://github.com/CodyQin/ai-task-compass) · [Start here](START-HERE.md)

**Should this task use AI, a workflow, an agent—or just a better process?**

A practical, open-source conversation framework that helps you describe real work, answer a few useful questions, and turn it into a task breakdown, tool route and small pilot. Designed for people who understand their work but may not know which AI architecture to choose.

No account, API key or installation is required by this project. Bring your own AI chat; that provider may charge for usage.


**Already using Codex / Claude Code?** [Install once, start with one sentence](docs/install-and-start.en.md).

## Start in a minute

1. Open the **[English page](https://codyqin.github.io/ai-task-compass/en.html)** or **[中文页面](https://codyqin.github.io/ai-task-compass/)**.
2. Describe one actual task, generate a starter message, then copy it into your AI assistant.
3. Answer its clarifying questions and ask for one small next step.

**Prefer copy and paste?** Open [PROMPT.en.md](PROMPT.en.md) or [PROMPT.md 中文](PROMPT.md), click **Raw**, copy the full text into a new chat, then add your task. No web page is needed.

Try this:

> Each week I turn dozens of customer comments into a report. I manually label, count and summarize them. I want fewer missed issues, but don't know whether to use chat or a workflow. Ask the most important clarifying question first. Reply in English.

## What you get

| Deliverable | What it helps you decide |
|---|---|
| A confirmed problem statement | What matters, what is known and what still needs evidence |
| A step-by-step task map | Which parts need rules, interpretation, analysis or exploration |
| Human / AI / tool responsibilities | Where review or process changes are needed |
| Up to two tool routes | Start with available tools; understand upgrade conditions |
| A small pilot | Samples, acceptance measures, owner, intervention and stop conditions |
| Cost and benefit questions | Include preparation, maintenance, checking and rework |

Start with one step and a few authorized samples. Check the proposed understanding before implementing a plan. This is decision support, not an autonomous execution service.

## The four-quadrant lens

| | Known, stable information | Varied or uncertain information |
|---|---|---|
| **Adaptive path** | **Q3 · Adaptive analysis** — choose the next step from intermediate evidence | **Q4 · Explore & validate** — clarify, investigate, experiment |
| **Predefined path** | **Q1 · Fixed execution** — rules, formulas, conventional automation | **Q2 · Interpret & organize** — extraction, understanding, retrieval in a defined process |

Use it on **task steps**, not an entire company. Mixed and unknown classifications are valid. These labels are not mathematical quadrant numbering or a maturity ranking. The axes are information uncertainty (rightward) and path adaptability (upward). A quadrant alone cannot establish ROI or justify an agent.

The lens is a practical heuristic, not a claimed original scientific taxonomy. The contribution here is the interview protocol and its bridge to responsibilities, implementation routes and pilot design. Tool guidance links to official documentation and distinguishes fixed workflows from adaptive agent behavior; see [route references](skills/task-compass/references/tool-routes.en.md).

## Use as an Agent Skill

Copy the complete [`skills/task-compass/`](skills/task-compass/) folder into the skills directory supported by your agent, and follow that agent's loading instructions. Then ask:

> Use task-compass to help me decide how to improve this task. Reply in English.

Directory conventions vary; this is not a universal installer. If your tool does not support skills, use the standalone prompt instead. The skill includes Chinese and English guidance and should respond in your requested language.

## Plan your first pilot

Use the **[bilingual task & pilot worksheet](WORKSHEET.md)** to keep facts, assumptions, responsibilities, acceptance measures and costs in one place. Fill only what you know; let the interview identify the next useful gap.

## Examples

See **[worked examples](examples.en.md)** / **[中文场景](examples.md)**: reports, feedback, knowledge bases, adaptive analysis, unclear goals and career work. Examples are synthetic illustrations, not measured model runs or customer case studies.

## Privacy and scope

The starter pages assemble text in your browser. They make no model calls, add no analytics and send no task content to this project. GitHub hosting has its own access logs. Once you paste a message into an AI product, that provider's data policy applies. Use anonymized material, never secrets or unnecessary customer data.

The framework does not install software, deploy systems, contact clients, modify business records or spend API credits. Those require a separately authorized implementation scope.

## FAQ

**Is it free?** The repository is MIT-licensed. AI providers and external platforms have separate terms, availability and costs.

**Does the website answer my question?** It prepares a complete message. Your chosen AI conducts the conversation after you paste it.

**Will it always ask many questions?** It should ask the next decision-relevant question, reuse context and allow unknowns. You can request a provisional plan with explicit assumptions.

**Is the output proven?** v0.4 ships usable prompts, a skill and standalone pages. No controlled model benchmark or measured business gains are claimed. Review recommendations against your real work.

**What if a recommended tool is unavailable?** Tell the assistant your region, budget, existing accounts and deployment limits. Ask for accessible alternatives and recheck official terms before adoption.

## Download, maintain and contribute

- Download a **[release ZIP](https://github.com/CodyQin/ai-task-compass/releases/latest)** or use GitHub **Code → Download ZIP**. Open `index.html` or `en.html` locally; internet is only needed for your AI product and external links.
- Only Python **3.10+**, standard library, is needed to rebuild; end users need no Python.
- After editing the skill or references, run `python scripts/build_prompt.py`. Run `python scripts/build_prompt.py --check` before a PR. CI checks generated files on pushes and PRs.
- Keep Chinese and English aligned. New examples should state inputs, expected reasoning and limitations. Report problems through [Issues](https://github.com/CodyQin/ai-task-compass/issues), with an anonymized task, model/date, observed problem and expected behavior. Do not post private business data.

Maintained by **[Cody Qin](https://github.com/CodyQin) / Q弟学了吗**. Contributions are welcome; response times and business outcomes are not guaranteed.

## License

[MIT](LICENSE) for this project's original material. Referenced tools and third-party content retain their own licenses and conditions. This license does not relicense them.
