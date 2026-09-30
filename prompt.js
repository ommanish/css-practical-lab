document.addEventListener("click",(event)=>{
  const button=event.target.closest("[data-copy-prompt]");
  if(!button)return;
  const section=button.closest("[data-prompt]");
  const text=section?.querySelector("[data-prompt-text]")?.textContent?.trim();
  if(!text)return;
  navigator.clipboard.writeText(text).then(()=>{
    const original=button.textContent;
    button.textContent="Copied ✓";
    button.dataset.copied="true";
    window.setTimeout(()=>{
      button.textContent=original;
      delete button.dataset.copied;
    },1600);
  });
});