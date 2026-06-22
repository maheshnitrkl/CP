/* ============================================================
   CP-II Lab — Main JavaScript
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initNavbar();
  initScrollReveal();
  initScrollTop();
  initSearch();
  initProgress();
});

/* ============================================================
   Theme Toggle (Dark / Light)
   ============================================================ */
function initTheme() {
  const toggle = document.querySelector('.theme-toggle');
  if (!toggle) return;

  const saved = localStorage.getItem('cp2-theme') || 'dark';
  document.documentElement.setAttribute('data-theme', saved);

  toggle.addEventListener('click', () => {
    const current = document.documentElement.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('cp2-theme', next);
  });
}

/* ============================================================
   Navbar Scroll Effect & Mobile Menu
   ============================================================ */
function initNavbar() {
  const navbar = document.querySelector('.navbar');
  const hamburger = document.querySelector('.navbar__hamburger');
  const nav = document.querySelector('.navbar__nav');

  if (navbar) {
    window.addEventListener('scroll', () => {
      navbar.classList.toggle('scrolled', window.scrollY > 20);
    }, { passive: true });
  }

  if (hamburger && nav) {
    hamburger.addEventListener('click', () => {
      nav.classList.toggle('open');
      hamburger.classList.toggle('active');
    });

    // Close menu on link click
    nav.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        nav.classList.remove('open');
        hamburger.classList.remove('active');
      });
    });
  }
}

/* ============================================================
   Scroll Reveal (IntersectionObserver)
   ============================================================ */
function initScrollReveal() {
  const els = document.querySelectorAll('.reveal, .stagger');
  if (!els.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -40px 0px'
  });

  els.forEach(el => observer.observe(el));
}

/* ============================================================
   Scroll to Top Button
   ============================================================ */
function initScrollTop() {
  const btn = document.querySelector('.scroll-top');
  if (!btn) return;

  window.addEventListener('scroll', () => {
    btn.classList.toggle('visible', window.scrollY > 400);
  }, { passive: true });

  btn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}

/* ============================================================
   Search (landing page)
   ============================================================ */
function initSearch() {
  const searchInput = document.getElementById('module-search');
  if (!searchInput) return;

  const cards = document.querySelectorAll('.module-card');

  searchInput.addEventListener('input', (e) => {
    const q = e.target.value.toLowerCase().trim();

    cards.forEach(card => {
      const title = card.querySelector('.module-card__title')?.textContent.toLowerCase() || '';
      const desc = card.querySelector('.module-card__desc')?.textContent.toLowerCase() || '';
      const tags = card.querySelector('.module-card__tags')?.textContent.toLowerCase() || '';
      const match = !q || title.includes(q) || desc.includes(q) || tags.includes(q);
      card.style.display = match ? '' : 'none';
    });
  });
}

/* ============================================================
   Progress Tracking
   ============================================================ */
const TOTAL_MODULES = 12;

function initProgress() {
  updateProgressUI();
}

function getCompletedModules() {
  try {
    return JSON.parse(localStorage.getItem('cp2-progress') || '[]');
  } catch {
    return [];
  }
}

function toggleModuleComplete(moduleId) {
  const id = String(moduleId);
  let completed = getCompletedModules();
  if (completed.includes(id)) {
    completed = completed.filter(c => c !== id);
  } else {
    completed.push(id);
  }
  localStorage.setItem('cp2-progress', JSON.stringify(completed));
  updateProgressUI();
}

function updateProgressUI() {
  const completed = getCompletedModules();
  const pct = Math.round((completed.length / TOTAL_MODULES) * 100);

  const bar = document.querySelector('.progress-bar__fill');
  if (bar) {
    bar.style.width = pct + '%';
  }

  const label = document.querySelector('.progress-label');
  if (label) {
    label.textContent = `${completed.length}/${TOTAL_MODULES} modules completed (${pct}%)`;
  }

  // Update module card checkmarks
  document.querySelectorAll('.module-card').forEach(card => {
    const id = card.dataset.module;
    if (id && completed.includes(String(id))) {
      card.classList.add('completed');
    } else {
      card.classList.remove('completed');
    }
  });
}

/* ============================================================
   Problem Card Toggles (Module Pages)
   ============================================================ */
document.addEventListener('click', (e) => {
  const header = e.target.closest('.problem-card__header');
  if (!header) return;

  const card = header.closest('.problem-card');
  if (card) {
    card.classList.toggle('open');
  }
});

/* ============================================================
   Table of Contents Active State (Module Pages)
   ============================================================ */
function initTOC() {
  const tocLinks = document.querySelectorAll('.toc__link');
  const sections = document.querySelectorAll('.module-section');

  if (!tocLinks.length || !sections.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.id;
        tocLinks.forEach(link => {
          link.classList.toggle('active',
            link.getAttribute('href') === `#${id}`);
        });
      }
    });
  }, {
    threshold: 0.2,
    rootMargin: '-80px 0px -60% 0px'
  });

  sections.forEach(section => observer.observe(section));
}

// Call on module pages
if (document.querySelector('.toc')) {
  initTOC();
}

/* ============================================================
   Smooth Anchor Links
   ============================================================ */
document.addEventListener('click', (e) => {
  const link = e.target.closest('a[href^="#"]');
  if (!link) return;

  const href = link.getAttribute('href');
  // Only intercept pure hash links (e.g., "#modules"), not cross-page ones
  if (!href || !href.startsWith('#')) return;

  const target = document.querySelector(href);
  if (target) {
    e.preventDefault();
    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
});
