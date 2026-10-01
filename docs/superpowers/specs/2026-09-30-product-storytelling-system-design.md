# Product Storytelling System — Design Spec

## Goal

Add an original, reusable enterprise-product storytelling system to `css-practical-lab`, inspired by the structural rhythm of the Salesforce Data page without copying Salesforce content, brand assets, product names, proprietary graphics, or exact visual styling.

The system must support two use cases:

1. Standalone reusable components that can be copied into other projects.
2. One complete, responsive product-overview page that assembles those components into a realistic end-to-end example.

The implementation stays framework-free, CSS-first, copy-friendly, accessible, and consistent with the existing lab.

## Design Principles

- Original visual language, not a Salesforce clone.
- Component structure inspired by common enterprise product storytelling patterns.
- Every component should communicate one clear content job.
- Motion should reinforce hierarchy and storytelling rather than decorate every element.
- CSS first; minimal vanilla JavaScript only for stateful behaviors.
- Progressive enhancement for newer browser APIs.
- `prefers-reduced-motion` support for all animated experiences.
- Keyboard and screen-reader usability for tabs, carousels, accordions, and interactive controls.
- Responsive from 320px through large desktop widths.
- Each component must work independently from the full-page example.

## Visual Direction

Create a premium 2026 technology-product aesthetic with:

- deep ink / charcoal surfaces mixed with warm off-white sections
- electric lime as the primary accent
- violet and cyan as secondary accents
- oversized editorial typography
- generous whitespace
- large rounded media surfaces
- subtle grid, glow, gradient, and noise-like effects built with CSS/SVG
- strong content hierarchy with restrained motion
- no copied Salesforce imagery, clouds, mascots, logos, customer names, or text

The page should feel original and polished while preserving the broad pacing of an enterprise product page: hero, product explanation, capability depth, proof, resources, conversion, FAQ.

## Component Set

### 1. Announcement Bar

**Purpose:** timely product or launch message.

**Structure:**
- message
- optional badge
- inline CTA
- dismiss control optional in the standalone demo only

**Motion:**
- subtle slide/fade entrance
- CTA arrow shift on hover/focus

### 2. Product Hero / Marquee

**Purpose:** primary value proposition and visual identity.

**Structure:**
- eyebrow
- large headline
- supporting copy
- primary CTA
- secondary CTA
- animated abstract product visual

**Motion:**
- staggered copy reveal
- slow ambient visual movement
- subtle parallax between visual layers
- no autoplay motion when reduced-motion is enabled

### 3. Solution Card Grid

**Purpose:** summarize product areas or solution families.

**Structure:**
- section intro
- 2–6 cards
- card media
- eyebrow
- title
- description
- one or two links

**Responsive:**
- 3 columns large desktop
- 2 columns tablet
- 1 column mobile

**Motion:**
- staggered card reveal
- media scale/parallax on hover
- CTA arrow movement

### 4. Capability Tabs

**Purpose:** switch among major capability groups.

**Structure:**
- tab list
- active indicator
- large content panel
- supporting media / abstract visual

**Interaction:**
- arrow-key keyboard navigation
- proper ARIA tab semantics
- active state reflected visually and semantically

**Motion:**
- moving pill or underline
- content crossfade + clipped reveal
- reduced-motion fallback to instant state changes

### 5. Numbered Feature Grid

**Purpose:** explain 3–6 features within a capability.

**Structure:**
- number / index
- feature title
- description
- optional link

**Motion:**
- subtle viewport reveal
- line/number progression animation

### 6. Trust / Logo Marquee

**Purpose:** ecosystem or partner proof.

**Structure:**
- section label
- horizontally repeated marks using original generic placeholder marks

**Motion:**
- seamless CSS marquee
- pause on hover/focus
- static wrapping layout under reduced motion

### 7. Customer Story Gallery

**Purpose:** show real-world outcome-style stories using fictional companies/content.

**Structure:**
- image/illustration
- customer category
- story title
- result statement
- CTA

**Interaction:**
- native horizontal scroll and scroll-snap
- keyboard-accessible controls when controls are shown

**Motion:**
- active-card emphasis
- lightweight transitions only

### 8. Analyst / Proof Cards

**Purpose:** provide large credibility blocks without using real analyst brands.

**Structure:**
- large editorial card
- proof category
- headline
- description
- CTA

**Motion:**
- subtle media scale
- layered text reveal

### 9. Community / Editorial Promo

**Purpose:** break the card-grid rhythm with a high-impact promotional blade.

**Structure:**
- large visual
- eyebrow
- heading
- body
- CTA

**Motion:**
- layered parallax / floating CSS shapes
- content reveal on viewport entry

### 10. Integration Card Grid

**Purpose:** show product integrations / ecosystem connections.

**Structure:**
- 4 cards
- original generic symbol
- heading
- description
- CTA

**Motion:**
- hover elevation
- icon shift
- CTA arrow transition

### 11. Resource Grid

**Purpose:** surface guides, videos, articles, and architecture content.

