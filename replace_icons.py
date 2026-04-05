import os
import re

dir_path = r"D:\projects\Forensic Accounting Firm"

# Map of some icon concepts to Unsplash image IDs for relevance
image_map = {
    'scale-balanced': '1589829085413-56de8ae18c73', # scales of justice
    'magnifying-glass-chart': '1551288049-bebda4e38f71', 
    'gavel': '1589829085413-56de8ae18c73',
    'file-invoice': '1554224155-8d04cb21cd6c',
    'sack-dollar': '1580519542036-ed5d6906aeb9',
    'chart-pie': '1551288049-bebda4e38f71',
    'house-chimney-crack': '1605810230434-7631ac76ec81',
    
    # Industries
    'gavel': '1589829085413-56de8ae18c73',
    'industry': '1581091226825-a6a2a5aee158',
    'building-columns': '1541359927273-d8c7c0062a4a',
    'tractor': '1592982537443-d1e462ad5f0b',
    'wheat-awn': '1592982537443-d1e462ad5f0b',
    'money-bill': '1580519542036-ed5d6906aeb9',
    'money-bill-transfer': '1580519542036-ed5d6906aeb9',
    'user-ninja': '1553531384-e910609b119c',
    'eye-slash': '1614064641983-4a171c6dd1f5',
    'truck-medical': '1516549655169-df83a0774514',
    'shield-halved': '1563986768609-322da13575f3',
    'magnifying-glass': '1581091226825-a6a2a5aee158',
    
    # Generic fallback
    'default': '1454165804606-c3d57bc86b40'
}

def get_image_url(icon_class):
    for key, val in image_map.items():
        if key in icon_class:
            return f"https://images.unsplash.com/photo-{val}?auto=format&fit=crop&q=80&w=150&h=150"
    return f"https://images.unsplash.com/photo-{image_map['default']}?auto=format&fit=crop&q=80&w=150&h=150"

favicon_img = "https://images.unsplash.com/photo-1589829085413-56de8ae18c73?auto=format&fit=crop&q=80&w=32&h=32"
logo_img = "https://images.unsplash.com/photo-1589829085413-56de8ae18c73?auto=format&fit=crop&q=80&w=64&h=64"

for file in os.listdir(dir_path):
    if file.endswith('.html'):
        filepath = os.path.join(dir_path, file)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Replace emoji favicon
        # <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>⚖️</text></svg>">
        content = re.sub(
            r'<link rel="icon" type="image/svg\+xml" href="data:image[^>]+>',
            f'<link rel="icon" type="image/jpeg" href="{favicon_img}">',
            content
        )

        # 2. Replace brand-logo scale-balanced icon
        content = re.sub(
            r'<i class="fa-solid fa-scale-balanced"[^>]*></i>',
            f'<img src="{logo_img}" alt="Logo" style="width: 32px; height: 32px; border-radius: 50%; object-fit: cover;">',
            content
        )

        # 3. Replace card icons
        # <div class="card-icon"><i class="fa-solid fa-industry"></i></div>
        def replace_card_icon(match):
            icon_class = match.group(1)
            img_url = get_image_url(icon_class)
            return f'<div class="card-image-wrap" style="text-align: center; margin-bottom: 1.5rem;"><img src="{img_url}" alt="Icon" style="width: 64px; height: 64px; border-radius: 8px; object-fit: cover; margin: 0 auto; box-shadow: 0 4px 6px rgba(0,0,0,0.1);"></div>'
        
        content = re.sub(
            r'<div class="card-icon">\s*<i class="([^"]+)"></i>\s*</div>',
            replace_card_icon,
            content
        )

        # 4. In case of standalone huge icons (like emergency response)
        # <i class="fa-solid fa-truck-medical" style="font-size: 6rem; color: var(--secondary-color);"></i>
        def replace_huge_icon(match):
            icon_class = match.group(1)
            img_url = get_image_url(icon_class)
            return f'<img src="{img_url}" alt="Feature" style="width: 150px; height: 150px; border-radius: 12px; object-fit: cover; box-shadow: 0 10px 15px rgba(0,0,0,0.2); margin: 0 auto;">'
        
        content = re.sub(
            r'<i class="([^"]+)" style="font-size: 6rem;[^"]*"></i>',
            replace_huge_icon,
            content
        )
        
        # 5. Resource icons (file-pdf, newspaper, circle-question)
        content = re.sub(
            r'<i class="fa-solid fa-file-pdf"></i>',
            f'<img src="{get_image_url("file-invoice")}" alt="PDF" style="width: 48px; height: 48px; object-fit: cover; border-radius: 4px;">',
            content
        )
        content = re.sub(
            r'<i class="fa-solid fa-newspaper"></i>',
            f'<img src="{get_image_url("file-invoice")}" alt="News" style="width: 48px; height: 48px; object-fit: cover; border-radius: 4px;">',
            content
        )
        content = re.sub(
            r'<i class="fa-solid fa-circle-question"></i>',
            f'<img src="{get_image_url("magnifying-glass")}" alt="Question" style="width: 48px; height: 48px; object-fit: cover; border-radius: 4px;">',
            content
        )

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Processed {file}")
