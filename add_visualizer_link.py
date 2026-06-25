#!/usr/bin/env python3
import glob, re, sys, os

sys.stdout.reconfigure(encoding='utf-8', errors='replace') if hasattr(sys.stdout, 'reconfigure') else None

BASE = "d:/CP_II_Website"

def process_file(filepath, link_path):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already added
    if 'visualizer.html' in content:
        return False
        
    # We want to insert: <a href="link_path" class="navbar__link">🔍 Visualizer</a>
    # just before the closing </div> of navbar__nav
    
    # Let's find the compiler link and insert after it.
    # e.g. <a href="../compiler.html" class="navbar__link">💻 Compiler</a>
    
    match = re.search(r'(<a[^>]+href=["\'][^"\']*compiler\.html["\'][^>]*>.*?</a>)', content)
    if match:
        insertion = f'{match.group(1)}<a href="{link_path}" class="navbar__link">🔍 Visualizer</a>'
        new_content = content.replace(match.group(1), insertion)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8', newline='\n') as f:
                f.write(new_content)
            print(f"Added to {os.path.basename(filepath)}")
            return True
            
    return False

def main():
    count = 0
    # Process index.html
    if process_file(f"{BASE}/index.html", "visualizer.html"):
        count += 1
        
    # Process modules
    for f in glob.glob(f"{BASE}/modules/*.html"):
        if process_file(f, "../visualizer.html"):
            count += 1
            
    # Process problems
    for f in glob.glob(f"{BASE}/problems/*.html"):
        if process_file(f, "../visualizer.html"):
            count += 1
            
    print(f"Modified {count} files.")

if __name__ == '__main__':
    main()
