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
// A static index of all problems for search. 
const PROBLEM_INDEX = [
  // Module 1
  { name: "Class Test", module: 1, href: "problems/m1-p1.html" },
  { name: "Largest Prime Factor", module: 1, href: "problems/m1-p2.html" },
  { name: "Sieve of Eratosthenes", module: 1, href: "problems/m1-p3.html" },
  { name: "GCD and LCM", module: 1, href: "problems/m1-p4.html" },
  { name: "Prime Factors", module: 1, href: "problems/m1-p5.html" },
  { name: "Check if Number is Prime", module: 1, href: "problems/m1-p6.html" },
  // Module 2
  { name: "Number of 1 Bits", module: 2, href: "problems/m2-p1.html" },
  { name: "Power of Two", module: 2, href: "problems/m2-p2.html" },
  { name: "Single Number", module: 2, href: "problems/m2-p3.html" },
  { name: "Counting Bits", module: 2, href: "problems/m2-p4.html" },
  { name: "Reverse Bits", module: 2, href: "problems/m2-p5.html" },
  { name: "Missing Number", module: 2, href: "problems/m2-p6.html" },
  // Module 3
  { name: "Binary Search", module: 3, href: "problems/m3-p1.html" },
  { name: "First and Last Position", module: 3, href: "problems/m3-p2.html" },
  { name: "Search Insert Position", module: 3, href: "problems/m3-p3.html" },
  { name: "Search in Rotated Sorted Array", module: 3, href: "problems/m3-p4.html" },
  { name: "Find Minimum in Rotated Sorted Array", module: 3, href: "problems/m3-p5.html" },
  { name: "Peak Index in a Mountain Array", module: 3, href: "problems/m3-p6.html" },
  // Module 4
  { name: "Minimum Moves to Equal Array Elements", module: 4, href: "problems/m4-p1.html" },
  { name: "Minimum Absolute Difference", module: 4, href: "problems/m4-p2.html" },
  { name: "Sort Array By Parity", module: 4, href: "problems/m4-p3.html" },
  { name: "Max Chunks To Make Sorted", module: 4, href: "problems/m4-p4.html" },
  { name: "Kth Largest Element in an Array", module: 4, href: "problems/m4-p5.html" },
  { name: "Boats to Save People", module: 4, href: "problems/m4-p6.html" },
  // Add more as needed, but this covers the first 4 modules for demo purposes.
];

function initSearch() {
  const searchInput = document.getElementById('module-search');
  if (!searchInput) return;

  const cards = document.querySelectorAll('.module-card');

  searchInput.addEventListener('input', (e) => {
    const q = e.target.value.toLowerCase().trim();

    cards.forEach(card => {
      const idStr = card.dataset.module;
      const modId = idStr ? parseInt(idStr) : -1;
      
      const title = card.querySelector('.module-card__title')?.textContent.toLowerCase() || '';
      const desc = card.querySelector('.module-card__desc')?.textContent.toLowerCase() || '';
      const tags = card.querySelector('.module-card__tags')?.textContent.toLowerCase() || '';
      
      // Check if module matches
      let match = !q || title.includes(q) || desc.includes(q) || tags.includes(q);
      
      // Check if any problem matches
      const matchingProblems = q ? PROBLEM_INDEX.filter(p => p.module === modId && p.name.toLowerCase().includes(q)) : [];
      if (matchingProblems.length > 0) match = true;

      card.style.display = match ? '' : 'none';

      // Handle sub-results for matching problems
      let probResultsContainer = card.querySelector('.problem-search-results');
      if (!probResultsContainer) {
        probResultsContainer = document.createElement('div');
        probResultsContainer.className = 'problem-search-results';
        probResultsContainer.style.marginTop = '1rem';
        probResultsContainer.style.padding = '0.5rem';
        probResultsContainer.style.background = 'var(--bg-elevated)';
        probResultsContainer.style.borderRadius = 'var(--radius-sm)';
        const cardBody = card.querySelector('.module-card__body');
        if (cardBody) cardBody.appendChild(probResultsContainer);
      }

      if (matchingProblems.length > 0) {
        probResultsContainer.style.display = 'block';
        probResultsContainer.innerHTML = '<div style="font-size: var(--fs-xs); color: var(--text-tertiary); margin-bottom: 0.25rem;">Matching Problems:</div>';
        matchingProblems.forEach(p => {
          const a = document.createElement('a');
          a.href = p.href;
          a.textContent = '↳ ' + p.name;
          a.style.display = 'block';
          a.style.fontSize = 'var(--fs-sm)';
          a.style.color = 'var(--accent-cyan)';
          a.style.textDecoration = 'none';
          a.style.marginBottom = '0.25rem';
          probResultsContainer.appendChild(a);
        });
      } else {
        probResultsContainer.style.display = 'none';
      }
    });
  });
}

/* ============================================================
   Progress Tracking
   ============================================================ */
const TOTAL_MODULES = 12;
const TOTAL_PROBLEMS = 76; // Total problems across all modules

function initProgress() {
  updateProgressUI();
  updateProblemProgressUI();
}

function getCompletedModules() {
  try { return JSON.parse(localStorage.getItem('cp2-progress') || '[]'); } 
  catch { return []; }
}

function getCompletedProblems() {
  try { return JSON.parse(localStorage.getItem('cp2-problem-progress') || '[]'); } 
  catch { return []; }
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

// Called directly from HTML onclick
window.toggleProblemComplete = function(problemId) {
  const id = String(problemId);
  let completed = getCompletedProblems();
  if (completed.includes(id)) {
    completed = completed.filter(c => c !== id);
  } else {
    completed.push(id);
  }
  localStorage.setItem('cp2-problem-progress', JSON.stringify(completed));
  updateProblemProgressUI();
}

function updateProgressUI() {
  const completed = getCompletedModules();
  const pct = Math.round((completed.length / TOTAL_MODULES) * 100);

  const bar = document.querySelector('.progress-bar__fill');
  if (bar) bar.style.width = pct + '%';

  const label = document.querySelector('.progress-label');
  if (label) label.textContent = `${completed.length}/${TOTAL_MODULES} modules completed (${pct}%)`;

  // Update module card checkmarks (index.html)
  document.querySelectorAll('.module-card').forEach(card => {
    const id = card.dataset.module;
    if (id && completed.includes(String(id))) {
      card.classList.add('completed');
    } else {
      card.classList.remove('completed');
    }
  });
}

function updateProblemProgressUI() {
  const completed = getCompletedProblems();
  
  // Update problem checkboxes on module pages
  document.querySelectorAll('.problem-card__checkbox input').forEach(input => {
    const id = input.id.replace('check-', ''); // e.g., check-m1-p1 -> m1-p1
    input.checked = completed.includes(id);
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
