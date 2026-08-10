import sys
import re

def update_deportes_css():
    file_path = "c:/Users/Nigonz/OneDrive/Documentos/nylon/nylon-web 14-07 - copia/deportes.html"
    with open(file_path, "r", encoding="utf-8", errors='ignore') as f:
        content = f.read()

    # We need to change max-width:800px to max-width:550px
    # and gap:30px to gap:80px specifically inside .vgrid

    # Let's extract the .vgrid block and replace within it to be safe
    def repl_vgrid(match):
        block = match.group(0)
        block = re.sub(r'max-width:\s*800px;', 'max-width:550px;', block)
        block = re.sub(r'gap:\s*30px;', 'gap:80px;', block)
        return block

    content = re.sub(r'\.vgrid\s*\{[\s\S]*?\}', repl_vgrid, content)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated deportes.html CSS successfully.")

if __name__ == "__main__":
    update_deportes_css()
