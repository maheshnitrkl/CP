import glob, re, os
tables = {}
for f in glob.glob('d:/CP_II_Website/problems/m[89]*.html'):
    content = open(f, encoding='utf-8').read()
    match = re.search(r'(<table class=\"comparison-table\".*?</table>)', content, re.DOTALL)
    if match:
        table_html = match.group(1).strip()
        table_html = re.sub(r'\s+', ' ', table_html)
        if table_html in tables:
            print(f'DUPLICATE TABLE FOUND: {os.path.basename(f)} is identical to {tables[table_html]}')
        else:
            tables[table_html] = os.path.basename(f)
