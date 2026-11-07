"""Build the offline bilingual route navigator from reviewed data. No model calls."""
from pathlib import Path
import json,sys
from urllib.parse import urlparse

root=Path(__file__).resolve().parents[1]
data=json.loads((root/'resources/solution-routes.json').read_text(encoding='utf-8'))
seen=set()
for route in data['routes']:
    assert route['id'] not in seen, 'Duplicate route ID'
    seen.add(route['id'])
    for field in ['title','problem','when','avoid','start','prerequisites','exercise','acceptance']:
        assert all(route[field].get(lang,'').strip() for lang in ['zh','en']), (route['id'],field)
    assert route['evidence_level']=='official-documentation-reviewed; no integration run claimed'
    assert route['resources']
    for resource in route['resources']:
        assert urlparse(resource['url']).scheme=='https',resource
page=(root/'solution-navigator-template.html').read_text(encoding='utf-8')
page=page.replace('__ROUTES__',json.dumps(data,ensure_ascii=False).replace('</','<\\/'))
target=root/'solution-navigator.html'
outputs={'solution-navigator.html':page}
for lang,suffix in [('zh','zh-CN'),('en','en')]:
    heading='# 从业务问题选技术路线' if lang=='zh' else '# Choose a technical route from the business problem'
    intro=('这是一张方案与学习地图，不是技术名词排行榜。每条路线按业务问题组织，先比较不用新平台的小版本。不同路线可以组合，也可能无需 AI。官方能力资料已核对，不代表安装、集成和业务效果已实测。' if lang=='zh' else 'A decision and learning map, not a technology ranking. Start small, combine routes only when useful, and allow no-AI outcomes. Official documentation has been reviewed; integrations and business outcomes are not claimed as tested.')
    text=heading+'\n\n[首页 / Overview](../README.md) · [中文](technical-routes.zh-CN.md) · [English](technical-routes.en.md) · [交互路线导航 / Navigator](https://codyqin.github.io/ai-task-compass/solution-navigator.html)\n\n'+intro+'\n\n'
    text+=('RAG 是架构做法，LangChain 是开发框架（当前也提供 harness 能力），LangGraph 处理状态编排，Harness 指模型循环周边的运行机制，DeepSeek 是模型服务候选，MCP 是连接标准。它们不是互斥选项。一套方案可能组合这些层，也不必全部采用。\n\n' if lang=='zh' else 'RAG is an architectural approach; LangChain is a framework (including harness capabilities), LangGraph addresses orchestration, a harness surrounds the model loop, DeepSeek is a model-service candidate, and MCP is a connection standard. They overlap and compose; none is a mandatory layer in every project.\n\n')
    for route in data['routes']:
        text+='## '+route['title'][lang]+'\n\n'
        for field,cn,en in [('problem','业务问题','Problem'),('when','适用条件','Use when'),('avoid','不适用与先处理什么','Avoid / resolve first'),('start','起步方案与升级','Start / upgrade'),('prerequisites','需要准备','Prerequisites'),('exercise','最小学习练习','Small learning exercise'),('acceptance','怎样验收','Acceptance')]:
            text+='- **'+(cn if lang=='zh' else en)+'：**'+route[field][lang]+'\n'
        text+='- **资料 / Resources：**'+' · '.join('['+x['title']+']('+x['url']+')' for x in route['resources'])+'\n\n'
    text+=('资料核查：2026-11-07。不同平台的地区、费用、许可与部署条件需在选型时复核。设计建议不等于已接通或可直接导入；不因本项目 MIT 许可推定第三方也采用 MIT。\n' if lang=='zh' else 'Reference review: 2026-11-07. Recheck region, fees, licensing and deployment conditions. Guidance does not mean an installed/importable implementation. Third-party licenses are independent of this repository MIT license.\n')
    outputs['docs/technical-routes.'+suffix+'.md']=text
if '--check' in sys.argv:
    stale=[name for name,value in outputs.items() if not (root/name).exists() or (root/name).read_text(encoding='utf-8')!=value]
    assert not stale,'Run python scripts/build_routes.py: '+', '.join(stale)
    print(f'{len(seen)} bilingual routes valid; navigator and guides match reviewed data.')
else:
    for name,value in outputs.items():
        (root/name).write_text(value,encoding='utf-8')
    print(f'Built navigator and bilingual guides with {len(seen)} routes. No network or model calls.')
