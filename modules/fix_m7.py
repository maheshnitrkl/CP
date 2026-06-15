import re

filename = r"d:\CP_II_Website\modules\module-07-linked-list-2.html"

with open(filename, "r", encoding="utf-8") as f:
    content = f.read()

# We want to replace `<` with `&lt;` ONLY inside `<pre><code...>` and `</code></pre>` blocks.
def escape_code_block(match):
    prefix = match.group(1)
    code = match.group(2)
    suffix = match.group(3)
    
    code = re.sub(r'<(?!\/?(?:pre|code|span|div)[>\s])', '&lt;', code)
    code = code.replace("&lt;lt;", "&lt;") # just in case
    return prefix + code + suffix

new_content = re.sub(r'(<pre><code[^>]*>)(.*?)(</code></pre>)', escape_code_block, content, flags=re.DOTALL)

# Add IDs to the problem cards
new_content = new_content.replace(
    '<a href="../problems/m7-p1.html" class="problem-card problem-card--link"',
    '<a href="../problems/m7-p1.html" id="p1" class="problem-card problem-card--link"'
)
new_content = new_content.replace(
    '<a href="../problems/m7-p2.html" class="problem-card problem-card--link"',
    '<a href="../problems/m7-p2.html" id="p2" class="problem-card problem-card--link"'
)
new_content = new_content.replace(
    '<a href="../problems/m7-p3.html" class="problem-card problem-card--link"',
    '<a href="../problems/m7-p3.html" id="p3" class="problem-card problem-card--link"'
)
new_content = new_content.replace(
    '<a href="../problems/m7-p4.html" class="problem-card problem-card--link"',
    '<a href="../problems/m7-p4.html" id="p4" class="problem-card problem-card--link"'
)
new_content = new_content.replace(
    '<a href="../problems/m7-p5.html" class="problem-card problem-card--link"',
    '<a href="../problems/m7-p5.html" id="p5" class="problem-card problem-card--link"'
)
new_content = new_content.replace(
    '<a href="../problems/m7-p6.html" class="problem-card problem-card--link"',
    '<a href="../problems/m7-p6.html" id="p6" class="problem-card problem-card--link"'
)

with open(filename, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Done fixing module-07-linked-list-2.html")
