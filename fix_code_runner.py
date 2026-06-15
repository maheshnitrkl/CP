#!/usr/bin/env python3
"""Fix missing code-runner.js in M10-M12 problem pages"""
import glob, os

files_to_fix = sorted(
    glob.glob('d:/CP_II_Website/problems/m10-*.html') +
    glob.glob('d:/CP_II_Website/problems/m11-*.html') +
    glob.glob('d:/CP_II_Website/problems/m12-*.html')
)

OLD = '<script src="../js/main.js"></script>'
NEW = '<script src="../js/main.js"></script>\n  <script src="../js/code-runner.js"></script>'

print(f'Files to fix: {len(files_to_fix)}')
fixed = 0
for f in files_to_fix:
    c = open(f, encoding='utf-8').read()
    if 'main.js' in c and 'code-runner.js' not in c:
        new_c = c.replace(OLD, NEW)
        if new_c != c:
            open(f, 'w', encoding='utf-8').write(new_c)
            print(f'  FIXED: {os.path.basename(f)}')
            fixed += 1
        else:
            print(f'  SKIP (pattern not found): {os.path.basename(f)}')
    else:
        print(f'  SKIP (already has it): {os.path.basename(f)}')

print(f'\nTotal fixed: {fixed}')
