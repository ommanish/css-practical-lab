from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "examples" / "enterprise-product-overview"
SCRIPT = (PAGE / "script.js").read_text()
MOTION = (PAGE / "scroll-motion.css").read_text()

errors = []

if "['.trust-track','']" in SCRIPT or '[".trust-track",""]' in SCRIPT:
    errors.append("trust marquee track must not receive motion-reveal because it cancels its own animation")

if "['.trust','']" not in SCRIPT and '[".trust",""]' not in SCRIPT:
    errors.append("trust section should receive the one-time viewport reveal instead of the marquee track")

if "document.startViewTransition" in SCRIPT:
    errors.append("capability tabs must not use a document-level View Transition")

if "tab-panel-enter" not in MOTION:
    errors.append("capability tabs need a local panel-enter animation")

if ".trust-track.motion-reveal" in MOTION:
    errors.append("scroll motion CSS must not override the trust-track transform/animation")

if "prefers-reduced-motion" not in MOTION or ".cap-panels article{animation:none!important}" not in MOTION:
    errors.append("local tab panel motion must be disabled for reduced-motion users")

if errors:
    print("FAIL")
    print("\n".join(errors))
    raise SystemExit(1)

print("PASS: product overview motion regression checks")
