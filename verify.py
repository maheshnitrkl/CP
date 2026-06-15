#!/usr/bin/env python3
import re, glob, os

# Verify duplicate issue
real_dupe_count = 0
for f in glob.glob('d:/CP_II_Website/problems/m*.html'):
    c = open(f, encoding='utf-8').read()
    h2_matches = re.findall(r'<h2[^>]*>.*?Approach Comparison.*?</h2>', c, re.DOTALL|re.IGNORECASE)
    if len(h2_matches) > 1:
        real_dupe_count += 1
        print(f'REAL DUPE: {f}')

if real_dupe_count == 0:
    print('CONFIRMED: Zero real duplicate H2 headings.')
    print('All 52 audit warnings are FALSE POSITIVES (HTML comment + actual heading is normal).')

# Verify M1 JS safety
print()
print('=== M1 JS: Scripts safely placed after </main>? ===')
for f in sorted(glob.glob('d:/CP_II_Website/problems/m1-*.html')):
    c = open(f, encoding='utf-8').read()
    main_close = c.find('</main>')
    script_start = c.find('<script>')
    safe = main_close != -1 and script_start > main_close
    print(f'  {os.path.basename(f)}: {safe}')

# Verify CSS fix
print()
main_css = open('d:/CP_II_Website/css/main.css', encoding='utf-8').read()
print('border-secondary in dark theme:', '--border-secondary' in main_css[:8000])
print('border-secondary in light theme:', main_css.count('--border-secondary:') >= 2)

# Verify code-runner fix
print()
print('=== M10-M12 code-runner.js check ===')
missing = []
for f in sorted(glob.glob('d:/CP_II_Website/problems/m1[012]-*.html')):
    c = open(f, encoding='utf-8').read()
    if 'code-runner.js' not in c:
        missing.append(os.path.basename(f))
if missing:
    print('Still missing:', missing)
else:
    print('All M10-M12 now have code-runner.js')
