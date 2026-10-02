(function () {
  function initPerspectiveStack() {
    const root = document.querySelector('[data-stack]');
    if (!root) return;

    const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const desktop = window.matchMedia('(min-width: 801px)').matches;

    if (reduce || !desktop || !window.gsap || !window.ScrollTrigger) return;

    const gsap = window.gsap;
    gsap.registerPlugin(window.ScrollTrigger);

    const cards = [...root.querySelectorAll('[data-stack-card]')];

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

  window.initPerspectiveStack = initPerspectiveStack;

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initPerspectiveStack, { once: true });
  } else {
    initPerspectiveStack();
  }
})();
