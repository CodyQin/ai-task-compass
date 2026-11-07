"""Build a portable chat prompt from the skill, without network or model calls."""
from pathlib import Path
import re
import sys
import json

root = Path(__file__).resolve().parents[1]
skill = root / 'skills/task-compass'
text = (skill / 'SKILL.md').read_text(encoding='utf-8-sig')
body = re.sub(r'\A---\r?\n.*?\r?\n---\r?\n', '', text, count=1, flags=re.S).strip()
body = body.replace('需要具体工具时读取 [references/tool-routes.md](references/tool-routes.md)，将其当候选地图而非固定排名。', '需要具体工具时参考本提示词末尾的工具路线，将其当候选地图而非固定排名。')
body = body.replace('此 Skill', '本协议')
body = body.replace('(references/protocol.en.md)', '(https://github.com/CodyQin/ai-task-compass/blob/main/skills/task-compass/references/protocol.en.md)')
body = body.replace('(references/tool-routes.en.md)', '(https://github.com/CodyQin/ai-task-compass/blob/main/skills/task-compass/references/tool-routes.en.md)')
routes = (skill / 'references/tool-routes.md').read_text(encoding='utf-8-sig').strip()
result = ('# 可直接复制的完整对话提示词\n\n'
          '请担任我的任务拆解与 AI 应用规划伙伴，按以下协议交流。先用一句话邀请我描述一项真实工作；如果我已经描述过，直接提出最影响判断的下一问。\n\n'
          + body + '\n\n---\n\n' + routes + '\n')
target = root / 'PROMPT.md'
chart = (root / 'assets/task-quadrants.svg').read_text(encoding='utf-8-sig')
page = (root / 'index-template.html').read_text(encoding='utf-8-sig')
page = page.replace('__CHART__', chart).replace('__PROTOCOL__', json.dumps(result, ensure_ascii=False).replace('</', '<\\/'))

english = (skill/'references/protocol.en.md').read_text(encoding='utf-8').strip()
english += '\n\n---\n\n' + (skill/'references/tool-routes.en.md').read_text(encoding='utf-8').strip() + '\n'
english = 'Please help me decide how to improve one real task. Follow the protocol below; if I have already described the task, ask the next most useful question.\n\n' + english
enpage = (root/'en-template.html').read_text(encoding='utf-8').replace('__PROTOCOL__', json.dumps(english, ensure_ascii=False).replace('</', '<\\/'))
outputs = {'PROMPT.md': result, 'index.html': page, 'PROMPT.en.md': english, 'en.html': enpage}
if '--check' in sys.argv:
    stale = [name for name, value in outputs.items() if not (root/name).exists() or (root/name).read_text(encoding='utf-8-sig') != value]
    if stale:
        raise SystemExit('Regenerate: ' + ', '.join(stale))
    print('All Chinese and English generated assets match their sources.')
else:
    for name, value in outputs.items():
        (root/name).write_text(value, encoding='utf-8')
    print('Built bilingual prompts and standalone pages; no network or model calls.')
