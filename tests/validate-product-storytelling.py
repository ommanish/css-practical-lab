from pathlib import Path
import re,sys
ROOT=Path(__file__).resolve().parents[1]; BASE=ROOT/'components'/'product-storytelling'
COMPONENTS=['announcement-bar','hero-product-marquee','solution-card-grid','capability-tabs','numbered-feature-grid','logo-marquee','customer-story-gallery','analyst-proof-cards','community-promo','integration-card-grid','resource-grid','conversion-cta','faq-accordion']
OLD_EXAMPLES=['animated-gradient-border','css-card-reveal','staggered-text-reveal','word-swap-headline','typewriter-cursor','gradient-text-shimmer','magnetic-tilt-card','morphing-button-states','smooth-accordion-reveal','animated-nav-indicator','clip-path-image-reveal','view-transition-api','infinite-marquee','sticky-scroll-layout','scroll-progress','scroll-content-reveal','sticky-storytelling','horizontal-scroll-gallery','parallax-depth','scroll-snap-carousel','autoplay-carousel','stacked-card-rotator','coverflow-carousel','full-page-section-slider','overlapping-grid','container-query-cards','has-selector-interaction']
FORBIDDEN=['Salesforce','Data 360','Agentforce','Dreamforce','Forrester','Gartner','Snowflake','Databricks']; errors=[]
def fail(x): errors.append(x)
def read(p): return p.read_text() if p.exists() else ''
def scan(t,label):
 for w in FORBIDDEN:
  if re.search(re.escape(w),t,re.I): fail(f'{label}: forbidden brand string {w}')
def prompt(t,label):
 for x in ['Vibe Coding Prompt','data-prompt','data-prompt-text','data-copy-prompt']:
  if x not in t: fail(f'{label}: missing {x}')
def component(slug):
 d=BASE/slug; h=d/'index.html'; c=d/'style.css'
 if not d.exists(): fail(f'missing component directory: {slug}'); return '',''
 if not h.exists(): fail(f'{slug}: missing index.html')
 if not c.exists(): fail(f'{slug}: missing style.css')
 ht,ct=read(h),read(c); prompt(ht,slug); scan(ht,slug); scan(ct,slug)
 if f'components/product-storytelling/{slug}' not in ht: fail(f'{slug}: source link does not point to its component directory')
 if ('animation:' in ct or 'transition:' in ct or '@keyframes' in ct) and 'prefers-reduced-motion' not in ct: fail(f'{slug}: missing reduced-motion handling')
 ext=[u for u in re.findall(r'https?://[^\"\'\s<>]+',ht) if 'github.com/ommanish/css-practical-lab' not in u]
 if ext: fail(f'{slug}: external required asset/link dependency {ext[0]}')
 return ht,ct
t={s:component(s) for s in COMPONENTS}
# Intro group
if 'announcement__message' not in t['announcement-bar'][0] or 'announcement__cta' not in t['announcement-bar'][0]: fail('announcement-bar: missing message or CTA')
if ':focus-visible' not in t['announcement-bar'][1]: fail('announcement-bar: missing focus-visible treatment')
hero=t['hero-product-marquee'][0]
for x in ['class="eyebrow"','<h1','hero__copy','hero__actions','hero__visual']:
 if x not in hero: fail(f'hero-product-marquee: missing {x}')
if hero.count('class="button')<2: fail('hero-product-marquee: needs two CTAs')
if t['solution-card-grid'][0].count('class="solution-card"')!=6: fail('solution-card-grid: expected 6 cards')
sg=t['solution-card-grid'][1].replace(' ','')
for x in ['repeat(3','repeat(2','grid-template-columns:1fr']:
 if x not in sg: fail(f'solution-card-grid: missing responsive rule {x}')
# Stateful depth
ct=t['capability-tabs'][0]
if 'role="tablist"' not in ct or ct.count('role="tab"')<3 or ct.count('role="tabpanel"')<3 or ct.count('aria-selected="true"')!=1: fail('capability-tabs: incomplete ARIA structure')
if not (BASE/'capability-tabs'/'script.js').exists(): fail('capability-tabs: missing script.js')
for n in ['01','02','03','04']:
 if f'>{n}<' not in t['numbered-feature-grid'][0]: fail(f'numbered-feature-grid: missing {n}')
