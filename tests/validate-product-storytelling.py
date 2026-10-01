from pathlib import Path
import re, sys
ROOT = Path(__file__).resolve().parents[1]
COMPONENTS = [
'announcement-bar','hero-product-marquee','solution-card-grid','capability-tabs','numbered-feature-grid','logo-marquee','customer-story-gallery','analyst-proof-cards','community-promo','integration-card-grid','resource-grid','conversion-cta','faq-accordion']
FORBIDDEN = ['Salesforce','Data 360','Agentforce','Dreamforce','Forrester','Gartner','Snowflake','Databricks']
errors=[]
def check_prompt(text, label):
    for s in ['Vibe Coding Prompt','data-prompt','data-prompt-text','data-copy-prompt']:
        if s not in text: errors.append(f'{label}: missing {s}')
def scan_forbidden(text,label):
    for s in FORBIDDEN:
        if re.search(re.escape(s), text, re.I): errors.append(f'{label}: forbidden brand string {s}')
def check_component(slug):
    d=ROOT/'components'/'product-storytelling'/slug
    if not d.exists(): errors.append(f'missing component directory: {slug}'); return
    html=d/'index.html'; css=d/'style.css'
    if not html.exists(): errors.append(f'{slug}: missing index.html'); return
    if not css.exists(): errors.append(f'{slug}: missing style.css'); return
    ht=html.read_text(); ct=css.read_text(); check_prompt(ht,slug); scan_forbidden(ht,slug); scan_forbidden(ct,slug)
    if 'http://' in ht or 'https://' in ht:
        external=[u for u in re.findall(r'https?://[^\"\'\s<>]+',ht) if 'github.com/ommanish/css-practical-lab' not in u]
        if external: errors.append(f'{slug}: external required asset/link dependency {external[0]}')
    if ('animation:' in ct or 'transition:' in ct or '@keyframes' in ct) and 'prefers-reduced-motion' not in ct:
        errors.append(f'{slug}: missing reduced-motion handling')
for c in COMPONENTS: check_component(c)

def task2_checks():
    base=ROOT/'components'/'product-storytelling'
    a=base/'announcement-bar'/'index.html'
    if a.exists():
        t=a.read_text()
        if 'class="announcement__message"' not in t: errors.append('announcement-bar: missing message')
        if 'class="announcement__cta"' not in t: errors.append('announcement-bar: missing inline CTA')
        css=(base/'announcement-bar'/'style.css').read_text() if (base/'announcement-bar'/'style.css').exists() else ''
        if ':focus-visible' not in css: errors.append('announcement-bar: missing focus-visible CTA treatment')
    h=base/'hero-product-marquee'/'index.html'
    if h.exists():
        t=h.read_text()
        for token in ['class="eyebrow"','<h1','class="hero__copy"','class="hero__actions"','class="hero__visual"']:
            if token not in t: errors.append(f'hero-product-marquee: missing {token}')
        if t.count('class="button') < 2: errors.append('hero-product-marquee: needs two CTAs')
    g=base/'solution-card-grid'/'index.html'
    if g.exists():
        t=g.read_text(); css=(base/'solution-card-grid'/'style.css').read_text() if (base/'solution-card-grid'/'style.css').exists() else ''
        if t.count('class="solution-card"') != 6: errors.append('solution-card-grid: expected 6 cards')
        for token in ['repeat(3','repeat(2','grid-template-columns:1fr']:
            if token not in css.replace(' ', ''): errors.append(f'solution-card-grid: missing responsive rule {token}')
task2_checks()

def task3_checks():
    base=ROOT/'components'/'product-storytelling'
    tabs=base/'capability-tabs'/'index.html'
    if tabs.exists():
        t=tabs.read_text()
        if 'role="tablist"' not in t: errors.append('capability-tabs: missing tablist')
        if t.count('role="tab"') < 3: errors.append('capability-tabs: expected at least 3 tabs')
        if t.count('role="tabpanel"') < 3: errors.append('capability-tabs: expected matching panels')
        if t.count('aria-selected="true"') != 1: errors.append('capability-tabs: exactly one tab must start selected')
        if not (base/'capability-tabs'/'script.js').exists(): errors.append('capability-tabs: missing script.js')
    f=base/'numbered-feature-grid'/'index.html'
    if f.exists():
        t=f.read_text()
        for n in ['01','02','03','04']:
            if f'>{n}<' not in t: errors.append(f'numbered-feature-grid: missing {n}')
task3_checks()

full=ROOT/'examples'/'enterprise-product-overview'
if not full.exists(): errors.append('missing full-page example: enterprise-product-overview')
else:
    for f in ['index.html','style.css','script.js']:
        if not (full/f).exists(): errors.append(f'enterprise-product-overview: missing {f}')
    if (full/'index.html').exists(): check_prompt((full/'index.html').read_text(),'enterprise-product-overview')
if errors:
    print('FAIL')
    print('\n'.join(errors))
    sys.exit(1)
print('PASS: product storytelling acceptance checks')
