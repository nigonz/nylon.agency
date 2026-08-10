import sys
import re

def update_deportes_landscape_css():
    file_path = "c:/Users/Nigonz/OneDrive/Documentos/nylon/nylon-web 14-07 - copia/deportes.html"
    with open(file_path, "r", encoding="utf-8", errors='ignore') as f:
        content = f.read()

    # 1. Update .vgrid
    def repl_vgrid(match):
        block = match.group(0)
        block = re.sub(r'max-width:\s*\d+px;', 'max-width:1100px;', block)
        block = re.sub(r'gap:\s*\d+px;', 'gap:40px;', block)
        return block
    content = re.sub(r'\.vgrid\s*\{[\s\S]*?\}', repl_vgrid, content)

    # 2. Update .vcard
    def repl_vcard(match):
        block = match.group(0)
        # Assuming original vcard has width:100% or just standard block stuff. We will inject flex.
        # It currently has: position:relative;border-radius:20px;overflow:hidden;background:var(--bg2);... width:100%;
        # We append the flex properties before the closing brace.
        if 'display:flex;' not in block:
            block = block.replace('}', '  display:flex;\n  flex-direction:row;\n  align-items:stretch;\n  padding:16px;\n}')
        return block
    content = re.sub(r'\.vcard\s*\{[\s\S]*?\}', repl_vcard, content)

    # 3. Update .vframe
    def repl_vframe(match):
        block = match.group(0)
        # Current: position:relative;width:100%;aspect-ratio:9 / 16;overflow:hidden;border-radius:20px 20px 0 0;background:#000;
        block = re.sub(r'width:\s*100%;', 'width:45%;\n  flex-shrink:0;', block)
        block = re.sub(r'border-radius:\s*[0-9px\s]+;', 'border-radius:12px;', block)
        return block
    content = re.sub(r'\.vframe\s*\{[\s\S]*?\}', repl_vframe, content)

    # 4. Update .vfooter
    def repl_vfooter(match):
        block = match.group(0)
        # Current: padding:20px 24px;border-top:1px solid rgba(26,143,160,.12);background:linear-gradient(to bottom,var(--bg2),#040614);
        block = re.sub(r'padding:\s*[0-9px\s]+;', 'padding:0 0 0 24px;', block)
        block = re.sub(r'border-top:\s*.*?;', 'border-top:none;', block)
        block = re.sub(r'background:\s*linear-gradient.*?;', 'background:transparent;', block)
        if 'display:flex;' not in block:
            block = block.replace('}', '  flex:1;\n  display:flex;\n  flex-direction:column;\n  justify-content:center;\n}')
        return block
    content = re.sub(r'\.vfooter\s*\{[\s\S]*?\}', repl_vfooter, content)

    # 5. Update .vf-title and .vf-sub text sizes
    def repl_vf_title(match):
        block = match.group(0)
        block = re.sub(r'font-size:\s*\d+px;', 'font-size:20px;', block)
        return block
    content = re.sub(r'\.vf-title\s*\{[\s\S]*?\}', repl_vf_title, content)
    
    def repl_vf_sub(match):
        block = match.group(0)
        block = re.sub(r'font-size:\s*\d+px;', 'font-size:13px;', block)
        return block
    content = re.sub(r'\.vf-sub\s*\{[\s\S]*?\}', repl_vf_sub, content)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated deportes.html landscape cards CSS successfully.")

if __name__ == "__main__":
    update_deportes_landscape_css()
