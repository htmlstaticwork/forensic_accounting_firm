import os
import re

dir_path = r"D:\projects\Forensic Accounting Firm"
updated = 0

for file in os.listdir(dir_path):
    if file.endswith('.html'):
        filepath = os.path.join(dir_path, file)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        desktop_nav_match = re.search(r'<ul class="nav-menu">.*?</ul>', content, re.DOTALL)
        if desktop_nav_match:
            desktop_nav = desktop_nav_match.group(0)
            if 'home-2.html' in desktop_nav:
                print(f'{file} already has Home 2 in desktop nav')
                continue
                
        # We need to insert after <li><a href="index.html" class="nav-link">Home</a></li>
        pattern = re.compile(r'(<ul[^>]*class="nav-menu"[^>]*>\s*(?:<!--.*?-->\s*)?<li><a href="index\.html"[^>]*>Home</a></li>)(\s*<li class="nav-item dropdown">)', re.DOTALL)
        
        new_class = 'nav-link active' if file == 'home-2.html' else 'nav-link'
        new_item = f'<li><a href="home-2.html" class="{new_class}">Home 2</a></li>'
        
        def rep(m):
            return m.group(1) + '\n                ' + new_item + m.group(2)
            
        new_content, count = pattern.subn(rep, content, count=1)
        
        if count > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            updated += 1
            print(f'Updated {file}')
        else:
            print(f'Pattern not found in {file}')

print(f'Total files updated: {updated}')
