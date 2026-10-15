#!/usr/bin/env python3
"""inventory.py — list every learning material in this repository.

    python3 tools/inventory.py            update the Inventory section of every topic README + docs/INVENTORY.md
    python3 tools/inventory.py --check    only print problems (missing titles, labs without manual, unused materials)
    python3 tools/inventory.py --init IC-Design/Digital-Design/FPGA
                                          make a last-level topic ready for materials: adds the material folders
                                          and the Materials / Inventory sections to its README

Material folders exist only at the LAST level of the hierarchy (a topic with no sub-topics).
A topic is a folder with the material folders lectures/ trainings/ labs/ projects/ videos/ materials/.
Recognised materials:
  trainings/<name>/training.json            interactive training (academy-templates:training)
  labs/<name>/lab/lab.json                  lab (academy-templates:lab-manual)
  projects/<name>/project/project.json      project (academy-templates:project-brief + brief2project.py)
  lectures/*.md | *.pdf, lectures/<name>/*.md   lecture notes / readings
  videos/*.mp4 | *.webm, videos/links.md    videos
  materials/*                               other files
"Used in" lists the package specs (Packages/*/pack-spec.json) whose sources point into the material."""
import json, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
TYPES = ('lectures', 'trainings', 'labs', 'projects', 'videos', 'materials')
SKIP = {'Packages', 'tools', '.git', 'node_modules'}


