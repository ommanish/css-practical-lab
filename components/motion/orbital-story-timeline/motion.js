(function () {
  function initOrbitalTimeline() {
    const root = document.querySelector('[data-orbit]');
    if (!root) return;

    const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const desktop = window.matchMedia('(min-width: 901px)').matches;

    if (reduce || !desktop || !window.gsap || !window.ScrollTrigger) return;

    const gsap = window.gsap;
    gsap.registerPlugin(window.ScrollTrigger);

    const chapters = [...root.querySelectorAll('[data-orbit-chapter]')];
    const nodes = [...root.querySelectorAll('[data-orbit-node]')];
    const marker = root.querySelector('[data-orbit-marker]');
    const coreValue = root.querySelector('[data-orbit-core-value]');
    const visual = root.querySelector('.orbit-visual');
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
        : 0.367;
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

    const trigger = window.ScrollTrigger.create({
      trigger: root,
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
      trigger.kill();
      window.removeEventListener('resize', syncMarker);
      window.ScrollTrigger.removeEventListener('refresh', syncMarker);
    };
  }

  window.initOrbitalTimeline = initOrbitalTimeline;

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initOrbitalTimeline, { once: true });
  } else {
    initOrbitalTimeline();
  }
})();
