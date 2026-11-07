# 一行安装，一句话开始

[项目首页](../README.md) · [English](install-and-start.en.md) · [全部模块](skill-collection.zh-CN.md)

## 选择适合你的入口

- **普通聊天用户**：打开[免安装使用页](https://codyqin.github.io/ai-task-compass/)，填写业务问题，把生成的完整消息复制到常用 AI。输入一个 `/task-compass` 不会让未安装技能的普通聊天自动加载本项目。
- **已经使用 Codex / Claude Code 等技能工具**：安装下面的 `task-compass` 统一入口，之后用一句话启动。只装这一项即可按需推进需求、方案、模型评测和试点复盘；四个专项 Skill 可另外选装。

## 1. 在终端安装一次

需要 Node.js 22.20+（含 npm/npx）、Git、可访问 GitHub 的网络，以及已配置并可使用的目标 AI 工具。模型服务与账号由目标工具提供，本项目不提供模型或调用额度。

```sh
npx skills add CodyQin/ai-task-compass --skill task-compass -g
```

按安装器提示选择你的 AI 工具。`-g` 表示当前用户级安装，可跨项目使用；默认不加 `-g` 则只安装到当前项目，需要在同一项目中打开 AI 工具。Windows 若不能创建符号链接，选择 Copy 或使用下方带 `--copy` 的命令。

已经确定工具时，直接复制对应的一行：

**Codex**
```sh
npx skills add CodyQin/ai-task-compass --skill task-compass -a codex -g --copy
```

**Claude Code**
```sh
npx skills add CodyQin/ai-task-compass --skill task-compass -a claude-code -g --copy
```

安装器为第三方开源工具 [vercel-labs/skills](https://github.com/vercel-labs/skills)，不是本项目自建的命令程序。它把仓库中的技能与配套引用安装到目标工具的目录。无需另外启动本项目服务器。

## 2. 在 AI 对话里说你想做什么

**Codex：**
```text
$task-compass 我想用 AI 改善自己的业务，请先帮我找出最值得解决的问题。
```

**Claude Code：**
```text
/task-compass 我想用 AI 改善自己的业务，请先帮我找出最值得解决的问题。
```

也可以直接带上具体工作，例如：
```text
我每周都要把客户反馈整理成报告，整理和核对特别耗时。先帮我梳理流程，再判断哪里值得用 AI。
```

调用入口后可以直接补充这段，不需要先懂 RAG、Agent 或四象限。不要把 `/task-compass` 当终端命令；它是 Claude Code 对话中的技能调用。Codex 用 `$task-compass`。

## 3. 怎样判断已经开始

若尚未描述任务，AI 应先邀请你描述一项真实工作；已经交代任务时，应复用信息，给当前观察并提出最影响下一步判断的问题，而非立即抛出整套工具清单。信息足够后，按需要形成同一份项目简报、任务分工、路线、验收和试点计划。

这是预期交互，具体回答取决于模型；安装成功不等于业务方案已经被验证。模板、路线导航和测算器保留在[项目总导航](../START-HERE.md)，不会因为安装 Skill 就自动接通外部业务系统。

## 常见问题

- `npx` 不存在：先安装 Node.js LTS（版本至少 22.20），重开终端；或直接使用免安装页。
- 找不到技能：核对安装成功的目标工具与范围；尝试新开对话或重启工具。项目级安装必须在对应项目使用。若仍不出现，查看该工具的技能列表与官方说明。
- Windows 链接失败：加 `--copy` 重新安装；无需为了这个项目修改系统执行策略。
- 想更新：重新运行原安装命令并确认覆盖本技能，或按安装器的 `skills check` / `skills update` 说明操作；先保留自己的定制。
- 想只用专项模块：把命令的 `--skill task-compass` 换成[模块表](skill-collection.zh-CN.md)中的名字。

## 官方与安装器说明

- [安装器与参数](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)
- [支持的工具与目录](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
- [OpenAI：技能的调用与发现](https://learn.chatgpt.com/docs/build-skills)
- [Claude Code：技能调用](https://code.claude.com/docs/en/skills)

核对日期：2026-11-07。公开仓库下载与两个工具的项目级 Copy 安装布局已检查；不代表跨平台对话效果或业务 ROI 已验证。
