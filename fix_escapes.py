import os
import glob
import re

def escape_code_blocks(html_content):
    # Pattern to match <code class="...">...</code> or just <code>...</code>
    # Use re.DOTALL to match across newlines
    pattern = re.compile(r'(<code[^>]*>)(.*?)(</code>)', re.DOTALL)
    
    def replacer(match):
        open_tag = match.group(1)
        code_content = match.group(2)
        close_tag = match.group(3)
        
        # First, unescape to avoid double escaping
        code_content = code_content.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')
        
        # Now escape properly
        code_content = code_content.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        
        return open_tag + code_content + close_tag

    return pattern.sub(replacer, html_content)

def main():
    modules_dir = r"d:\CP_II_Website\modules"
    files = glob.glob(os.path.join(modules_dir, "*.html"))
    
    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = escape_code_blocks(content)
        
        if content != new_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed {os.path.basename(file_path)}")
        else:
            print(f"No changes for {os.path.basename(file_path)}")

if __name__ == "__main__":
    main()
