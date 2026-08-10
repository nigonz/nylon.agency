import sys
import re

def update_host_details():
    file_path = "c:/Users/Nigonz/OneDrive/Documentos/nylon/nylon-web 14-07 - copia/host.html"
    with open(file_path, "r", encoding="utf-8", errors='ignore') as f:
        content = f.read()

    # 1. Main Title
    # It might be "HOST <em>ON CAMERA TALENT</em>" or similar
    content = re.sub(r'HOST\s*<em>ON\s*CAMERA\s*TALENT</em>', r'NATALIA <em>GARAYGORTA</em>', content, flags=re.IGNORECASE)
    # Just in case it's not wrapped in em
    content = re.sub(r'>HOST ON CAMERA TALENT<', r'>NATALIA <em>GARAYGORTA</em><', content, flags=re.IGNORECASE)

    # 2. Subtitle
    content = re.sub(r'(<div class="nc-sub"[^>]*>.*?)Natalia Garaygorta(.*?</div>)', r'\1Periodista\2', content, flags=re.IGNORECASE)

    # 3. Buttons (nc-tag)
    # They are likely in <div class="nc-tags">...</div>
    # We will replace the text of the tags directly.
    content = re.sub(r'(<div class="nc-tag"[^>]*>)\s*(?:Host on Camera Talent|Actor|Host|Presentador)\s*(</div>)', r'\1HOST ON CAMERA TALENT\2', content, flags=re.IGNORECASE)
    content = re.sub(r'(<div class="nc-tag"[^>]*>)\s*(?:Project Manager|Producer|Director)\s*(</div>)', r'\1PROYECT MANAGER\2', content, flags=re.IGNORECASE)
    content = re.sub(r'(<div class="nc-tag"[^>]*>)\s*(?:Periodismo|Journalism|Writer)\s*(</div>)', r'\1PERIODISMO\2', content, flags=re.IGNORECASE)

    # Just in case the exact old text isn't found, let's grab all nc-tags in order and replace them:
    # First, try replacing all nc-tags if there are exactly 3
    tags = re.findall(r'<div class="nc-tag"[^>]*>.*?</div>', content)
    if len(tags) >= 3:
        new_tag1 = re.sub(r'>.*?</div>', '>HOST ON CAMERA TALENT</div>', tags[0])
        new_tag2 = re.sub(r'>.*?</div>', '>PROYECT MANAGER</div>', tags[1])
        new_tag3 = re.sub(r'>.*?</div>', '>PERIODISMO</div>', tags[2])
        
        content = content.replace(tags[0], new_tag1, 1)
        content = content.replace(tags[1], new_tag2, 1)
        content = content.replace(tags[2], new_tag3, 1)

    # 4. Color adjustments to #178d8f
    # .nc-name em gradient
    old_em_css = r"\.nc-name\s*em\s*\{[\s\S]*?\}"
    new_em_css = """.nc-name em{
  font-style:normal;
  background:linear-gradient(128deg, #ffffff, #178d8f, #0f5b5c);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
  text-shadow: 0 0 20px rgba(23,141,143,0.3);
}"""
    content = re.sub(old_em_css, new_em_css, content)

    # .nc-tag colors
    old_tag_css = r"\.nc-tag\s*\{[\s\S]*?\}"
    new_tag_css = """.nc-tag{
  padding:4px 16px;border-radius:20px;
  font-family:'Space Grotesk',sans-serif;font-size:10px;font-weight:700;letter-spacing:2px;text-transform:uppercase;
  background:rgba(23,141,143,0.1);border:1px solid #178d8f;color:#178d8f;
  transition:all 0.3s; cursor:pointer;
}
.nc-tag:hover{
  background:rgba(23,141,143,0.2);
  box-shadow:0 0 15px rgba(23,141,143,0.4);
}"""
    content = re.sub(old_tag_css, new_tag_css, content)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated host.html text and colors successfully.")

if __name__ == "__main__":
    update_host_details()