# Trust/stories
if t['logo-marquee'][0].count('class="marquee__set"')<2 or ':focus-within' not in t['logo-marquee'][1]: fail('logo-marquee: incomplete repeated/pause behavior')
st=t['customer-story-gallery'][0]
if len(re.findall(r'class="story-card(?:\s|\")',st))<4 or 'scroll-snap-type' not in t['customer-story-gallery'][1]: fail('customer-story-gallery: incomplete gallery')
for x in ['Previous story','Next story']:
 if x not in st: fail(f'customer-story-gallery: missing {x}')
# Proof/promo/integrations
if len(re.findall(r'class="proof-card(?:\s|\")',t['analyst-proof-cards'][0]))!=2: fail('analyst-proof-cards: expected 2 cards')
for x in ['promo__visual','promo__eyebrow','promo__body','promo__cta']:
 if x not in t['community-promo'][0]: fail(f'community-promo: missing {x}')
it=t['integration-card-grid'][0]
if len(re.findall(r'class="integration-card(?:\s|\")',it))!=4 or len(set(re.findall(r'data-symbol="([^"]+)"',it)))!=4: fail('integration-card-grid: expected 4 unique cards')
# Resources/conversion/FAQ
if len(re.findall(r'class="resource-card(?:\s|\")',t['resource-grid'][0]))<4 or t['resource-grid'][0].count('resource-card__type')<4: fail('resource-grid: expected 4 typed resources')
if len(re.findall(r'class="conversion-card(?:\s|\")',t['conversion-cta'][0]))!=2: fail('conversion-cta: expected 2 actions')
fh,fc=t['faq-accordion']
if fh.count('aria-expanded=')<5 or 'faq__icon' not in fh or '.faq__icon::before' not in fc or '.faq__icon::after' not in fc: fail('faq-accordion: incomplete controls/icon')
r=re.search(r'\.faq__icon\{([^}]*)\}',fc)
if r and re.search(r'(^|;)\s*transform\s*:',r.group(1)): fail('faq-accordion: icon container must not transform')
# Complete page
full=ROOT/'examples'/'enterprise-product-overview'
for name in ['index.html','style.css','script.js']:
 if not (full/name).exists(): fail(f'enterprise-product-overview: missing {name}')
ft,fcss,fjs=read(full/'index.html'),read(full/'style.css'),read(full/'script.js')
if ft:
 prompt(ft,'enterprise-product-overview'); scan(ft,'enterprise-product-overview')
 hooks=['announcement','hero','solutions','capabilities','features','trust','stories','proof','promo','integrations','resources','conversion','faq']; pos=[ft.find(f'data-section="{x}"') for x in hooks]
 for x,p in zip(hooks,pos):
  if p<0: fail(f'enterprise-product-overview: missing section {x}')
 if all(p>=0 for p in pos) and pos!=sorted(pos): fail('enterprise-product-overview: incorrect section order')
 if len(re.findall(r'<h1(?:\s|>)',ft))!=1: fail('enterprise-product-overview: expected exactly one h1')
 if 'examples/enterprise-product-overview' not in ft: fail('enterprise-product-overview: incorrect source link')
scan(fcss,'enterprise-product-overview CSS'); scan(fjs,'enterprise-product-overview JS')
if fcss and 'prefers-reduced-motion' not in fcss: fail('enterprise-product-overview: missing reduced-motion styles')
# Homepage + README regression guard
home=read(ROOT/'index.html'); md=read(ROOT/'README.md')
if not home: fail('homepage: missing index.html')
else:
 if 'examples/enterprise-product-overview/' not in home or 'Product Storytelling System' not in home: fail('homepage: missing product storytelling system')
 if '<strong>28</strong><span>Examples</span>' not in home: fail('homepage: example count must be 28')
 for slug in OLD_EXAMPLES:
  if f'examples/{slug}/' not in home: fail(f'homepage regression: missing existing example {slug}')
if not md: fail('README: missing README.md')
else:
 if 'enterprise-product-overview' not in md: fail('README: missing complete page')
 for slug in COMPONENTS:
  if f'components/product-storytelling/{slug}/' not in md: fail(f'README: missing {slug}')
if errors:
 print('FAIL');print('\n'.join(errors));sys.exit(1)
print('PASS: product storytelling acceptance checks')