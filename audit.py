#!/usr/bin/env python3
"""Comprehensive audit script for CP-II Website"""
import glob, re, os

problems_dir = "d:/CP_II_Website/problems"
modules_dir  = "d:/CP_II_Website/modules"

issues = []

def warn(fname, msg):
    issues.append(f"  [{os.path.basename(fname)}]  {msg}")

# ──────────────────────────────────────────────
# 1. Collect all problem files and module files
# ──────────────────────────────────────────────
problem_files = sorted(glob.glob(f"{problems_dir}/m*.html"))
module_files  = sorted(glob.glob(f"{modules_dir}/module-*.html"))

# ──────────────────────────────────────────────
# 2. Per-file checks on PROBLEM pages
# ──────────────────────────────────────────────
REQUIRED_SECTIONS = [
    ("Problem Statement",   r'Problem Statement'),
    ("Approach Progression",r'Approach Progression'),
    ("Approach Comparison", r'comparison-table'),
    ("Visualization",       r'visualizer'),
    ("Implementation",      r'Optimal Implementation'),
]

REQUIRED_CSS = [
    ("main.css",       r'href="../css/main.css"'),
    ("components.css", r'href="../css/components.css"'),
    ("problem.css",    r'href="../css/problem.css"'),
]

import sys; sys.stdout.reconfigure(encoding='utf-8', errors='replace') if hasattr(sys.stdout, 'reconfigure') else None
print("=" * 60)
print("  CP-II WEBSITE - COMPREHENSIVE BUG AUDIT")
print("=" * 60)

section_issues = []
link_issues    = []
js_issues      = []
struct_issues  = []
nav_issues     = []

for f in problem_files:
    content = open(f, encoding="utf-8").read()
    bname   = os.path.basename(f)

    # --- Required sections present?
    for name, pat in REQUIRED_SECTIONS:
        if not re.search(pat, content, re.IGNORECASE):
            section_issues.append(f"  [{bname}]  MISSING section: '{name}'")

    # --- Required CSS links?
    for name, pat in REQUIRED_CSS:
        if not re.search(pat, content):
            struct_issues.append(f"  [{bname}]  MISSING CSS: {name}")

    # --- Prism (syntax highlighting) present?
    if "prism" not in content.lower():
        struct_issues.append(f"  [{bname}]  MISSING Prism syntax highlighter link")

    # --- main.js not linked (should be in global JS or inline)
    # (problem pages use inline JS so this is OK, skip)

    # --- Duplicate comparison tables?
    ct = len(re.findall(r'comparison-table', content))
    if ct > 1:
        struct_issues.append(f"  [{bname}]  DUPLICATE comparison-table ({ct} occurrences)")

    # --- Duplicate Approach Comparison headings?
    ac = len(re.findall(r'Approach Comparison', content, re.IGNORECASE))
    if ac > 1:
        struct_issues.append(f"  [{bname}]  DUPLICATE 'Approach Comparison' heading ({ac} occurrences)")

    # --- Multiple <h1> tags?
    h1_count = len(re.findall(r'<h1[\s>]', content))
    if h1_count != 1:
        struct_issues.append(f"  [{bname}]  Expected 1 <h1>, found {h1_count}")

    # --- Missing <title>?
    if not re.search(r'<title>[^<]+</title>', content):
        struct_issues.append(f"  [{bname}]  MISSING <title>")

    # --- Broken back-link? (should point to correct module)
    # derive expected module from filename e.g. m8-p3 -> module-08
    match = re.match(r'm(\d+)-p\d+\.html$', bname)
    if match:
        mnum = int(match.group(1))
        expected_module_pattern = f"module-{mnum:02d}"
        if expected_module_pattern not in content:
            nav_issues.append(f"  [{bname}]  Navbar back-link may not reference '{expected_module_pattern}'")

    # --- DOMContentLoaded in script? (all visualizers must have it)
    script_blocks = re.findall(r'<script>(.*?)</script>', content, re.DOTALL)
    for sb in script_blocks:
        # check for bare document.getElementById without DOMContentLoaded guard
        if 'getElementById' in sb and 'DOMContentLoaded' not in sb:
            js_issues.append(f"  [{bname}]  script block uses getElementById WITHOUT DOMContentLoaded guard")
            break

    # --- Unclosed <section> tags?
    open_sections  = len(re.findall(r'<section', content))
    close_sections = len(re.findall(r'</section>', content))
    if open_sections != close_sections:
        struct_issues.append(f"  [{bname}]  Mismatched <section> tags: {open_sections} open vs {close_sections} close")

    # --- Code tab switching JS present when multiple tabs exist?
    tab_count = len(re.findall(r'code-block__tab', content))
    if tab_count > 1:
        # must have tab switching logic
        if 'code-block__tab' not in content or 'active' not in content:
            js_issues.append(f"  [{bname}]  Multiple code tabs but no tab-switching logic detected")

    # --- TBD placeholders remaining?
    if re.search(r'\bTBD\b', content):
        section_issues.append(f"  [{bname}]  Contains 'TBD' placeholder – not fully implemented")

    # --- btn-reset or btn-step IDs without corresponding event listeners?
    if 'btn-reset' in content and "btn-reset" not in content.split('<script>',1)[-1]:
        js_issues.append(f"  [{bname}]  btn-reset found in HTML but no JS handler detected in script block")

