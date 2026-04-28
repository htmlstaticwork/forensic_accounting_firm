import os
import re

def update_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace theme-toggle ID with class
    content = re.sub(r'id="theme-toggle"', r'class="theme-toggle-btn theme-toggle"', content)
    # Remove redundant class if it exists after ID replacement
    content = re.sub(r'class="theme-toggle-btn theme-toggle"\s+class="theme-toggle-btn"', r'class="theme-toggle-btn theme-toggle"', content)
    # Handle cases where class was already there
    content = re.sub(r'class="theme-toggle-btn"\s+class="theme-toggle-btn theme-toggle"', r'class="theme-toggle-btn theme-toggle"', content)

    # 2. Replace rtl-toggle ID with class
    content = re.sub(r'id="rtl-toggle"', r'class="theme-toggle-btn rtl-toggle"', content)
    content = re.sub(r'class="theme-toggle-btn rtl-toggle"\s+class="theme-toggle-btn"', r'class="theme-toggle-btn rtl-toggle"', content)
    content = re.sub(r'class="theme-toggle-btn"\s+class="theme-toggle-btn rtl-toggle"', r'class="theme-toggle-btn rtl-toggle"', content)

    # 3. Add mobile toggles to mobile-nav if present
    mobile_nav_toggles = """        <div class="mobile-nav-toggles">
            <button class="theme-toggle-btn theme-toggle" aria-label="Toggle Dark Mode">
                <i class="fa-solid fa-circle-half-stroke"></i> Theme
            </button>
            <button class="theme-toggle-btn rtl-toggle" aria-label="Toggle RTL Mode">
                <span class="rtl-toggle-text">RTL</span> Layout
            </button>
        </div>"""
    
    if '<div id="mobile-nav" class="mobile-nav">' in content:
        if 'mobile-nav-toggles' not in content:
            # Find the closing </ul> of the nav-menu inside mobile-nav
            parts = content.split('<div id="mobile-nav" class="mobile-nav">')
            nav_part = parts[1]
            # Find the first </ul>
            ul_end_index = nav_part.find('</ul>')
            if ul_end_index != -1:
                new_nav_part = nav_part[:ul_end_index+5] + "\n" + mobile_nav_toggles + nav_part[ul_end_index+5:]
                content = parts[0] + '<div id="mobile-nav" class="mobile-nav">' + new_nav_part

    # 4. Handle Dashboard Sidebar specifically
    if '<aside class="dashboard-sidebar"' in content:
        if 'mobile-nav-toggles' not in content:
            # Add before Logout in sidebar-footer
            sidebar_toggles = """            <div class="mobile-nav-toggles" style="margin-bottom: 1rem; border-top: none; padding-top: 0;">
                <button class="theme-toggle-btn theme-toggle" aria-label="Toggle Dark Mode">
                    <i class="fa-solid fa-circle-half-stroke"></i>
                </button>
                <button class="theme-toggle-btn rtl-toggle" aria-label="Toggle RTL Mode">
                    <span class="rtl-toggle-text">RTL</span>
                </button>
            </div>"""
            content = content.replace('<div class="sidebar-footer">', '<div class="sidebar-footer">\n' + sidebar_toggles)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for filename in os.listdir('.'):
    if filename.endswith('.html'):
        update_html(filename)
