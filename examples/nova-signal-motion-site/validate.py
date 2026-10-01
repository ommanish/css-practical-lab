from pathlib import Path
import re, sys
root=Path(__file__).parent
html=(root/'index.html').read_text()
css=(root/'style.css').read_text()
js=(root/'motion.js').read_text()
errors=[]
for f in ['style.css','motion.js']:
    if not (root/f).exists(): errors.append(f'missing {f}')
for sec in ['top','product','capabilities','system','story','final-cta','resources']:
    if f'id="{sec}"' not in html: errors.append(f'missing section {sec}')
if html.count('<h1') != 1: errors.append('expected exactly one h1')
for key in ['observe','understand','act']:
    if f'data-capability="{key}"' not in html: errors.append(f'missing capability {key}')
for key in ['signal','context','decision','action']:
    if f'data-flow-step="{key}"' not in html: errors.append(f'missing flow step {key}')
for key in ['anomaly','impact','response']:
    if f'data-story-beat="{key}"' not in html: errors.append(f'missing story beat {key}')
if 'prefers-reduced-motion:reduce' not in css.replace(' ',''): errors.append('missing reduced motion css')
if ':focus-visible' not in css: errors.append('missing focus visible')
if 'gsap.registerPlugin(ScrollTrigger)' not in js: errors.append('missing gsap registration')
if js.count('pin:') != 2: errors.append(f'expected exactly two pin timelines, got {js.count("pin:")}')
if '.mobile-nav' not in css or 'details class="mobile-nav"' not in html: errors.append('missing mobile nav')
imgs=re.findall(r'<img\b[^>]*>',html)
for tag in imgs:
    if 'alt=' not in tag: errors.append('image missing alt')
assets=set(re.findall(r'assets/[\w-]+\.webp',html))
for a in assets:
    if not (root/a).exists(): errors.append(f'missing asset {a}')
if len(assets) != 5: errors.append(f'expected 5 optimized asset refs, got {len(assets)}')
if errors:
    print('FAIL')
    print('\n'.join(errors)); sys.exit(1)
print('PASS: NOVA local acceptance checks')
