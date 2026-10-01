# Product Storytelling System Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build 13 standalone enterprise-product storytelling components plus one complete responsive product-overview example inside `css-practical-lab`, using original content/visuals and native CSS-first motion.

**Architecture:** Each standalone component lives under `components/product-storytelling/<component>/` and is independently runnable with its own `index.html`, `style.css`, and `script.js` only where state is required. A separate `examples/enterprise-product-overview/` page re-implements the same patterns in one cohesive composition so the standalone examples remain copyable rather than tightly coupled. A single stdlib Python validator pins structure, accessibility hooks, prompt presence, source links, reduced-motion coverage, and regression safety across the new system.

**Tech Stack:** HTML5, CSS, minimal vanilla JavaScript, CSS Scroll-Driven Animations where appropriate, View Transition API as progressive enhancement, Python stdlib validation, GitHub Pages.

**Spec:** `docs/superpowers/specs/2026-09-30-product-storytelling-system-design.md`

## Global Constraints

- No Salesforce copy, logos, images, customer names, product names, proprietary graphics, or proprietary Page Builder code.
- Original deep-ink / warm-off-white visual system with electric lime primary accent and violet/cyan secondary accents.
- Framework-free; no package manager, build step, runtime dependency, GSAP, Framer Motion, Swiper, or animation library.
- CSS first; JavaScript only for stateful interactions that CSS cannot provide reliably.
- Every animated experience must support `prefers-reduced-motion: reduce`.
- Interactive controls must be keyboard usable with visible focus styles and correct ARIA semantics.
- All layouts must work from 320px through large desktop widths with no horizontal page overflow.
- Every standalone component and the complete page must expose a visible Vibe Coding Prompt and Copy Prompt control using the existing lab prompt UI.
- Existing 27 demos must not be rewritten or behaviorally changed by this feature.

## Review Focus

1. **320px mobile width:** no component or full-page section may force horizontal overflow; pinned by the structural validator and browser-width audit in Tasks 7 and 8.
2. **Reduced motion:** every component with continuous or entrance motion must become static or instant without losing information; pinned by CSS token checks in Tasks 2–6 and final audit in Task 8.
3. **Keyboard stateful controls:** tabs, gallery controls, and FAQ must remain usable without a pointer and expose correct state; pinned by DOM/ARIA assertions plus browser keyboard checks in Tasks 3, 4, and 6.
4. **Independent copyability:** standalone components must not depend on files from sibling component folders; pinned by relative-asset validation in Task 7.
5. **Originality boundary:** no forbidden Salesforce names/brand strings may enter source; pinned by forbidden-string scans in Tasks 2–8.

---

### Task 1: Add the Product Storytelling Validation Harness

**Files:**
- Create: `tests/validate-product-storytelling.py`

**Interfaces:**
- Consumes: the design spec component names and required file layout.
- Produces: one executable validation command, `python3 tests/validate-product-storytelling.py`, that later tasks extend by satisfying its assertions.

- [ ] **Step 1: Write the failing validator**

The validator must assert these future paths exist:
`components/product-storytelling/announcement-bar/`, `hero-product-marquee/`, `solution-card-grid/`, `capability-tabs/`, `numbered-feature-grid/`, `logo-marquee/`, `customer-story-gallery/`, `analyst-proof-cards/`, `community-promo/`, `integration-card-grid/`, `resource-grid/`, `conversion-cta/`, `faq-accordion/`, and `examples/enterprise-product-overview/`.

It must also define reusable assertions for:
- `index.html` and `style.css` presence
- visible `Vibe Coding Prompt`
- `data-prompt`, `data-prompt-text`, and `data-copy-prompt`
- `prefers-reduced-motion` in animated component CSS
- no forbidden brand strings: `Salesforce`, `Data 360`, `Agentforce`, `Dreamforce`, `Forrester`, `Gartner`, `Snowflake`, `Databricks`
- no absolute external asset dependency for required visuals

- [ ] **Step 2: Run the validator to verify RED**

Run: `python3 tests/validate-product-storytelling.py`

Expected: FAIL because the 13 component directories and full-page example do not exist yet.

- [ ] **Step 3: Commit the failing validator**

```bash
git add tests/validate-product-storytelling.py
git commit -m "test: define product storytelling acceptance checks"
```

### Task 2: Build Announcement Bar, Product Hero, and Solution Card Grid

**Files:**
- Create: `components/product-storytelling/announcement-bar/index.html`
- Create: `components/product-storytelling/announcement-bar/style.css`
- Create: `components/product-storytelling/hero-product-marquee/index.html`
- Create: `components/product-storytelling/hero-product-marquee/style.css`
- Create: `components/product-storytelling/solution-card-grid/index.html`
- Create: `components/product-storytelling/solution-card-grid/style.css`

