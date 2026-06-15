import glob, re

files = glob.glob('d:/CP_II_Website/problems/m8-p[5-8].html') + glob.glob('d:/CP_II_Website/problems/m9-p*.html')

pattern = re.compile(r'^\s*<!-- 6\. Approach Comparison -->\s*<section class="problem-section">\s*<h2 class="problem-section__title"><span class="icon">.*?</span> Approach Comparison</h2>\s*<table class="comparison-table">[\s\S]*?</table>\s*</section>\s*', re.MULTILINE)

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content, num_subs = pattern.subn('', content)
    
    if num_subs > 0:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f'Fixed {f}')
    else:
        print(f'Pattern not found in {f}')
