import sys
import re

def update_nav():
    file_path = "c:/Users/Nigonz/OneDrive/Documentos/nylon/nylon-web 14-07 - copia/deportes.html"
    with open(file_path, "r", encoding="utf-8", errors='ignore') as f:
        content = f.read()

    # Replace top in nav
    content = re.sub(r'(nav\s*\{[\s\S]*?top:\s*)20px(;)', r'\g<1>8px\2', content)
    
    # Replace padding in nav
    content = re.sub(r'(nav\s*\{[\s\S]*?padding:\s*)15px(\s+30px\s*!important;)', r'\g<1>8px\2', content)
    
    # Replace min-height in nav
    content = re.sub(r'(nav\s*\{[\s\S]*?min-height:\s*)60px(;)', r'\g<1>48px\2', content)

    # Replace padding in .nav-links
    content = re.sub(r'(\.nav-links\s*\{[\s\S]*?padding:\s*)10px(\s+24px;)', r'\g<1>4px\2', content)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated deportes.html nav successfully.")

if __name__ == "__main__":
    update_nav()
