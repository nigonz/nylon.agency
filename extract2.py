import re
import io
import sys

def extract():
    with open('c:/Users/Nigonz/OneDrive/Documentos/nylon/nylon-web 14-07 - copia/comercial.html', 'r', encoding='utf-8') as f:
        c = f.read()

    print("=== HTML vsec ===")
    m1 = re.search(r'(<section class="vsec">.*?</section>)', c, re.DOTALL)
    if m1: 
        print(m1.group(1))

    print("\n=== CSS vgrid ===")
    m2 = re.search(r'(\.vgrid\s*\{[\s\S]*?/\*\s*═══\s*VIDEO FACADE)', c)
    if m2:
        print(m2.group(1))

    print("\n=== JS ===")
    m3 = re.search(r'(/\* ═══════════════════════════════════════════\s*VIDEO PLAYER — FUNCIONAL[\s\S]*?\}\)\(\);)', c)
    if m3:
        print(m3.group(1))

if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    extract()
