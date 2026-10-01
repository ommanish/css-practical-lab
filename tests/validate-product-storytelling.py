from pathlib import Path
import re,sys
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'components'/'product-storytelling'
COMPONENTS=['announcement-bar','hero-product-marquee','solution-card-grid','capability-tabs','numbered-feature-grid','logo-marquee','customer-story-gallery','analyst-proof-cards','community-promo','integration-card-grid','resource-grid','conversion-cta','faq-accordion']
FORBIDDEN=['Salesforce','Data 360','Agentforce','Dreamforce','Forrester','Gartner','Snowflake','Databricks']
errors=[]
def fail(msg): errors.append(msg)
def scan(text,label):
 for word in FORBIDDEN:
  if re.search(re.escape(word),text,re.I): fail(f'{label}: forbidden brand string {word}')
def prompt(text,label):
 for token in ['Vibe Coding Prompt','data-prompt','data-prompt-text','data-copy-prompt']:
  if token not in text: fail(f'{label}: missing {token}')
def read(path): return path.read_text() if path.exists() else ''
def component(slug):
 d=BASE/slug; h=d/'index.html'; c=d/'style.css'
 if not d.exists(): fail(f'missing component directory: {slug}'); return '',''
 if not h.exists(): fail(f'{slug}: missing index.html')
 if not c.exists(): fail(f'{slug}: missing style.css')
 ht,ct=read(h),read(c); prompt(ht,slug); scan(ht,slug); scan(ct,slug)
 if ('animation:' in ct or 'transition:' in ct or '@keyframes' in ct) and 'prefers-reduced-motion' not in ct: fail(f'{slug}: missing reduced-motion handling')
 external=[u for u in re.findall(r'https?://[^\"\'\s<>]+',ht) if 'github.com/ommanish/css-practical-lab' not in u]
 if external: fail(f'{slug}: external required asset/link dependency {external[0]}')
 return ht,ct
texts={s:component(s) for s in COMPONENTS}
# intro system
if 'announcement__message' not in texts['announcement-bar'][0] or 'announcement__cta' not in texts['announcement-bar'][0]: fail('announcement-bar: missing message or CTA')
if ':focus-visible' not in texts['announcement-bar'][1]: fail('announcement-bar: missing focus-visible treatment')
hero=texts['hero-product-marquee'][0]
for token in ['class="eyebrow"','<h1','hero__copy','hero__actions','hero__visual']:
 if token not in hero: fail(f'hero-product-marquee: missing {token}')
if hero.count('class="button')<2: fail('hero-product-marquee: needs two CTAs')
if texts['solution-card-grid'][0].count('class="solution-card"')!=6: fail('solution-card-grid: expected 6 cards')
css=texts['solution-card-grid'][1].replace(' ','')
for token in ['repeat(3','repeat(2','grid-template-columns:1fr']:
 if token not in css: fail(f'solution-card-grid: missing responsive rule {token}')
# tabs + numbered features
tabs=texts['capability-tabs'][0]
if 'role="tablist"' not in tabs or tabs.count('role="tab"')<3 or tabs.count('role="tabpanel"')<3: fail('capability-tabs: incomplete ARIA structure')
if tabs.count('aria-selected="true"')!=1: fail('capability-tabs: exactly one initial selected tab required')
if not (BASE/'capability-tabs'/'script.js').exists(): fail('capability-tabs: missing script.js')
for n in ['01','02','03','04']:
 if f'>{n}<' not in texts['numbered-feature-grid'][0]: fail(f'numbered-feature-grid: missing {n}')
# trust + story gallery
if texts['logo-marquee'][0].count('class="marquee__set"')<2: fail('logo-marquee: needs two repeated sets')
if ':hover' not in texts['logo-marquee'][1] or ':focus-within' not in texts['logo-marquee'][1]: fail('logo-marquee: missing pause states')
story=texts['customer-story-gallery'][0]
if len(re.findall(r'class="story-card(?:\s|\")',story))<4 or 'scroll-snap-type' not in texts['customer-story-gallery'][1]: fail('customer-story-gallery: incomplete gallery')
for label in ['Previous story','Next story']:
 if label not in story: fail(f'customer-story-gallery: missing {label}')
# proof/promo/integrations
if len(re.findall(r'class="proof-card(?:\s|\")',texts['analyst-proof-cards'][0]))!=2: fail('analyst-proof-cards: expected 2 cards')
for token in ['promo__visual','promo__eyebrow','promo__body','promo__cta']:
 if token not in texts['community-promo'][0]: fail(f'community-promo: missing {token}')
integ=texts['integration-card-grid'][0]
if len(re.findall(r'class="integration-card(?:\s|\")',integ))!=4 or len(set(re.findall(r'data-symbol="([^"]+)"',integ)))!=4: fail('integration-card-grid: expected 4 uniquely illustrated cards')
# resources/conversion/faq
if len(re.findall(r'class="resource-card(?:\s|\")',texts['resource-grid'][0]))<4 or texts['resource-grid'][0].count('resource-card__type')<4: fail('resource-grid: expected 4 typed resources')
if len(re.findall(r'class="conversion-card(?:\s|\")',texts['conversion-cta'][0]))!=2: fail('conversion-cta: expected 2 actions')
faq=texts['faq-accordion'][0]; faqcss=texts['faq-accordion'][1]
if faq.count('aria-expanded=')<5 or 'faq__icon' not in faq: fail('faq-accordion: incomplete accessible controls')
if '.faq__icon::before' not in faqcss or '.faq__icon::after' not in faqcss: fail('faq-accordion: glyph must use pseudo-elements')
base_rule=re.search(r'\.faq__icon\{([^}]*)\}',faqcss)
if base_rule and re.search(r'(^|;)\s*transform\s*:',base_rule.group(1)): fail('faq-accordion: icon container must not transform')
# complete page
full=ROOT/'examples'/'enterprise-product-overview'
for name in ['index.html','style.css','script.js']:
 if not (full/name).exists(): fail(f'enterprise-product-overview: missing {name}')
ft,fc,fj=read(full/'index.html'),read(full/'style.css'),read(full/'script.js')
if ft:
 prompt(ft,'enterprise-product-overview'); scan(ft,'enterprise-product-overview')
 hooks=['announcement','hero','solutions','capabilities','features','trust','stories','proof','promo','integrations','resources','conversion','faq']
 positions=[ft.find(f'data-section="{h}"') for h in hooks]
 for h,p in zip(hooks,positions):
  if p<0: fail(f'enterprise-product-overview: missing section {h}')
 if all(p>=0 for p in positions) and positions!=sorted(positions): fail('enterprise-product-overview: incorrect section order')
 if len(re.findall(r'<h1(?:\s|>)',ft))!=1: fail('enterprise-product-overview: expected exactly one h1')
scan(fc,'enterprise-product-overview CSS'); scan(fj,'enterprise-product-overview JS')
if fc and 'prefers-reduced-motion' not in fc: fail('enterprise-product-overview: missing reduced-motion styles')
if errors:
 print('FAIL'); print('\n'.join(errors)); sys.exit(1)
print('PASS: product storytelling acceptance checks')
