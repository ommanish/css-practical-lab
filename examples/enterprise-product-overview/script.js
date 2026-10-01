const reduceMotion=window.matchMedia('(prefers-reduced-motion: reduce)');

const motionStyles=document.createElement('link');
motionStyles.rel='stylesheet';
motionStyles.href='scroll-motion.css';
document.head.append(motionStyles);
motionStyles.addEventListener('load',()=>initPageMotion());

function initPageMotion(){
  if(reduceMotion.matches)return;

  document.documentElement.classList.add('motion-enabled');

  const curtain=document.createElement('div');
  curtain.className='page-load-curtain';
  curtain.setAttribute('aria-hidden','true');
  curtain.innerHTML='<span class="page-load-curtain__mark">Entering the system<i></i></span>';
  document.body.prepend(curtain);

  const groups=[
    ['.hero__visual','motion-zoom'],
    ['.section-head',''],
    ['.solution-grid > article',''],
    ['.cap-tabs',''],
    ['.cap-panels','motion-zoom'],
    ['.feature-grid > article',''],
    ['.trust > .eyebrow',''],
    ['.trust-track',''],
    ['.story-card',''],
    ['.proof-grid > article',''],
    ['.promo > :first-child','motion-left'],
    ['.promo > :last-child','motion-right'],
    ['.integration-grid > article',''],
    ['.resource-grid > article',''],
    ['.conversion-grid > article',''],
    ['.faq > article',''],
    ['.vibe-prompt','']
  ];

  const mediaSelector='.hero__visual,.mini-art,.cap-art,.story-art,.proof-art,.promo-art,.int-icon,.res-art';
  document.querySelectorAll(mediaSelector).forEach(el=>el.classList.add('motion-media-target'));

  const items=[];
  groups.forEach(([selector,modifier])=>{
    document.querySelectorAll(selector).forEach((el,index)=>{
      if(el.classList.contains('motion-reveal'))return;
      el.classList.add('motion-reveal');
      if(modifier)el.classList.add(modifier);
      el.style.setProperty('--motion-delay',`${Math.min(index%6,5)*75}ms`);
      items.push(el);
    });
  });

  const observer=new IntersectionObserver(entries=>{
    entries.forEach(entry=>{
      if(!entry.isIntersecting)return;
      entry.target.classList.add('is-visible');
      observer.unobserve(entry.target);
    });
  },{threshold:.13,rootMargin:'0px 0px -9% 0px'});

  items.forEach(item=>observer.observe(item));

  requestAnimationFrame(()=>requestAnimationFrame(()=>{
    document.documentElement.classList.add('is-page-ready');
  }));

  window.setTimeout(()=>curtain.remove(),1500);
}

const tabs=[...document.querySelectorAll('.cap-tabs [role="tab"]')];
const panels=[...document.querySelectorAll('.cap-panels [role="tabpanel"]')];
const indicator=document.querySelector('.cap-indicator');
function moveIndicator(tab){if(!tab||!indicator)return;const a=tab.getBoundingClientRect(),b=tab.parentElement.getBoundingClientRect();indicator.style.width=`${a.width}px`;indicator.style.transform=`translateX(${a.left-b.left}px)`}
function applyTab(tab,focus=false){tabs.forEach(t=>{const on=t===tab;t.setAttribute('aria-selected',String(on));t.tabIndex=on?0:-1});panels.forEach(p=>p.hidden=p.id!==tab.getAttribute('aria-controls'));moveIndicator(tab);if(focus)tab.focus()}
function selectTab(tab,focus=false){if(document.startViewTransition&&!reduceMotion.matches){document.startViewTransition(()=>applyTab(tab,focus))}else applyTab(tab,focus)}
tabs.forEach((tab,i)=>{tab.addEventListener('click',()=>selectTab(tab));tab.addEventListener('keydown',e=>{let n=null;if(e.key==='ArrowRight')n=(i+1)%tabs.length;if(e.key==='ArrowLeft')n=(i-1+tabs.length)%tabs.length;if(e.key==='Home')n=0;if(e.key==='End')n=tabs.length-1;if(n!==null){e.preventDefault();selectTab(tabs[n],true)}})});
window.addEventListener('resize',()=>moveIndicator(document.querySelector('.cap-tabs [aria-selected="true"]')));
moveIndicator(tabs[0]);

const storyRow=document.querySelector('[data-story-row]');
if(storyRow){
  const storyCards=[...storyRow.children];
  function moveStories(dir){const gap=parseFloat(getComputedStyle(storyRow).gap)||18;const amount=storyCards[0].getBoundingClientRect().width+gap;storyRow.scrollBy({left:dir*amount,behavior:reduceMotion.matches?'auto':'smooth'})}
  document.querySelector('[data-story-prev]')?.addEventListener('click',()=>moveStories(-1));
  document.querySelector('[data-story-next]')?.addEventListener('click',()=>moveStories(1));
}

document.querySelectorAll('.faq button').forEach(button=>button.addEventListener('click',()=>{const open=button.getAttribute('aria-expanded')==='true';button.setAttribute('aria-expanded',String(!open));button.closest('article').classList.toggle('is-open',!open)}));
