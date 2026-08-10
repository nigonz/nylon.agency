import sys
import re

def update_deportes_layout():
    file_path = "c:/Users/Nigonz/OneDrive/Documentos/nylon/nylon-web 14-07 - copia/deportes.html"
    with open(file_path, "r", encoding="utf-8", errors='ignore') as f:
        content = f.read()

    # 1. Hero Spacing
    # .hero{...}
    content = re.sub(r'(\.hero\s*\{[\s\S]*?)(\})', r'\1  padding-top: 60px;\n\2', content, count=1)

    # 2. Section Renaming
    content = content.replace("<h2>Transmisiones</h2>", "<h2>Eventos Corporativos</h2>")
    content = content.replace("<h2>Fragmentos del Universo</h2>", "<h2>Eventos Deportivos</h2>")

    # 3. CSS for Grid
    # Update .vgrid to 2 columns and max-width 800px
    old_vgrid = r"\.vgrid\s*\{[\s\S]*?\}"
    new_vgrid = """.vgrid{
  display:grid;
  grid-template-columns:repeat(2, 1fr);
  gap:30px;
  max-width:800px;
  margin:0 auto;
  perspective:1400px;
  perspective-origin:50% 30%;
}"""
    content = re.sub(old_vgrid, new_vgrid, content)

    # Change .vframe aspect ratio to 9/16 globally since all videos are vertical here
    content = re.sub(r'aspect-ratio:\s*16\s*/\s*9;', 'aspect-ratio: 9 / 16;', content)
    # Remove any specific 9/16 overrides since the default is now 9/16
    content = re.sub(r'/\*\s*Verticales:.*?\*/[\s\S]*?aspect-ratio:\s*9\s*/\s*16;\s*\}', '', content)

    # Remove photo CSS
    content = re.sub(r'/\*\s*══════════════════════════════════════════\s*PHOTOS\s*══════════════════════════════════════════\s*\*/[\s\S]*?(?=/\*\s*══════════════════════════════════════════\s*FLOAT ANIMATIONS)', '', content)

    # Remove lightbox CSS
    content = re.sub(r'/\*\s*══════════════════════════════════════════\s*LIGHTBOX\s*══════════════════════════════════════════\s*\*/[\s\S]*?(?=/\*\s*══════════════════════════════════════════\s*RESPONSIVE)', '', content)

    # 4. HTML structure replacement
    # We will replace from <section class="vsec"> all the way to before <!-- MAIN END --> or <footer>
    # Wait, the structure is:
    # <section class="vsec"> ... </section>
    # <h2>Fragmentos...</h2>
    # <section class="psec"> ... </section>
    # We need to construct two identical <section class="vsec"> with 2 cards each.
    
    video_card_html = """
      <div class="fw reveal" style="--delay:0s;--dur:6.8s;--fa:float-a">
        <div class="vcard tilt">
          <div class="vframe">
            <div class="video-facade" data-video-id="22439234">
              <div class="video-facade-play-btn">
                <svg viewBox="0 0 24 24"><polygon points="5,3 19,12 5,21"/></svg>
              </div>
            </div>
          </div>
          <div class="vfooter">
            <div class="vf-title">Video 1</div>
            <div class="vf-sub">Contenido · 2024</div>
          </div>
        </div>
      </div>
      <div class="fw reveal" style="--delay:0.65s;--dur:8.1s;--fa:float-b">
        <div class="vcard tilt">
          <div class="vframe">
            <div class="video-facade" data-video-id="76979871">
              <div class="video-facade-play-btn">
                <svg viewBox="0 0 24 24"><polygon points="5,3 19,12 5,21"/></svg>
              </div>
            </div>
          </div>
          <div class="vfooter">
            <div class="vf-title">Video 2</div>
            <div class="vf-sub">Contenido · 2024</div>
          </div>
        </div>
      </div>
"""

    new_html_sections = f"""
  <section class="vsec">
    <div class="vgrid">
{video_card_html}
    </div>
  </section>

  <div class="sec-hd reveal" style="margin-top:12px">
    <div class="sec-orb">◈</div>
    <h2>Eventos Deportivos</h2>
    <div class="sec-line"></div>
  </div>

  <section class="vsec">
    <div class="vgrid">
{video_card_html}
    </div>
  </section>
"""

    # We match from <section class="vsec"> up to the end of <section class="psec">
    pattern_html = r'<section class="vsec">[\s\S]*?</section>\s*<!-- ═══ PHOTOS ═══ -->\s*<div class="sec-hd reveal" style="margin-top:12px">\s*<div class="sec-orb">◈</div>\s*<h2>Eventos Deportivos</h2>\s*<div class="sec-line"></div>\s*</div>\s*<section class="psec">[\s\S]*?</section>'
    
    # Wait, the <h2> is now "Eventos Deportivos" because I already string-replaced it above.
    
    content = re.sub(pattern_html, new_html_sections.replace('\\', '\\\\'), content)

    # 5. Remove Lightbox HTML
    content = re.sub(r'<!-- LIGHTBOX -->[\s\S]*?</div>', '', content)
    
    # 6. Remove Lightbox JS (bottom of file)
    content = re.sub(r'// ── LIGHTBOX ──[\s\S]*?(?=// ── VIDEO)', '', content)
    
    # 7. Remove Constellation JS
    content = re.sub(r'// ── CONSTELLATION ──[\s\S]*?(?=// ── LIGHTBOX)', '', content)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated deportes.html layout successfully.")

if __name__ == "__main__":
    update_deportes_layout()
