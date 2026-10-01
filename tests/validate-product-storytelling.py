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