def rjson(p):
    try:
        with open(p, encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return None


_PARTNERS = None


def partner_keys():
    """keys registered in docs/PARTNERS.md (the `key` column of its tables)"""
    global _PARTNERS
    if _PARTNERS is None:
        f = os.path.join(ROOT, 'docs', 'PARTNERS.md')
        txt = open(f, encoding='utf-8').read() if os.path.exists(f) else ''
        _PARTNERS = set(re.findall(r'^\|\s*`([a-z0-9][a-z0-9-]*)`\s*\|', txt, re.M))
    return _PARTNERS


def meta_of(abspath):
    """a material's meta.json: beside it, or one level up (labs and projects record .../lab, .../project)"""
    d = abspath if os.path.isdir(abspath) else os.path.dirname(abspath)
    for cand in (d, os.path.dirname(d)):
        m = rjson(os.path.join(cand, 'meta.json'))
        if isinstance(m, dict):
            return m
    return {}


def meta_tag(m, where, problems):
    """short suffix for the Info column; everything omitted means foundation / released / en"""
    if not m:
        return ''
    bits = []
    if m.get('status') and m['status'] != 'released':
        bits.append(m['status'])
    if m.get('origin') == 'partner':
        k = m.get('partner') or '?'
        bits.append('with ' + k)
        if k not in partner_keys():
            problems.append(f'{where}: partner "{k}" is not registered in docs/PARTNERS.md')
    elif m.get('origin') == 'community':
        bits.append('community')
    elif m.get('origin') not in (None, 'foundation'):
        problems.append(f'{where}: unknown origin "{m["origin"]}" (foundation / partner / community)')
    if m.get('audience'):
        bits.append(m['audience'])
    if m.get('language') and m['language'] != 'en':
        bits.append(m['language'])
    return (' · ' + ', '.join(bits)) if bits else ''


def topics():
    out = []
    for r, ds, fs in os.walk(ROOT):
        ds[:] = sorted(d for d in ds if d not in SKIP and not d.startswith('.') and d not in TYPES)
        if r != ROOT and any(os.path.isdir(os.path.join(r, t)) for t in TYPES):
            out.append(r)
    return out


def package_sources():
    """absolute source path -> [package titles]"""
    m = {}
    pk = os.path.join(ROOT, 'Packages')
    for d in sorted(os.listdir(pk)) if os.path.isdir(pk) else []:
        spec = rjson(os.path.join(pk, d, 'pack-spec.json'))
        if not spec:
            continue
        name = (spec.get('pack') or {}).get('title') or d
        for g in ('trainings', 'labs', 'readings', 'videos', 'materials', 'projects'):
            for e in spec.get(g, []):
                if e.get('source'):
                    m.setdefault(os.path.normpath(os.path.join(pk, d, e['source'])), []).append(name)
    return m


def used_in(path, srcs):
    path = os.path.normpath(path)
    names = set()
    for s, ns in srcs.items():
        if s == path or s.startswith(path + os.sep) or path.startswith(s + os.sep):
            names.update(ns)
    return sorted(names)


def scan(topic, srcs, problems):
    items = []
    rel = lambda p: os.path.relpath(p, topic)
    def add(kind, title, path, info, ok=True):
        info += meta_tag(meta_of(path), os.path.relpath(path, ROOT), problems)
        items.append({'kind': kind, 'title': title, 'path': rel(path), 'info': info, 'used': used_in(path, srcs), 'ok': ok})
    d = os.path.join(topic, 'trainings')
    for n in sorted(os.listdir(d)) if os.path.isdir(d) else []:
        p = os.path.join(d, n)
        if not os.path.isdir(p):
            continue
        tr = rjson(os.path.join(p, 'training.json'))
        if not tr:
            problems.append(f'{os.path.relpath(p, ROOT)}: no valid training.json'); continue
        sc = tr.get('schedule') or {}
        add('Training', tr.get('title', n), p, f"{len(tr.get('topics', []))} topics" + (f", {sc.get('weeks')}-week plan" if sc.get('weeks') else ''))
    d = os.path.join(topic, 'labs')
    for n in sorted(os.listdir(d)) if os.path.isdir(d) else []:
        p = os.path.join(d, n)
        if not os.path.isdir(p):
            continue
        lab = rjson(os.path.join(p, 'lab', 'lab.json'))
        if not lab:
            problems.append(f'{os.path.relpath(p, ROOT)}: no lab/lab.json (build the lab with the lab-manual template)'); continue
        man = os.path.exists(os.path.join(p, 'lab', lab.get('manual') or 'manual.pdf'))
        if not man:
            problems.append(f'{os.path.relpath(p, ROOT)}: manual PDF not built yet (tools/build.py)')
        add('Lab', lab.get('title', n), os.path.join(p, 'lab'), f"{len(lab.get('steps', []))} steps" + (', quiz' if (lab.get('quiz') or {}).get('questions') else '') + ('' if man else ', **no manual PDF**'), man)
    d = os.path.join(topic, 'projects')
    for n in sorted(os.listdir(d)) if os.path.isdir(d) else []:
        p = os.path.join(d, n)
        if not os.path.isdir(p):
            continue
        pj = rjson(os.path.join(p, 'project', 'project.json'))
        if not pj:
            problems.append(f'{os.path.relpath(p, ROOT)}: no project/project.json (run brief2project.py)')
            add('Project brief', n, p, 'brief only — not converted for the app', False); continue
        add('Project', pj.get('title', n), os.path.join(p, 'project'), f"{pj.get('category', '')}, {pj.get('durationWeeks', len(pj.get('weeks', [])))} weeks")
    d = os.path.join(topic, 'lectures')
    for n in sorted(os.listdir(d)) if os.path.isdir(d) else []:
        p = os.path.join(d, n)
        if os.path.isfile(p) and re.search(r'\.(md|markdown|pdf)$', n, re.I):
            t = n
            if n.lower().endswith(('.md', '.markdown')):
                m = re.search(r'^#\s+(.+)$', open(p, encoding='utf-8', errors='ignore').read(), re.M)
                t = m.group(1).strip() if m else n
            add('Lecture', t, p, 'PDF' if n.lower().endswith('.pdf') else 'Markdown')
        elif os.path.isdir(p):
            mds = [f for f in sorted(os.listdir(p)) if f.lower().endswith(('.md', '.markdown'))]
            if mds:
                m = re.search(r'^#\s+(.+)$', open(os.path.join(p, mds[0]), encoding='utf-8', errors='ignore').read(), re.M)
                add('Lecture', m.group(1).strip() if m else n, os.path.join(p, mds[0]), 'Markdown + images')
    d = os.path.join(topic, 'videos')
    for n in sorted(os.listdir(d)) if os.path.isdir(d) else []:
        p = os.path.join(d, n)
        if re.search(r'\.(mp4|m4v|webm)$', n, re.I):
            add('Video', n, p, f'{os.path.getsize(p) // 1048576} MB')
        elif n == 'links.md':
            k = len(re.findall(r'https?://', open(p, encoding='utf-8').read()))
            add('Video links', 'Online videos', p, f'{k} links')
    d = os.path.join(topic, 'materials')
    for n in sorted(os.listdir(d)) if os.path.isdir(d) else []:
        if n.startswith('.'):
            continue
        p = os.path.join(d, n)
        add('Material', n, p, 'folder' if os.path.isdir(p) else f'{max(1, os.path.getsize(p) // 1024)} KB')
    return items


def table(items, link_base=''):
    if not items:
        return '_No materials yet._'
    rows = ['| Type | Title | Path | Info | In packages |', '|---|---|---|---|---|']
    for i in items:
        rows.append(f"| {i['kind']} | {i['title']} | `{link_base}{i['path']}` | {i['info']} | {', '.join(i['used']) or '—'} |")
    return '\n'.join(rows)


MATERIALS = """## Materials

| Folder | What goes in | Made with |
|---|---|---|
| `lectures/` | lecture notes and readings (Markdown with images, or PDF) | by hand / any PDF template |
| `trainings/` | interactive web trainings, one folder each | `academy-templates:training` |
| `labs/` | labs: manual PDF + app lab (`lab/`), one folder each | `academy-templates:lab-manual` |
| `projects/` | project briefs + app projects (`project/`) | `academy-templates:project-brief` (+ `brief2project.py`) |
| `videos/` | `.mp4` (H.264 + AAC) / `.webm`, or `links.md` with online videos | — |
| `materials/` | starter files, constraints, datasheets, templates | — |

Name every material folder `<topic>-<short-name>` (e.g. `fpga-vivado-flow`); it becomes its id in packages.

## Inventory

<!-- inventory:start -->
_No materials yet._
<!-- inventory:end -->
"""


def init(rel):
    t = os.path.join(ROOT, rel)
    if not os.path.isdir(t):
        sys.exit(f'no topic folder {rel}')
    subs = [d for d in os.listdir(t) if os.path.isdir(os.path.join(t, d)) and d not in TYPES and not d.startswith('.')]
    if subs:
        sys.exit(f'{rel} has sub-topics ({", ".join(sorted(subs))}) — material folders go only at the last level')
    for d in TYPES:
        os.makedirs(os.path.join(t, d), exist_ok=True)
    rd = os.path.join(t, 'README.md')
    s = open(rd, encoding='utf-8').read() if os.path.exists(rd) else f'# {os.path.basename(t)}\n\n'
    s = re.sub(r'_Hierarchy not final yet\..*?_\n\n?', '', s, flags=re.S)
    if '<!-- inventory:start -->' not in s:
        m = re.search(r'\nSee \[', s)
        s = s[:m.start() + 1] + MATERIALS + '\n' + s[m.start() + 1:] if m else s.rstrip() + '\n\n' + MATERIALS
    open(rd, 'w', encoding='utf-8').write(s)
    print(f'{rel}: material folders added ({", ".join(TYPES)})')


def main():
    if '--init' in sys.argv:
        i = sys.argv.index('--init')
        if i + 1 >= len(sys.argv):
            sys.exit('usage: inventory.py --init <topic path>')
        init(sys.argv[i + 1])
    check = '--check' in sys.argv
    srcs, problems, allrows = package_sources(), [], []
    for t in topics():
        items = scan(t, srcs, problems)
        relt = os.path.relpath(t, ROOT)
        allrows.append((relt, items))
        rd = os.path.join(t, 'README.md')
        if not check and os.path.exists(rd):
            s = open(rd, encoding='utf-8').read()
            s2 = re.sub(r'(<!-- inventory:start -->\n).*?(\n<!-- inventory:end -->)', lambda m: m.group(1) + table(items) + m.group(2), s, flags=re.S)
            if s2 != s:
                open(rd, 'w', encoding='utf-8').write(s2)
        for i in items:
            if not i['used'] and i['kind'] in ('Training', 'Lab', 'Project', 'Lecture'):
                problems.append(f"{relt}/{i['path']}: not in any package yet")
    total = sum(len(i) for _, i in allrows)
    if not check:
        lines = ['# Inventory of learning materials', '', f'{total} materials in {len(allrows)} topics. Generated by `python3 tools/inventory.py` — do not edit by hand.', '']
        for relt, items in allrows:
            lines += [f'## {relt}', '', table(items, relt + '/'), '']
        open(os.path.join(ROOT, 'docs', 'INVENTORY.md'), 'w', encoding='utf-8').write('\n'.join(lines))
    by = {}
    for _, items in allrows:
        for i in items:
            by[i['kind']] = by.get(i['kind'], 0) + 1
    print(f"{total} materials in {len(allrows)} topics" + (': ' + ', '.join(f'{v} {k.lower()}' for k, v in sorted(by.items())) if by else ''))
    for p in problems:
        print('  ⚠ ' + p)
    if not check:
        print('updated docs/INVENTORY.md and the Inventory section of each topic README')


if __name__ == '__main__':
    main()
