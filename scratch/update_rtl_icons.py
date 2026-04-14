import os

search_text = '<i class="fa-solid fa-language"></i>'
replace_text = '<span class="rtl-toggle-text">RTL</span>'

files = [
    'index.html', 'about.html', 'case-studies.html', 'contact.html',
    'dashboard.html', 'dashboard-cases.html', 'dashboard-documents.html',
    'dashboard-messages.html', 'dashboard-settings.html', 'home-2.html',
    'how-it-works.html', 'industries.html', 'login.html', 'register.html',
    'resources.html', 'services.html'
]

for filename in files:
    path = os.path.join(os.getcwd(), filename)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if search_text in content:
            new_content = content.replace(search_text, replace_text)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
        else:
            print(f"Pattern not found in {filename}")
    else:
        print(f"File not found: {filename}")
