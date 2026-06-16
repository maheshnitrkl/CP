/* compiler.js - Logic for the Online Compiler Page */

document.addEventListener('DOMContentLoaded', () => {
  initCompilerTabs();
  syncThemeWithIframes();
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

function syncThemeWithIframes() {
  // Listen for theme toggle clicks from the main navbar
  const themeToggle = document.getElementById('theme-toggle');
  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      // The theme toggle changes the data-theme on html element.
      // We need to wait a tick for it to update, then update our iframes.
      setTimeout(() => {
        const currentTheme = document.documentElement.getAttribute('data-theme');
        updateIframeThemes(currentTheme);
      }, 50);
    });
  }
}

function updateIframeThemes(theme) {
  // OneCompiler supports theme=dark and theme=light in the URL
  const iframes = document.querySelectorAll('.compiler-iframe-container iframe');
  
  iframes.forEach(iframe => {
    let src = iframe.src;
    if (theme === 'light') {
      src = src.replace('theme=dark', 'theme=light');
    } else {
      src = src.replace('theme=light', 'theme=dark');
    }
    
    // Only reload iframe if theme actually changed in URL to prevent unnecessary reloads
    if (iframe.src !== src) {
      iframe.src = src;
    }
  });
}