**Interfaces:**
- Consumes: existing root `prompt.css` and `prompt.js` only for prompt UI behavior.
- Produces: three independent standalone component examples with original CSS/SVG artwork and no stateful JS.

- [ ] **Step 1: Extend the validator with component-specific failing assertions**

Assert:
- announcement bar has message, inline CTA, and focus-visible CTA treatment
- hero has eyebrow, `h1`, supporting copy, two CTAs, and an abstract visual container
- solution grid contains 6 cards and responsive 3/2/1-column rules
- all three include prompt UI and reduced-motion rules where animation exists

- [ ] **Step 2: Run validator to verify RED**

Run: `python3 tests/validate-product-storytelling.py`

Expected: FAIL on these three component assertions.

- [ ] **Step 3: Implement the three components**

Use only original fictional copy. Keep hero motion to staggered text plus slow ambient transform/opacity effects. Keep solution-card motion to restrained reveal/hover transforms.

- [ ] **Step 4: Run validator to verify GREEN for Task 2**

Run: `python3 tests/validate-product-storytelling.py`

Expected: Task 2 assertions pass; remaining future-component assertions still fail.

- [ ] **Step 5: Commit**

```bash
git add components/product-storytelling/announcement-bar components/product-storytelling/hero-product-marquee components/product-storytelling/solution-card-grid tests/validate-product-storytelling.py
git commit -m "feat: add product intro storytelling components"
```

### Task 3: Build Capability Tabs and Numbered Feature Grid

**Files:**
- Create: `components/product-storytelling/capability-tabs/index.html`
- Create: `components/product-storytelling/capability-tabs/style.css`
- Create: `components/product-storytelling/capability-tabs/script.js`
- Create: `components/product-storytelling/numbered-feature-grid/index.html`
- Create: `components/product-storytelling/numbered-feature-grid/style.css`

**Interfaces:**
- Consumes: root prompt UI assets.
- Produces: keyboard-accessible ARIA tabs and a 4-item numbered feature grid.

- [ ] **Step 1: Add failing validator assertions**

Assert capability tabs include:
- `role="tablist"`, at least 3 `role="tab"` controls, matching `role="tabpanel"` elements
- exactly one initial `aria-selected="true"`
- local `script.js`

Assert numbered feature grid includes 4 indexed items (`01`–`04`) and reduced-motion coverage.

- [ ] **Step 2: Run validator to verify RED**

Run: `python3 tests/validate-product-storytelling.py`

Expected: FAIL for Task 3 paths/semantics.

- [ ] **Step 3: Implement capability tab behavior**

`script.js` must support click, ArrowLeft, ArrowRight, Home, and End; update `aria-selected`, `tabindex`, and panel visibility; focus the newly selected tab for keyboard navigation.

- [ ] **Step 4: Implement numbered feature grid**

Use original content with scroll/viewport reveal as progressive enhancement; content must remain visible if the newer animation feature is unsupported.

- [ ] **Step 5: Verify JS and validator**

Run:
```bash
node --check components/product-storytelling/capability-tabs/script.js
python3 tests/validate-product-storytelling.py
```

Expected: JS syntax passes and Task 3 assertions pass.

- [ ] **Step 6: Commit**

```bash
git add components/product-storytelling/capability-tabs components/product-storytelling/numbered-feature-grid tests/validate-product-storytelling.py
git commit -m "feat: add capability and feature components"
```

### Task 4: Build Trust Marquee and Customer Story Gallery

**Files:**
- Create: `components/product-storytelling/logo-marquee/index.html`
- Create: `components/product-storytelling/logo-marquee/style.css`
- Create: `components/product-storytelling/customer-story-gallery/index.html`
- Create: `components/product-storytelling/customer-story-gallery/style.css`
- Create: `components/product-storytelling/customer-story-gallery/script.js`

**Interfaces:**
- Consumes: root prompt UI assets.
- Produces: a pure-CSS looping trust rail and a native scroll-snap story gallery with optional previous/next controls.

- [ ] **Step 1: Add failing validator assertions**

Assert:
- marquee contains two repeated tracks/sets, pauses on hover/focus, and has reduced-motion static fallback
- gallery uses `scroll-snap-type`, includes at least 4 original story cards, and exposes previous/next buttons with accessible labels

- [ ] **Step 2: Run validator to verify RED**

Run: `python3 tests/validate-product-storytelling.py`

Expected: FAIL for Task 4 assertions.

- [ ] **Step 3: Implement the marquee**

Use generic original wordmarks/symbols only; no external logos or images.

- [ ] **Step 4: Implement gallery behavior**

Use native scrolling; JS only calls `scrollIntoView()` / `scrollBy()` for controls and must not replace touch/trackpad scrolling.

- [ ] **Step 5: Verify JS and validator**

