/* ============================================================
   CP-II Lab — Code Block Manager
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {
  initCodeTabs();
  initCopyButtons();
});

/* ============================================================
   Language Tab Switching
   ============================================================ */
function initCodeTabs() {
  document.querySelectorAll('.code-block').forEach(block => {
    const tabs = block.querySelectorAll('.code-block__tab');
    const contents = block.querySelectorAll('.code-block__content');

    tabs.forEach(tab => {
      tab.addEventListener('click', () => {
        const lang = tab.dataset.lang;

        // Update active tab
        tabs.forEach(t => t.classList.remove('active'));
        tab.classList.add('active');

        // Show matching content
        contents.forEach(c => {
          c.classList.toggle('active', c.dataset.lang === lang);
        });
      });
    });
  });
}

/* ============================================================
   Copy to Clipboard
   ============================================================ */
function initCopyButtons() {
  document.querySelectorAll('.code-block__copy').forEach(btn => {
    btn.addEventListener('click', async () => {
      const block = btn.closest('.code-block');
      const activeContent = block.querySelector('.code-block__content.active code');

      if (!activeContent) return;

      try {
        await navigator.clipboard.writeText(activeContent.textContent);
        btn.classList.add('copied');
        btn.innerHTML = '✓ Copied';

        setTimeout(() => {
          btn.classList.remove('copied');
          btn.innerHTML = '📋 Copy';
        }, 2000);
      } catch (err) {
        // Fallback for older browsers
        const textarea = document.createElement('textarea');
        textarea.value = activeContent.textContent;
        textarea.style.position = 'fixed';
        textarea.style.opacity = '0';
        document.body.appendChild(textarea);
        textarea.select();
        document.execCommand('copy');
        document.body.removeChild(textarea);

        btn.classList.add('copied');
        btn.innerHTML = '✓ Copied';

        setTimeout(() => {
          btn.classList.remove('copied');
          btn.innerHTML = '📋 Copy';
        }, 2000);
      }
    });
  });
}

/* ============================================================
   Syntax Highlighting Helper (basic, for when Prism isn't loaded)
   ============================================================ */
function highlightCode(code, language) {
  if (typeof Prism !== 'undefined') {
    const grammar = Prism.languages[language] || Prism.languages.plaintext;
    return Prism.highlight(code, grammar, language);
  }
  return escapeHTML(code);
}

function escapeHTML(str) {
  return str.replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}
