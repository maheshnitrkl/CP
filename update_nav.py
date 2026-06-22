import os
import glob

# Add Compiler link to index.html
index_file = "d:/CP_II_Website/index.html"
with open(index_file, "r", encoding="utf-8") as f:
    content = f.read()

# For index.html
if '💻 Compiler' not in content:
    content = content.replace(
        '<a href="#resources" class="navbar__link">📖 Resources</a>',
        '<a href="#resources" class="navbar__link">📖 Resources</a>\n        <a href="compiler.html" class="navbar__link">💻 Compiler</a>'
    )
    with open(index_file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {index_file}")

# Update modules pages
module_files = glob.glob("d:/CP_II_Website/modules/*.html")
for file in module_files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    if '💻 Compiler' not in content:
        content = content.replace(
            '<a href="#problems" class="navbar__link">💡 Problems</a>',
            '<a href="#problems" class="navbar__link">💡 Problems</a><a href="../compiler.html" class="navbar__link">💻 Compiler</a>'
        )
        with open(file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {file}")

# Update problems pages
problem_files = glob.glob("d:/CP_II_Website/problems/*.html")
for file in problem_files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    if '💻 Compiler' not in content:
        # Find the closing div of the navbar__nav
        # It looks like: <div class="navbar__nav"><a href="...">...</a></div>
        if '<div class="navbar__nav">' in content:
            # We'll split by `<div class="navbar__actions">` and insert before it
            # The structure is: <div class="navbar__nav">...</div><div class="navbar__actions">
            parts = content.split('<div class="navbar__actions">')
            if len(parts) == 2:
                # We need to add the link inside the navbar__nav div.
                # Let's replace the closing </div> of navbar__nav instead.
                # Actually, easier to do regex or simple string replacement.
                # Look for `</a></div><div class="navbar__actions">`
                if '</a></div><div class="navbar__actions">' in content:
                     content = content.replace(
                         '</a></div><div class="navbar__actions">',
                         '</a><a href="../compiler.html" class="navbar__link" style="margin-left: 1rem;">💻 Compiler</a></div><div class="navbar__actions">'
                     )
                else:
                    # Some files might have different formatting, let's just do a blanket replace if possible
                    # Or insert right before `<div class="navbar__actions">`
                    # Since we know `navbar__nav` and `navbar__actions` are siblings
                    # Wait, if we put it outside `navbar__nav`, it breaks flex layout.
                    pass
        
        with open(file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {file}")

print("Done updating navbars.")
