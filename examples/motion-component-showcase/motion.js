(function () {
  function initHeroCards() {
    const root = document.querySelector('[data-kinetic-hero]');
    if (!root) return;

    const panels = [...root.querySelectorAll('[data-kinetic-panel]')];
    const coarsePointer = window.matchMedia('(pointer: coarse)').matches;

    if (!coarsePointer) return;

    panels.forEach((panel) => {
      panel.addEventListener('click', () => {
        const wasActive = panel.classList.contains('is-active');
        panels.forEach((item) => item.classList.remove('is-active'));
        if (!wasActive) panel.classList.add('is-active');
      });
    });
  }

  function initMosaic() {
    const root = document.querySelector('[data-mosaic]');
    if (!root || window.matchMedia('(pointer: coarse)').matches) return;

    root.querySelectorAll('[data-mosaic-tile]').forEach((tile) => {
      tile.addEventListener('pointermove', (event) => {
        const rect = tile.getBoundingClientRect();
        const x = ((event.clientX - rect.left) / rect.width) * 100;
        const y = ((event.clientY - rect.top) / rect.height) * 100;

        tile.style.setProperty('--spot-x', `${x}%`);
        tile.style.setProperty('--spot-y', `${y}%`);
        tile.style.setProperty('--tilt-x', `${(50 - y) * 0.012}deg`);
        tile.style.setProperty('--tilt-y', `${(x - 50) * 0.012}deg`);
      });

      tile.addEventListener('pointerleave', () => {
        tile.style.setProperty('--spot-x', '50%');
        tile.style.setProperty('--spot-y', '50%');
        tile.style.setProperty('--tilt-x', '0deg');
        tile.style.setProperty('--tilt-y', '0deg');
      });
    });
  }

  function initMotionShowcase() {
    initHeroCards();
    initMosaic();

    if (!window.gsap || !window.ScrollTrigger) return;

    const gsap = window.gsap;
    gsap.registerPlugin(window.ScrollTrigger);

    const mm = gsap.matchMedia();

    mm.add(
      {
        desktop: '(min-width: 901px)',
        reduce: '(prefers-reduced-motion: reduce)'
      },
      (context) => {
        if (!context.conditions.desktop || context.conditions.reduce) return;

        const stack = document.querySelector('[data-stack]');

        if (stack) {
          const cards = [...stack.querySelectorAll('[data-stack-card]')];

          cards.forEach((card, index) => {
            gsap.set(card, { zIndex: index + 1 });

            if (index === cards.length - 1) return;

            gsap.to(card, {
              scale: 0.962,
              y: -10,
              rotateX: 0.45,
              opacity: 0.86,
              ease: 'none',
              scrollTrigger: {
                trigger: cards[index + 1],
                start: 'top 82%',
                end: 'top 24%',
                scrub: 0.55
              }
            });
          });
        }

        const orbit = document.querySelector('[data-orbit]');

        if (orbit) {
          const chapters = [...orbit.querySelectorAll('[data-orbit-chapter]')];
          const nodes = [...orbit.querySelectorAll('[data-orbit-node]')];
          const marker = orbit.querySelector('[data-orbit-marker]');
          const coreValue = orbit.querySelector('[data-orbit-core-value]');
          const visual = orbit.querySelector('.orbit-visual');
          let current = -1;

          gsap.set(chapters, { autoAlpha: 0, y: 14 });

          const markerPosition = (index) => {
            if (!marker || !visual || !nodes[index]) return null;

            const visualRect = visual.getBoundingClientRect();
            const nodeRect = nodes[index].getBoundingClientRect();
            const centerX = visualRect.width / 2;
            const centerY = visualRect.height / 2;
            const nodeX = nodeRect.left - visualRect.left + nodeRect.width / 2;
            const nodeY = nodeRect.top - visualRect.top + nodeRect.height / 2;
            const dx = nodeX - centerX;
            const dy = nodeY - centerY;
            const distance = Math.hypot(dx, dy) || 1;
            const svg = visual.querySelector('svg');
            const orbitCircle = svg ? svg.querySelector('circle') : null;
            const viewBoxWidth = svg && svg.viewBox && svg.viewBox.baseVal ? svg.viewBox.baseVal.width : 0;
            const radiusRatio = orbitCircle && viewBoxWidth
              ? orbitCircle.r.baseVal.value / viewBoxWidth
              : 0.373;
            const radius = Math.min(visualRect.width, visualRect.height) * radiusRatio;

            return {
              x: centerX + (dx / distance) * radius,
              y: centerY + (dy / distance) * radius
            };
          };

          const moveMarker = (index, immediate = false) => {
            const point = markerPosition(index);
            if (!point || !marker) return;

            gsap.to(marker, {
              left: 0,
              top: 0,
              x: point.x,
              y: point.y,
              xPercent: -50,
              yPercent: -50,
              duration: immediate ? 0 : 0.46,
              ease: 'power2.inOut',
              overwrite: true
            });
          };

          const activate = (index, immediate = false) => {
            if (index === current && !immediate) return;

            current = index;

            chapters.forEach((element, chapterIndex) => {
              const isActive = chapterIndex === index;
              element.classList.toggle('is-active', isActive);
              gsap.killTweensOf(element);

              if (isActive) {
                gsap.set(element, { visibility: 'visible' });
                gsap.fromTo(
                  element,
                  { opacity: immediate ? 1 : 0, y: immediate ? 0 : 14 },
                  { opacity: 1, y: 0, duration: immediate ? 0 : 0.34, ease: 'power3.out' }
                );
              } else {
                gsap.set(element, { autoAlpha: 0, y: 14 });
              }
            });

            nodes.forEach((element, nodeIndex) => {
              element.classList.toggle('is-active', nodeIndex === index);
            });

            if (coreValue) {
              coreValue.textContent = String(index + 1).padStart(2, '0');
            }

            moveMarker(index, immediate);
          };

          activate(0, true);

          const orbitTrigger = window.ScrollTrigger.create({
            trigger: orbit,
            start: 'top top',
            end: 'bottom bottom',
            onUpdate: (self) => {
              const index = Math.min(
                chapters.length - 1,
                Math.floor(self.progress * chapters.length)
              );
              activate(index);
            }
          });

          const syncMarker = () => moveMarker(current, true);
          window.addEventListener('resize', syncMarker);
          window.ScrollTrigger.addEventListener('refresh', syncMarker);

          return () => {
            orbitTrigger.kill();
            window.removeEventListener('resize', syncMarker);
            window.ScrollTrigger.removeEventListener('refresh', syncMarker);
          };
        }
      }
    );
  }

  window.initMotionShowcase = initMotionShowcase;

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initMotionShowcase, { once: true });
  } else {
    initMotionShowcase();
  }
})();
