(function () {
  function initKineticHero() {
    const root = document.querySelector('[data-kinetic-hero]');
    if (!root) return;

    const panels = [...root.querySelectorAll('[data-kinetic-panel]')];
    const coarsePointer = window.matchMedia('(pointer: coarse)').matches;

    if (!coarsePointer) return;

    panels.forEach((panel) => {
      panel.addEventListener('click', () => {
        const wasActive = panel.classList.contains('is-active');

        panels.forEach((item) => item.classList.remove('is-active'));

        if (!wasActive) {
          panel.classList.add('is-active');
        }
      });
    });
  }

  window.initKineticHero = initKineticHero;

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initKineticHero, { once: true });
  } else {
    initKineticHero();
  }
})();
