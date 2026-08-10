import sys
import re

def update_deportes_content():
    file_path = "c:/Users/Nigonz/OneDrive/Documentos/nylon/nylon-web 14-07 - copia/deportes.html"
    with open(file_path, "r", encoding="utf-8", errors='ignore') as f:
        content = f.read()

    # We have two identical vsec sections in the code currently.
    # The first one is Eventos Corporativos. The second is Eventos Deportivos.
    # We will find them by the headers that precede them.

    # 1. Update Corporativos
    # Card 1:
    corp_pattern = r'(<h2>Eventos Corporativos</h2>[\s\S]*?)(data-video-id=")\d+("[\s\S]*?<div class="vf-title">).*?(</div>)'
    content = re.sub(corp_pattern, r'\g<1>\g<2>1209349157\g<3>AUTOCLÁSICA\g<4>', content, count=1)
    
    # Card 2: (Find next occurrence after Corporativos header)
    corp_pattern2 = r'(<h2>Eventos Corporativos</h2>[\s\S]*?1209349157[\s\S]*?AUTOCLÁSICA[\s\S]*?)(data-video-id=")\d+("[\s\S]*?<div class="vf-title">).*?(</div>)'
    content = re.sub(corp_pattern2, r'\g<1>\g<2>1209353385\g<3>EXPOAGRO\g<4>', content, count=1)

    # 2. Update Deportivos
    dep_pattern = r'(<h2>Eventos Deportivos</h2>[\s\S]*?)(data-video-id=")\d+("[\s\S]*?<div class="vf-title">).*?(</div>)'
    content = re.sub(dep_pattern, r'\g<1>\g<2>1209355022\g<3>Recap - Travel Fest\g<4>', content, count=1)
    
    dep_pattern2 = r'(<h2>Eventos Deportivos</h2>[\s\S]*?1209355022[\s\S]*?Travel Fest[\s\S]*?)(data-video-id=")\d+("[\s\S]*?<div class="vf-title">).*?(</div>)'
    content = re.sub(dep_pattern2, r'\g<1>\g<2>1133974487\g<3>Total Energies\g<4>', content, count=1)

    # 3. Add fetch for thumbnails inside initVideoFacades
    old_js = r"(const videoId = facade\.dataset\.videoId;\s*if \(!videoId\) return;)"
    new_js = r"""\1

    fetch(`https://vimeo.com/api/v2/video/${videoId}.json`)
      .then(r => r.json())
      .then(d => {
        if(d && d[0] && d[0].thumbnail_large) {
          facade.style.backgroundImage = 'url(' + d[0].thumbnail_large + ')';
          facade.style.backgroundSize = 'cover';
          facade.style.backgroundPosition = 'center';
        }
      }).catch(e => console.error(e));
"""
    content = re.sub(old_js, new_js, content)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated content and script successfully.")

if __name__ == "__main__":
    update_deportes_content()
