import sys
import re
import os
import glob

def update_global_colors():
    base_dir = "c:/Users/Nigonz/OneDrive/Documentos/nylon/nylon-web 14-07 - copia"
    files = glob.glob(os.path.join(base_dir, "*.html")) + glob.glob(os.path.join(base_dir, "*.css"))

    for file_path in files:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        new_content = content
        
        # We target specific color definitions in :root or anywhere they are defined globally
        # Usually they look like --cyan: #00e5ff; or --teal: #1a8fa0;
        # We will use regex to catch all hex/rgba variations of these exact variable names
        
        # Lighter Accent Teal: #02968d
        new_content = re.sub(r'(--teal-light|--teal-l)\s*:\s*(#[0-9a-fA-F]{3,8}|rgba?\([^)]+\));', r'\1: #02968d;', new_content)
        
        # Primary/Darker Teal: #00756c and #00756d
        new_content = re.sub(r'(--teal)\s*:\s*(#[0-9a-fA-F]{3,8}|rgba?\([^)]+\));', r'\1: #00756c;', new_content)
        new_content = re.sub(r'(--cyan)\s*:\s*(#[0-9a-fA-F]{3,8}|rgba?\([^)]+\));', r'\1: #00756d;', new_content)

        if new_content != content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated colors in: {os.path.basename(file_path)}")

if __name__ == "__main__":
    update_global_colors()