Run:
```bash
node --check components/product-storytelling/customer-story-gallery/script.js
python3 tests/validate-product-storytelling.py
```

Expected: Task 4 assertions pass.

- [ ] **Step 6: Commit**

```bash
git add components/product-storytelling/logo-marquee components/product-storytelling/customer-story-gallery tests/validate-product-storytelling.py
git commit -m "feat: add trust and customer story components"
```

### Task 5: Build Proof Cards, Editorial Promo, and Integration Grid

**Files:**
- Create: `components/product-storytelling/analyst-proof-cards/index.html`
- Create: `components/product-storytelling/analyst-proof-cards/style.css`
- Create: `components/product-storytelling/community-promo/index.html`
- Create: `components/product-storytelling/community-promo/style.css`
- Create: `components/product-storytelling/integration-card-grid/index.html`
- Create: `components/product-storytelling/integration-card-grid/style.css`

**Interfaces:**
- Consumes: root prompt UI assets.
- Produces: two editorial proof cards, one high-impact promo blade, and a 4-card integration grid using original abstract marks.

- [ ] **Step 1: Add failing validator assertions**

Assert:
- proof area has exactly 2 major cards
- community promo has large visual + eyebrow + heading + body + CTA
- integration grid has exactly 4 cards with unique generic symbols
- all components include prompt UI and reduced-motion rules for animated effects

- [ ] **Step 2: Run validator to verify RED**

Run: `python3 tests/validate-product-storytelling.py`

Expected: FAIL for Task 5 assertions.

- [ ] **Step 3: Implement the three components**

Use transform/opacity-only hover and reveal motion where possible; community visual may use layered CSS/SVG shapes and subtle parallax.

- [ ] **Step 4: Run validator to verify GREEN for Task 5**

Run: `python3 tests/validate-product-storytelling.py`

Expected: Task 5 assertions pass.

- [ ] **Step 5: Commit**

```bash
git add components/product-storytelling/analyst-proof-cards components/product-storytelling/community-promo components/product-storytelling/integration-card-grid tests/validate-product-storytelling.py
git commit -m "feat: add proof promo and integration components"
```

### Task 6: Build Resource Grid, Conversion CTA, and FAQ Accordion

**Files:**
- Create: `components/product-storytelling/resource-grid/index.html`
- Create: `components/product-storytelling/resource-grid/style.css`
- Create: `components/product-storytelling/conversion-cta/index.html`
- Create: `components/product-storytelling/conversion-cta/style.css`
- Create: `components/product-storytelling/faq-accordion/index.html`
- Create: `components/product-storytelling/faq-accordion/style.css`
- Create: `components/product-storytelling/faq-accordion/script.js`

**Interfaces:**
- Consumes: root prompt UI assets.
- Produces: a 4-card resource section, 2-up conversion block, and accessible accordion.

- [ ] **Step 1: Add failing validator assertions**

Assert:
- resource grid has at least 4 resource cards and resource-type labels
- conversion area has exactly 2 primary actions
- FAQ has at least 5 buttons with `aria-expanded`
- FAQ icon container remains structurally separate from the `+ / ×` glyph so the circle itself is never rotated

- [ ] **Step 2: Run validator to verify RED**

Run: `python3 tests/validate-product-storytelling.py`

Expected: FAIL for Task 6 assertions.

- [ ] **Step 3: Implement resource and conversion components**

Use sequential reveal/hover zoom for resource art and directional hover states for the CTA blocks.

- [ ] **Step 4: Implement FAQ behavior**

Use CSS grid `0fr → 1fr` for panel animation, update `aria-expanded`, and draw the icon glyph with pseudo-elements inside a fixed-size circle.

- [ ] **Step 5: Verify JS and validator**

Run:
```bash
node --check components/product-storytelling/faq-accordion/script.js
python3 tests/validate-product-storytelling.py
```

Expected: all 13 standalone component assertions now pass; full-page example assertions still fail.

- [ ] **Step 6: Commit**

```bash
git add components/product-storytelling/resource-grid components/product-storytelling/conversion-cta components/product-storytelling/faq-accordion tests/validate-product-storytelling.py
git commit -m "feat: add resource conversion and faq components"
```

### Task 7: Assemble the Full Enterprise Product Overview Example

**Files:**
- Create: `examples/enterprise-product-overview/index.html`
- Create: `examples/enterprise-product-overview/style.css`
- Create: `examples/enterprise-product-overview/script.js`
- Modify: `tests/validate-product-storytelling.py`

**Interfaces:**
- Consumes: the visual/interaction patterns established by Tasks 2–6, but not their CSS files; the page owns its composed styles so it is directly portable.
- Produces: one direct-load GitHub Pages example containing all 13 sections in spec order.

- [ ] **Step 1: Add failing full-page assertions**

