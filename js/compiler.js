/* compiler.js - Logic for the Online Compiler Page */

document.addEventListener('DOMContentLoaded', () => {
  initCompilerTabs();
});

function initCompilerTabs() {
  const tabs = document.querySelectorAll('.compiler-tab');
  const iframes = document.querySelectorAll('.compiler-iframe-container');

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      const lang = tab.dataset.lang;

      // Update active tab styling
      tabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');

      // Update active iframe
      iframes.forEach(iframe => {
        iframe.classList.remove('active');
        if (iframe.id === `iframe-${lang}`) {
          iframe.classList.add('active');
        }
      });
    });
  });

  // Check URL parameters for pre-selected language
  const urlParams = new URLSearchParams(window.location.search);
  const langParam = urlParams.get('lang');
  if (langParam === 'python' || langParam === 'cpp') {
    const tabToClick = document.querySelector(`.compiler-tab[data-lang="${langParam}"]`);
    if (tabToClick) {
      tabToClick.click();
    }
  }
}

// Theme syncing is handled in the JDoodle dashboard for embeds, 
// so we don't manually swap iframe srcs here anymore.
