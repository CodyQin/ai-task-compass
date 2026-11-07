# Install once, start with one sentence

[Overview](../README.md) · [中文](install-and-start.zh-CN.md) · [Modules](skill-collection.en.md)

## Choose your entry

- **Ordinary AI chat:** use the [no-install starter](https://codyqin.github.io/ai-task-compass/en.html), describe your work, and paste the generated full message into your AI. A short slash command does not load this repository into a chat that has not installed the skill.
- **Codex / Claude Code or another skill-capable tool:** install `task-compass`, the integrated entry. It includes stage selection and planning guidance; installing the four specialist skills is optional.

## 1. Install from your terminal

Prerequisites: Node.js 22.20+ with npm/npx, Git, access to GitHub, and a working, configured target AI tool. Your tool supplies the model/account; this project supplies no inference credits.

```sh
npx skills add CodyQin/ai-task-compass --skill task-compass -g
```

Select your AI tool when prompted. `-g` installs at user scope across projects. Without `-g`, installation is project-scoped: open your AI tool in that project. On Windows, select Copy if symlinks are unavailable, or use an explicit command below.

**Codex**
```sh
npx skills add CodyQin/ai-task-compass --skill task-compass -a codex -g --copy
```

**Claude Code**
```sh
npx skills add CodyQin/ai-task-compass --skill task-compass -a claude-code -g --copy
```

The third-party open-source [vercel-labs/skills](https://github.com/vercel-labs/skills) installer copies the skill and references into the appropriate tool directory. This is not a custom CLI provided by AI Task Compass. No project server is needed.

## 2. Start inside your AI conversation

**Codex**
```text
$task-compass Help me find where AI could improve my business. Start with the most important question.
```

**Claude Code**
```text
/task-compass Help me find where AI could improve my business. Start with the most important question.
```

Add a concrete task: “Every week I turn customer comments into a report. Organizing and checking take too long. Help me map the work before choosing AI tools.” The invocation belongs in the AI conversation, not the terminal.

## 3. What to expect

With no task supplied, the AI should invite one real example. With context supplied, it should reuse it and ask the next useful question rather than deliver a long tool list. When enough is known, it can produce a shared brief, task responsibilities, routes, acceptance criteria and a bounded pilot.

Actual responses depend on the model. Installation does not validate a business plan. Templates, the navigator and calculator remain available in [Start here](../START-HERE.md); installing a skill does not connect your business systems.

## Troubleshooting

- No `npx`: install Node.js LTS version 22.20+ and reopen the terminal, or use the no-install starter.
- Skill not found: verify the selected tool and installation scope; try a new conversation or restart. Project-scoped skills require the matching project. Check the tool's skill list and documentation.
- Windows symlink error: add `--copy`; this project does not require changing execution policy.
- Update: rerun the installation command and confirm replacing this skill, or follow the installer's `skills check` / `skills update` documentation. Preserve personal edits first.
- Specialist only: replace the `--skill` value with a name from the [module table](skill-collection.en.md).

## References

- [Installer options](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)
- [Supported tools and paths](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
- [OpenAI skill invocation and discovery](https://learn.chatgpt.com/docs/build-skills)
- [Claude Code skills](https://code.claude.com/docs/en/skills)

Checked 2026-11-07. Public-repository download and project-scoped Copy installation layouts were checked for both tools. Cross-platform conversational behavior and business ROI have not been established.
