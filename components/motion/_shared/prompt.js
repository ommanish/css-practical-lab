(function () {
  function copyFallback(text) {
    const textarea = document.createElement('textarea');
    textarea.value = text;
    textarea.setAttribute('readonly', '');
    textarea.style.position = 'fixed';
    textarea.style.opacity = '0';
    textarea.style.pointerEvents = 'none';
    document.body.appendChild(textarea);
    textarea.select();

    const copied = document.execCommand('copy');
    textarea.remove();

    if (!copied) throw new Error('Copy command failed');
  }

  async function copyText(text) {
    if (navigator.clipboard && window.isSecureContext) {
      await navigator.clipboard.writeText(text);
      return;
    }

    copyFallback(text);
  }

  function initDemoPrompts() {
    document.querySelectorAll('[data-copy-prompt]').forEach((button) => {
      const section = button.closest('.build-prompt');
      const prompt = section?.querySelector('[data-prompt-text]');
      const status = section?.querySelector('[data-copy-status]');

      if (!prompt) return;

      const defaultLabel = button.textContent;
      let resetTimer;

      button.addEventListener('click', async () => {
        const text = prompt.textContent.trim();

        try {
          await copyText(text);
          window.clearTimeout(resetTimer);
          button.textContent = 'Copied';
          if (status) status.textContent = 'Prompt copied to clipboard.';

          resetTimer = window.setTimeout(() => {
            button.textContent = defaultLabel;
            if (status) status.textContent = '';
          }, 1800);
        } catch (error) {
          if (status) status.textContent = 'Copy failed. Select the prompt text and copy it manually.';
        }
      });
    });
  }

  window.initDemoPrompts = initDemoPrompts;

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initDemoPrompts, { once: true });
  } else {
    initDemoPrompts();
  }
})();