Assert the full page includes section hooks for all 13 patterns in the required order, one `h1`, semantic section headings, visible prompt UI, local `style.css`, local `script.js`, reduced-motion support, and no forbidden brand strings.

- [ ] **Step 2: Run validator to verify RED**

Run: `python3 tests/validate-product-storytelling.py`

Expected: FAIL because the full-page example is not built.

- [ ] **Step 3: Implement full-page HTML and visual composition**

Use original fictional product positioning and CSS/SVG visuals. Preserve the pacing: announcement → hero → solutions → tabs/features → trust → stories → proof → promo → integrations → resources → conversion → FAQ.

- [ ] **Step 4: Implement full-page JS**

One local `script.js` owns tabs, gallery controls, FAQ state, prompt copying only if needed beyond root prompt UI, and progressive View Transition enhancement. No autoplay behavior may trap or block user navigation.

- [ ] **Step 5: Verify syntax and structural validator**

Run:
```bash
node --check examples/enterprise-product-overview/script.js
python3 tests/validate-product-storytelling.py
```

Expected: PASS for all structural assertions.

- [ ] **Step 6: Verify standalone independence**

Extend validator to reject `../<sibling-component>/...` dependencies inside standalone component HTML/CSS/JS.

Run: `python3 tests/validate-product-storytelling.py`

Expected: PASS.

- [ ] **Step 7: Commit**

```bash
git add examples/enterprise-product-overview tests/validate-product-storytelling.py
git commit -m "feat: add enterprise product overview example"
```

### Task 8: Integrate With the Lab Homepage and Run Full Regression Verification

**Files:**
- Modify: `index.html`
- Modify: `README.md`
- Modify only if required for the new collection card: `styles-base.css` or `preview-motion.css`
- Modify: `tests/validate-product-storytelling.py`

**Interfaces:**
- Consumes: all completed standalone components and the full-page example.
- Produces: discoverability from the main lab without changing behavior of the existing 27 demos.

- [ ] **Step 1: Add failing integration assertions**

Assert root homepage links to:
- `examples/enterprise-product-overview/`
- `components/product-storytelling/`

Assert README documents the component collection and full-page example without changing/removing the existing 27 demo entries.

- [ ] **Step 2: Run validator to verify RED**

Run: `python3 tests/validate-product-storytelling.py`

Expected: FAIL on root integration links/docs.

- [ ] **Step 3: Add one Product Storytelling collection card/section to the homepage**

Use one distinctive preview that communicates the assembled page architecture. Do not renumber or rewrite the existing demo collection unless the UI needs a separate collection count label.

- [ ] **Step 4: Update README**

Add concise links for the 13 components and complete enterprise example. Keep existing README content intact otherwise.

- [ ] **Step 5: Run complete static validation**

Run:
```bash
python3 tests/validate-product-storytelling.py
find components/product-storytelling examples/enterprise-product-overview -name '*.js' -print0 | xargs -0 -n1 node --check
```

Expected: PASS / zero JS syntax errors.

- [ ] **Step 6: Run local browser audit at required widths**

Serve the repo:
```bash
python3 -m http.server 4173
```

Check the root homepage, all 13 standalone components, and the full-page example at approximately:
- 1440×1000
- 1024×900
- 768×900
- 390×844
- 320×700

For each page verify:
- `document.documentElement.scrollWidth <= window.innerWidth`
- prompt section is reachable and visible
- focus indicators are visible
- no clipped primary content

- [ ] **Step 7: Run keyboard interaction audit**

Verify:
- capability tabs with ArrowLeft/ArrowRight/Home/End
- customer gallery controls with keyboard activation
- FAQ buttons with Enter/Space
- prompt Copy button accessible by keyboard

- [ ] **Step 8: Run reduced-motion audit**

Emulate `prefers-reduced-motion: reduce` and verify marquee, ambient hero motion, reveal animations, and continuous effects stop or become static while all content remains visible.

- [ ] **Step 9: Compare branch against `main` for regression scope**

Run:
```bash
git diff --name-status main...HEAD
```

Expected: changes limited to new product-storytelling files, the new example, validation/doc files, and minimal root homepage/README integration. Existing `examples/<old-demo>/` files must not be modified.

- [ ] **Step 10: Final test run**

Run:
```bash
python3 tests/validate-product-storytelling.py
find components/product-storytelling examples/enterprise-product-overview -name '*.js' -print0 | xargs -0 -n1 node --check
```

Expected: all checks pass.

- [ ] **Step 11: Commit integration**

```bash
git add index.html README.md styles-base.css preview-motion.css tests/validate-product-storytelling.py
git commit -m "feat: integrate product storytelling collection"
```

- [ ] **Step 12: Whole-branch review before merge**

Review the branch against the spec, verify GitHub Pages paths, and only then open a PR from `feature/product-storytelling-system` to `main`.
