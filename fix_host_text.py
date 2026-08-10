import sys
import re

def fix_host_text():
    file_path = "c:/Users/Nigonz/OneDrive/Documentos/nylon/nylon-web 14-07 - copia/host.html"
    with open(file_path, "r", encoding="utf-8", errors='ignore') as f:
        content = f.read()

    # Title
    content = re.sub(r'Host - <em>On Camera Talent</em>', r'NATALIA <em>GARAYGORTA</em>', content, flags=re.IGNORECASE)

    # Note: subtitle is already Periodista in line 10. (Because my previous run probably missed the name but caught the subtitle? No, it looks like it might have already been Periodista or it was updated. Wait, "Abajo donde ahora dice natalia garaygorta debe decir Periodista". But line 10 says Periodista. If it's already there, no problem. Wait, let me make sure we don't have "Natalia Garaygorta" anywhere else).
    
    # Tags
    # <span class="nc-tag">UGC Creator</span> -> HOST ON CAMERA TALENT
    content = re.sub(r'<span class="nc-tag">\s*UGC Creator\s*</span>', r'<span class="nc-tag">HOST ON CAMERA TALENT</span>', content, flags=re.IGNORECASE)
    
    # <span class="nc-tag">Brand Experience</span> -> PROYECT MANAGER
    content = re.sub(r'<span class="nc-tag">\s*Brand Experience\s*</span>', r'<span class="nc-tag">PROYECT MANAGER</span>', content, flags=re.IGNORECASE)
    
    # <span class="nc-tag">Eventos</span> -> PERIODISMO
    content = re.sub(r'<span class="nc-tag">\s*Eventos\s*</span>', r'<span class="nc-tag">PERIODISMO</span>', content, flags=re.IGNORECASE)

    # Let me ensure the subtitle is Periodista if it wasn't. Line 10 was: <div class="nc-sub">Periodista</div>. The user said "Abajo donde ahora dice natalia garaygorta debe decir Periodista". Maybe I should search for "natalia garaygorta" and replace with "Periodista" globally just in case it's somewhere else in the hero.
    content = re.sub(r'>\s*Natalia Garaygorta\s*<', '>Periodista<', content, flags=re.IGNORECASE)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Fixed host.html text successfully.")

if __name__ == "__main__":
    fix_host_text()
