from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
base=ROOT/'examples'/'enterprise-product-overview'
css=base/'scroll-motion.css'
js=base/'script.js'
errors=[]
if not css.exists(): errors.append('missing scroll-motion.css')
ct=css.read_text() if css.exists() else ''
jt=js.read_text() if js.exists() else ''
for token in ['IntersectionObserver','motion-reveal','is-visible','--motion-delay','scroll-motion.css','page-load-curtain']:
    if token not in jt and token not in ct: errors.append(f'missing motion token: {token}')
for token in ['.motion-reveal','.motion-reveal.is-visible','.motion-media-target','.page-load-curtain','prefers-reduced-motion']:
    if token not in ct: errors.append(f'missing CSS behavior: {token}')
if errors:
    print('FAIL')
    print('\n'.join(errors))
    sys.exit(1)
print('PASS: enterprise scroll motion checks')
