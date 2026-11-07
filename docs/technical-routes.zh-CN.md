# 从业务问题选技术路线

[首页 / Overview](../README.md) · [中文](technical-routes.zh-CN.md) · [English](technical-routes.en.md) · [交互路线导航 / Navigator](https://codyqin.github.io/ai-task-compass/solution-navigator.html)

这是一张方案与学习地图，不是技术名词排行榜。每条路线按业务问题组织，先比较不用新平台的小版本。不同路线可以组合，也可能无需 AI。官方能力资料已核对，不代表安装、集成和业务效果已实测。

RAG 是架构做法，LangChain 是开发框架（当前也提供 harness 能力），LangGraph 处理状态编排，Harness 指模型循环周边的运行机制，DeepSeek 是模型服务候选，MCP 是连接标准。它们不是互斥选项。一套方案可能组合这些层，也不必全部采用。

## 规则与普通自动化

- **业务问题：**表格汇总、规则计算、重复流转
- **适用条件：**输入和规则已确认，输出可确定核对
- **不适用与先处理什么：**规则与口径没确认，或需要理解自然语言时先补这部分
- **起步方案与升级：**现有表格/脚本；跨系统重复运行再比较工作流
- **需要准备：**重复键、单位、异常规则与负责人
- **最小学习练习：**用一份已知答案的小表验证规则
- **怎样验收：**总数、异常、重复和返工
- **资料 / Resources：**[n8n](https://docs.n8n.io/)

## 提示词与结构化输出

- **业务问题：**反馈分类、字段提取、草稿整理
- **适用条件：**输出字段稳定，输入文字表达多变
- **不适用与先处理什么：**无来源事实、重要决定或计算不能靠模型猜
- **起步方案与升级：**现有聊天+字段表；需要重复应用再比较 Dify
- **需要准备：**字段、未知值、证据引用、人工检查
- **最小学习练习：**用少量脱敏材料按固定字段提取并核对
- **怎样验收：**漏项、无依据内容、格式和人工修改
- **资料 / Resources：**[Dify](https://docs.dify.ai/en/home) · [DeepSeek](https://api-docs.deepseek.com/) · [Qwen / Model Studio](https://www.alibabacloud.com/help/en/model-studio/models)

## 文档解析与多模态

- **业务问题：**扫描件、图片、跨页表格、音视频资料
- **适用条件：**业务信息藏在文本以外的格式中
- **不适用与先处理什么：**已经有干净结构化数据时不必先做 OCR
- **起步方案与升级：**先解析出可核对的字段/文本，再进入业务流程
- **需要准备：**授权、格式、语言、单位、原文件定位
- **最小学习练习：**选择容易漏字段的一份文档，与原件逐项核对
- **怎样验收：**识别错误、表格错位、单位和缺失字段
- **资料 / Resources：**[LlamaIndex](https://developers.llamaindex.ai/python/framework/) · [Qwen / Model Studio](https://www.alibabacloud.com/help/en/model-studio/models)

## RAG 与企业知识库

- **业务问题：**按政策/手册回答，反复查内部资料
- **适用条件：**需要依据已授权、可维护的资料回答
- **不适用与先处理什么：**资料版本冲突、缺失事实、只查几份材料时先处理源头或试简单读取
- **起步方案与升级：**少量文件试读；重复共享使用时比较 Dify；代码路线比较 LlamaIndex
- **需要准备：**负责人、版本、访问权限、引用与无答案处理
- **最小学习练习：**选可回答/无答案/冲突问题，分别检查检索与生成
- **怎样验收：**证据命中、引用、过期资料和越权
- **资料 / Resources：**[Dify](https://docs.dify.ai/en/home) · [LlamaIndex](https://developers.llamaindex.ai/python/framework/)

## 结构化数据与业务分析

- **业务问题：**指标报表、数据库查询、经营异常调查
- **适用条件：**有明确指标口径、数据授权和只读查询条件
- **不适用与先处理什么：**缺指标定义不能直接 Text-to-SQL；相关性不能直接说因果
- **起步方案与升级：**表格/BI/人工查询优先；需要时增加受限查询工具和模型解释
- **需要准备：**口径、主键、单位、权限、查询范围和审阅
- **最小学习练习：**用已知结果的一组查询核对指标，再探索异常
- **怎样验收：**数字正确、权限、查询开销与解释依据
- **资料 / Resources：**[Workflows and agents](https://www.anthropic.com/research/building-effective-agents) · [LangChain](https://docs.langchain.com/oss/python/langchain/overview)

## 跨系统工作流

- **业务问题：**触发、审批、通知、固定批处理
- **适用条件：**步骤/分支可以提前定义，重复流转有价值
- **不适用与先处理什么：**只有一次小任务、账号权限和失败处理不明确时先缩小
- **起步方案与升级：**优先现有系统；业务流转比较 n8n，AI 应用流程比较 Dify
- **需要准备：**接口、身份、幂等、重试、失败通知、维护
- **最小学习练习：**先在不写真实业务数据的样本上跑一条路径
- **怎样验收：**重复执行、失败恢复、异常与人工接管
- **资料 / Resources：**[n8n](https://docs.n8n.io/) · [Dify](https://docs.dify.ai/en/home)

## 工具调用与 MCP

- **业务问题：**让 AI 查询授权系统或调用确定工具
- **适用条件：**确实需要实时查询/动作，并有明确接口权限
- **不适用与先处理什么：**MCP 不等于授权、安全边界或必需架构；有普通接口也能做
- **起步方案与升级：**先一个只读工具；兼容多个客户端时再评估 MCP
- **需要准备：**参数校验、最小权限、超时、审计、人工审批
- **最小学习练习：**调用一个受限只读查询并检查非法参数失败路径
- **怎样验收：**参数、权限、工具错误和危险动作是否被阻止
- **资料 / Resources：**[MCP](https://modelcontextprotocol.io/docs/getting-started/intro) · [LangChain](https://docs.langchain.com/oss/python/langchain/overview) · [OWASP GenAI risks](https://genai.owasp.org/llm-top-10/)

## 自适应 Agent

- **业务问题：**调查、研究、多步任务随结果改变下一步
- **适用条件：**目标可验收，路径需要根据新发现调整
- **不适用与先处理什么：**规则完整的固定流程、不可检测的错误或无接管条件不优先
- **起步方案与升级：**先人带工具；需要模型控制时比较 LangChain 或 Dify Agent
- **需要准备：**工具、验收、轮数/费用上限、日志、接管
- **最小学习练习：**给一个目标和受限工具，记录动作与证据
- **怎样验收：**完成率、错误动作、预算、证据与稳定性
- **资料 / Resources：**[LangChain](https://docs.langchain.com/oss/python/langchain/overview) · [Dify](https://docs.dify.ai/en/home) · [Workflows and agents](https://www.anthropic.com/research/building-effective-agents)

## 状态与流程编排

- **业务问题：**长流程暂停、恢复、人工确认、多分支状态
- **适用条件：**确实有跨步骤状态和恢复要求
- **不适用与先处理什么：**一次聊天无需先搭持久化编排
- **起步方案与升级：**先清楚状态/节点；代码路线比较 LangGraph，简单应用可用平台流程
- **需要准备：**持久状态、恢复点、并发、版本、接管与运维
- **最小学习练习：**中断一次样本流程，再恢复并核对无重复动作
- **怎样验收：**状态丢失、恢复、重复副作用和审批边界
- **资料 / Resources：**[LangGraph](https://docs.langchain.com/oss/python/langgraph/overview)

## Harness、上下文与记忆

- **业务问题：**长任务跨会话继续、工具循环、进度与上下文管理
- **适用条件：**出现会话交接、上下文膨胀、失去进度等具体问题
- **不适用与先处理什么：**不要因为流行就单独造一套；已有框架可能已经覆盖
- **起步方案与升级：**在已有运行框架上补任务状态、上下文策略、检查、预算与人工接管
- **需要准备：**目标、进度记录、压缩/检索策略、权限、错误恢复
- **最小学习练习：**完成一小段后结束会话，检查能否按记录继续
- **怎样验收：**遗忘目标、虚假完成、重复操作、上下文成本
- **资料 / Resources：**[Long-running harness design](https://www.anthropic.com/research/effective-harnesses-for-long-running-agents) · [LangChain](https://docs.langchain.com/oss/python/langchain/overview) · [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview)

## 模型定制与微调

- **业务问题：**稳定任务在提示词/检索/流程改进后仍不达标
- **适用条件：**有合法训练样本、独立评测与明确改进目标
- **不适用与先处理什么：**不把微调当知识实时更新或替代缺失数据；不要先训练再找业务
- **起步方案与升级：**先定位错误；必要时比较参数高效微调，保留未训练样本
- **需要准备：**数据质量、许可、算力、版本、退化与持续维护
- **最小学习练习：**先做数据/错误分析和小实验计划，不默认开训练
- **怎样验收：**留出样本表现、泛化、成本、退化
- **资料 / Resources：**[PEFT](https://huggingface.co/docs/peft/index) · [Agent evaluations](https://www.anthropic.com/research/demystifying-evals-for-ai-agents)

## 上线、观测与持续维护

- **业务问题：**多人持续使用、追查错误、更新与回滚
- **适用条件：**从演示走到长期服务，需要可追溯与负责人
- **不适用与先处理什么：**没有日志/权限/预算/接管不应把 demo 当生产完成
- **起步方案与升级：**先日志与人工复盘；规模需要时比较 Langfuse 等观测与评测平台
- **需要准备：**数据留存、敏感信息处理、版本、预算、告警、回滚
- **最小学习练习：**回放一个错误和一次版本变化，检查发现/恢复链路
- **怎样验收：**质量回归、延迟、失败、总成本、使用与事件
- **资料 / Resources：**[Langfuse](https://langfuse.com/docs) · [OWASP GenAI risks](https://genai.owasp.org/llm-top-10/) · [Agent evaluations](https://www.anthropic.com/research/demystifying-evals-for-ai-agents)

资料核查：2026-11-07。不同平台的地区、费用、许可与部署条件需在选型时复核。设计建议不等于已接通或可直接导入；不因本项目 MIT 许可推定第三方也采用 MIT。
