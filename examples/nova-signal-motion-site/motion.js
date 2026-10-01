(() => {
  const header = document.querySelector('[data-header]');
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const mobile = window.matchMedia('(max-width: 760px)').matches;
  const setHeader = () => header?.classList.toggle('is-scrolled', window.scrollY > 40);
  setHeader();
  addEventListener('scroll', setHeader, { passive: true });

  document.querySelectorAll('.mobile-nav a').forEach(link => link.addEventListener('click', () => {
    link.closest('details')?.removeAttribute('open');
  }));

  if (reduced || mobile || !window.gsap || !window.ScrollTrigger) return;
  gsap.registerPlugin(ScrollTrigger);

  const mm = gsap.matchMedia();
  mm.add('(min-width: 761px)', () => {
    const intro = gsap.timeline({ defaults: { ease: 'power3.out' } });
    intro.from('[data-reveal]', { yPercent: 45, opacity: 0, duration: 1.05, stagger: 0.11 })
      .to('[data-hero-media] img', { scale: 1, duration: 1.4 }, 0);

    gsap.to('[data-hero-media] img', { yPercent: 8, scale: .98, ease: 'none', scrollTrigger: { trigger: '[data-hero]', start: 'top top', end: 'bottom top', scrub: .8 } });

    gsap.from('[data-section="premise"] .premise-copy', { y: 60, opacity: 0, scrollTrigger: { trigger: '[data-section="premise"]', start: 'top 72%', end: 'top 45%', scrub: .8 } });
    gsap.from('[data-media-reveal] img', { scale: 1.08, filter: 'blur(10px)', scrollTrigger: { trigger: '[data-media-reveal]', start: 'top 85%', end: 'center 55%', scrub: .8 } });

    const caps = ['observe','understand','act'];
    const capTimeline = gsap.timeline({ scrollTrigger: { trigger: '[data-capability-section]', start: 'top top', end: '+=220%', pin: '.capability-stage', scrub: .6, anticipatePin: 1 } });
    caps.forEach((key, i) => {
      if (i === 0) return;
      const at = i;
      capTimeline.to(`.capability-copy-item[data-capability="${caps[i-1]}"]`, { opacity: 0, y: -22, duration: .35 }, at)
        .to(`.cap-scene[data-scene="${caps[i-1]}"]`, { opacity: 0, scale: 1.035, duration: .45 }, at)
        .fromTo(`.capability-copy-item[data-capability="${key}"]`, { opacity: 0, y: 26 }, { opacity: 1, y: 0, duration: .45 }, at + .2)
        .fromTo(`.cap-scene[data-scene="${key}"]`, { opacity: 0, scale: 1.05 }, { opacity: 1, scale: 1, duration: .55 }, at + .15)
        .to('.capability-progress span', { width: `${(i+1)/3*100}%`, duration: .5 }, at + .15);
    });

    const flowSteps = gsap.utils.toArray('[data-flow-step]');
    const flow = gsap.timeline({ scrollTrigger: { trigger: '[data-system]', start: 'top 70%', end: 'bottom 55%', scrub: .7 } });
    flow.to('.flow-line span', { width: '100%', duration: 4, ease: 'none' });
    flowSteps.forEach((step, i) => flow.to(step, { opacity: 1, color: '#fff', duration: .3 }, i + .3));

    gsap.from('.metrics > div', { y: 40, opacity: 0, stagger: .12, scrollTrigger: { trigger: '[data-scale]', start: 'top 60%' } });
    gsap.to('.scale-media img', { yPercent: 10, scale: 1.04, ease: 'none', scrollTrigger: { trigger: '[data-scale]', start: 'top bottom', end: 'bottom top', scrub: .8 } });

    const beats = ['anomaly','impact','response'];
    const storyTimeline = gsap.timeline({ scrollTrigger: { trigger: '[data-story-section]', start: 'top top', end: '+=220%', pin: '.story-stage', scrub: .6, anticipatePin: 1 } });
    beats.forEach((key, i) => {
      if (i === 0) return;
      const at = i;
      storyTimeline.to(`.story-beat[data-story-beat="${beats[i-1]}"]`, { opacity: 0, y: -22, duration: .35 }, at)
        .to(`.story-scene[data-story-scene="${beats[i-1]}"]`, { opacity: 0, scale: 1.05, duration: .5 }, at)
        .fromTo(`.story-beat[data-story-beat="${key}"]`, { opacity: 0, y: 26 }, { opacity: 1, y: 0, duration: .45 }, at + .2)
        .fromTo(`.story-scene[data-story-scene="${key}"]`, { opacity: 0, scale: 1.07 }, { opacity: 1, scale: 1, duration: .55 }, at + .15);
    });

    gsap.from('[data-final] .final-copy > *', { y: 50, opacity: 0, stagger: .1, scrollTrigger: { trigger: '[data-final]', start: 'top 62%' } });
    gsap.fromTo('[data-final] picture img', { scale: 1.08 }, { scale: 1, ease: 'none', scrollTrigger: { trigger: '[data-final]', start: 'top bottom', end: 'bottom bottom', scrub: .8 } });

    return () => ScrollTrigger.getAll().forEach(t => t.kill());
  });
})();