**Structure:**
- resource type
- thumbnail/abstract artwork
- title
- description
- CTA

**Motion:**
- sequential reveal
- restrained thumbnail zoom on hover

### 12. Conversion CTA

**Purpose:** end the narrative with two clear next actions.

**Structure:**
- 2-up actions
- heading
- short copy
- CTA

**Motion:**
- directional background/arrow transitions

### 13. FAQ Accordion

**Purpose:** detailed education and SEO-style question coverage using original generic copy.

**Structure:**
- question button
- aligned `+ / ×` icon
- answer region

**Interaction:**
- real buttons
- `aria-expanded`
- keyboard native behavior

**Motion:**
- CSS grid `0fr → 1fr`
- opacity transition
- icon glyph transforms without moving the icon container

## Full-Page Example

Create:

`examples/enterprise-product-overview/`

The page assembles the standalone components in this sequence:

1. Announcement bar
2. Product hero
3. Solution card grid
4. Capability tabs
5. Numbered feature grid
6. Trust marquee
7. Customer story gallery
8. Proof cards
9. Editorial/community promo
10. Integration card grid
11. Resource grid
12. Conversion CTA
13. FAQ

The page must use fictional product content and original visual assets generated from CSS/SVG only.

## Repository Structure

```text
components/
  product-storytelling/
    announcement-bar/
    hero-product-marquee/
    solution-card-grid/
    capability-tabs/
    numbered-feature-grid/
    logo-marquee/
    customer-story-gallery/
    analyst-proof-cards/
    community-promo/
    integration-card-grid/
    resource-grid/
    conversion-cta/
    faq-accordion/

examples/
  enterprise-product-overview/
    index.html
    style.css
    script.js
```

Each standalone component directory should contain only the files it needs, generally:

- `index.html`
- `style.css`
- `script.js` only when stateful behavior requires JavaScript

No framework, package manager, build step, animation library, or runtime dependency is introduced.

## Vibe Coding Prompt Pattern

Each standalone component and the full-page example should contain a visible **Vibe Coding Prompt** section using the existing lab prompt UI.

Each prompt should describe:

- goal
- visual structure
- interaction behavior
- animation behavior
- responsive behavior
- accessibility requirements
- technical constraints

The prompt should be implementation-agnostic enough to work with ChatGPT, Claude, Gemini, Cursor, Copilot, or similar tools.

## Animation System

Preferred native technologies:

- CSS transitions
- CSS keyframes
- `animation-timeline: view()` where appropriate
- scroll-driven animations with visible fallback content
- `position: sticky`
- `scroll-snap`
- `clip-path`
- masks where useful
- 2D/3D transforms
- `perspective`
- View Transition API as progressive enhancement
- IntersectionObserver only where CSS cannot reliably provide the effect

Avoid:

- GSAP
- Framer Motion
- Swiper
- animation frameworks
- autoplay behaviors that cannot be paused

## Accessibility

Required across the system:

- semantic heading hierarchy
- visible focus states
- keyboard-accessible interactive components
- ARIA tabs semantics for capability tabs
- `aria-expanded` for accordions
- descriptive link text
- no meaningful information conveyed only through animation
- `prefers-reduced-motion: reduce`
- no horizontal page overflow at 320px+
- adequate text/background contrast

## Performance

- no external JS libraries
- avoid layout-thrashing animation properties
- prefer `transform` and `opacity`
- lazy-load non-critical images if raster assets are ever added later
- CSS/SVG artwork should be lightweight
- avoid creating many independent continuous animations above the fold
- pause nonessential animation when appropriate

## Integration With Existing Lab

The existing homepage should gain a new collection/card for the product storytelling system and a link to the complete enterprise product overview example.

Do not rewrite the existing 27 demos or change their current behavior as part of this feature.

The new collection should visually fit the lab while being clearly identifiable as a larger component-system example.

## Testing / Acceptance Criteria

The work is complete only when:

- all 13 standalone components render independently
- the full-page example assembles all 13 patterns
- no Salesforce text, logos, images, customer names, or proprietary graphics are used
- desktop layout is checked at approximately 1440px
- tablet layout is checked around 768–1024px
- mobile layout is checked around 390px and 320px
- no horizontal overflow occurs
- all interactive controls work by keyboard
- tabs expose correct active semantics
- FAQ icon remains centered in both `+` and `×` states
- all animated sections support reduced motion
- all components expose a visible Vibe Coding Prompt and Copy Prompt control
- source links point to the correct component directories
- the assembled example can be opened directly through GitHub Pages
- the existing lab homepage and demos remain regression-safe

## Non-Goals

This feature will not:

- reproduce Salesforce branding or copy
- recreate Salesforce proprietary Page Builder blade code
- introduce a framework or component runtime
- create a generic design-system package with tokens/API documentation beyond what the demo needs
- add backend functionality
- add CMS integration

## Success Definition

A developer or designer should be able to open the lab, inspect a polished enterprise product page, then copy any individual component, its source, or its Vibe Coding Prompt and reuse the pattern independently in another project.