# ──────────────────────────────────────────────
# 3. Per-file checks on MODULE pages
# ──────────────────────────────────────────────
module_link_issues = []
module_file_map = {}
for f in module_files:
    content = open(f, encoding='utf-8').read()
    bname   = os.path.basename(f)
    # collect links to problems
    links = re.findall(r'href=["\']([^"\']*m\d+-p\d+\.html)["\']', content)
    for link in links:
        # Resolve relative path
        link_name = os.path.basename(link)
        expected  = os.path.join(problems_dir, link_name).replace("\\", "/")
        if not os.path.exists(expected.replace("d:/", "d:\\")):
            module_link_issues.append(f"  [{bname}]  Broken link → '{link_name}' does not exist in problems/")

# ──────────────────────────────────────────────
# 4. Check problem links from index.html
# ──────────────────────────────────────────────
index_content = open("d:/CP_II_Website/index.html", encoding='utf-8').read()
index_links   = re.findall(r'href=["\']([^"\']*\.html)["\']', index_content)
index_issues  = []
for link in index_links:
    if link.startswith("modules/") or link.startswith("problems/"):
        full = "d:/" + "CP_II_Website/" + link.lstrip("/")
        full = full.replace("/", "\\")
        if not os.path.exists(full):
            index_issues.append(f"  [index.html]  Broken link → '{link}'")

# ──────────────────────────────────────────────
# 5. Check JS files for common issues
# ──────────────────────────────────────────────
js_file_issues = []
for jf in glob.glob("d:/CP_II_Website/js/*.js"):
    jcontent = open(jf, encoding='utf-8').read()
    jbname   = os.path.basename(jf)
    # Check for var (prefer const/let)
    var_count = len(re.findall(r'\bvar\b', jcontent))
    if var_count > 5:
        js_file_issues.append(f"  [{jbname}]  Uses 'var' {var_count}x — consider const/let")
    # undefined variable references (basic heuristic)
    if 'console.log' in jcontent:
        js_file_issues.append(f"  [{jbname}]  Contains console.log (debug leftovers?)")

# ──────────────────────────────────────────────
# 6. CSS variable consistency check
# ──────────────────────────────────────────────
css_issues = []
main_css = open("d:/CP_II_Website/css/main.css", encoding='utf-8').read()
defined_vars = set(re.findall(r'--([\w-]+)\s*:', main_css))
comp_css = open("d:/CP_II_Website/css/components.css", encoding='utf-8').read()
prob_css = open("d:/CP_II_Website/css/problem.css", encoding='utf-8').read()
all_css  = comp_css + prob_css
used_vars = set(re.findall(r'var\(--([\w-]+)\)', all_css))
undefined_used = used_vars - defined_vars
if undefined_used:
    for v in sorted(undefined_used):
        css_issues.append(f"  [CSS]  '--{v}' used in components/problem CSS but NOT defined in main.css")

# ──────────────────────────────────────────────
# 7. Print Report
# ──────────────────────────────────────────────
def print_section(title, items):
    if items:
        print(f"\n{'='*60}")
        print(f"  [!]  {title} ({len(items)} issues)")
        print(f"{'='*60}")
        for i in items:
            print(i)
    else:
        print(f"\n  [OK]  {title}: No Issues")

print_section("Missing/Incomplete Sections", section_issues)
print_section("HTML Structure Issues", struct_issues)
print_section("Navigation / Back-link Issues", nav_issues)
print_section("JavaScript Issues", js_issues)
print_section("Module → Problem Link Issues", module_link_issues)
print_section("Index.html Link Issues", index_issues)
print_section("JS File Quality", js_file_issues)
print_section("CSS Variable Issues", css_issues)

total = len(section_issues)+len(struct_issues)+len(nav_issues)+len(js_issues)+len(module_link_issues)+len(index_issues)+len(js_file_issues)+len(css_issues)
print(f"\n{'='*60}")
print(f"  TOTAL ISSUES FOUND: {total}")
print(f"{'='*60}\n")
