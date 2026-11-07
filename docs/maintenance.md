# 维护与贡献 · Maintenance

[首页](../README.md) · [总导航](../START-HERE.md)

## 单一数据源 / Sources of truth

- `skills/task-compass/SKILL.md` 与工具参考 / tool references build `PROMPT.md` and the Chinese starter.
- `skills/task-compass/references/protocol.en.md` 与英文工具参考 / English route references build `PROMPT.en.md` and the English starter.
- `resources/solution-routes.json` builds the navigator and both technical-route guides. Edit the source, not separate lists in generated files.
- Skills can be installed independently; do not introduce unnecessary dependencies or claim unperformed integrations/evaluations.

## 生成与检查 / Build and check

```text
python scripts/build_prompt.py
python scripts/build_routes.py
python scripts/build_prompt.py --check
python scripts/build_routes.py --check
node scripts/check-business-math.js
```

Python build scripts use the standard library. Node is only needed for the calculator checks. End users need neither.

中英文意图保持一致。新增路线说明业务问题、适用/不适用、起步、前提、官方资料、练习与验收；不要以覆盖流行词为目标。 / Keep language intent aligned and recommendations business-led.

图的 PNG 用于稳定显示，SVG 是可编辑源；图中只陈述现有交付，不添加虚构客户数字或效果。 / PNGs provide consistent display; SVGs are editable sources. Do not add unsupported outcome claims.

## 反馈 / Feedback

Provide an anonymized task, model/version/date if relevant, observed problem and expected behavior through Issues. Do not post secrets or private business data. Proposals are welcome; mark untested ideas and synthetic examples explicitly.

Project originals are MIT-licensed. External tools/resources retain their own terms and licenses.
