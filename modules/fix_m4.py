import re

filename = r"d:\CP_II_Website\modules\module-04-sorting.html"

with open(filename, "r", encoding="utf-8") as f:
    content = f.read()

# We want to replace `<` with `&lt;` ONLY inside `<pre><code...>` and `</code></pre>` blocks.
def escape_code_block(match):
    prefix = match.group(1)
    code = match.group(2)
    suffix = match.group(3)
    # Replace `<` with `&lt;`, BUT be careful not to replace already escaped `&lt;`
    # or tags if there are any, but inside code blocks there shouldn't be HTML tags
    # other than what we want to escape.
    # Actually, we might have `vector&lt;int&gt;` already.
    # So `&lt;` is already there. Let's just replace `< ` and `<n` and `<=` etc.
    # A safe way is to replace `<` that is not part of `&lt;` or `</`.
    # Wait, the easiest way is to just replace all `<` with `&lt;` and then replace `&lt;lt;` back if we double escaped, or just write a regex:
    code = code.replace("< ", "&lt; ").replace("<n", "&lt;n").replace("<=", "&lt;=").replace("<l", "&lt;l").replace("<r", "&lt;r").replace("< p", "&lt; p").replace("< h", "&lt; h")
    # Actually let's just do a proper regex for any `<` not followed by `pre`, `code`, `/code`, `span`, etc.
    code = re.sub(r'<(?!\/?(?:pre|code|span|div)[>\s])', '&lt;', code)
    # Re-fix `&lt;&lt;` if we broke it?
    code = code.replace("&lt;lt;", "&lt;") # just in case
    return prefix + code + suffix

new_content = re.sub(r'(<pre><code[^>]*>)(.*?)(</code></pre>)', escape_code_block, content, flags=re.DOTALL)

# Add IDs to the problem cards
new_content = new_content.replace(
    '<a href="../problems/m4-p1.html" class="problem-card problem-card--link"',
    '<a href="../problems/m4-p1.html" id="p1" class="problem-card problem-card--link"'
)
new_content = new_content.replace(
    '<a href="../problems/m4-p2.html" class="problem-card problem-card--link"',
    '<a href="../problems/m4-p2.html" id="p2" class="problem-card problem-card--link"'
)
new_content = new_content.replace(
    '<a href="../problems/m4-p3.html" class="problem-card problem-card--link"',
    '<a href="../problems/m4-p3.html" id="p3" class="problem-card problem-card--link"'
)
new_content = new_content.replace(
    '<a href="../problems/m4-p4.html" class="problem-card problem-card--link"',
    '<a href="../problems/m4-p4.html" id="p4" class="problem-card problem-card--link"'
)
new_content = new_content.replace(
    '<a href="../problems/m4-p5.html" class="problem-card problem-card--link"',
    '<a href="../problems/m4-p5.html" id="p5" class="problem-card problem-card--link"'
)
new_content = new_content.replace(
    '<a href="../problems/m4-p6.html" class="problem-card problem-card--link"',
    '<a href="../problems/m4-p6.html" id="p6" class="problem-card problem-card--link"'
)

with open(filename, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Done fixing module-04-sorting.html")
