import sys
import re

def update_deportes():
    file_path = "c:/Users/Nigonz/OneDrive/Documentos/nylon/nylon-web 14-07 - copia/deportes.html"
    with open(file_path, "r", encoding="utf-8", errors='ignore') as f:
        content = f.read()

    # 1. Update Title HTML
    content = re.sub(r'SECTOR\s*-\s*<em>EVENTOS</em>', r'Sector <em>Eventos</em>', content, flags=re.IGNORECASE)
    
    # 2. Update Subtitle HTML
    content = re.sub(r'Porque como se capta lo irrepetible, si importa\.', r'Porque cómo se capta lo irrepetible, sí importa.', content, flags=re.IGNORECASE)

    # 3. Update CSS for .nc-name
    # font-family: 'Playfair Display', serif;
    old_name_css = r"\.nc-name\s*\{[\s\S]*?\}"
    new_name_css = """.nc-name{
  font-family:'Playfair Display',serif;
  font-size:clamp(28px,4.5vw,52px);
  font-weight:700;letter-spacing:-1.5px;line-height:1.0;
}"""
    content = re.sub(old_name_css, new_name_css, content)

    # 4. Update CSS for .nc-name em
    old_name_em_css = r"\.nc-name em\s*\{[\s\S]*?\}"
    new_name_em_css = """.nc-name em{
  font-style:normal;
  background:linear-gradient(135deg, #00756d, #00756c);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
}"""
    content = re.sub(old_name_em_css, new_name_em_css, content)

    # 5. Update CSS for .nc-sub (to match .hero-subtitle)
    old_sub_css = r"\.nc-sub\s*\{[\s\S]*?\}"
    new_sub_css = """.nc-sub{
  font-family:'Cormorant Garamond',serif;
  font-size:28px;
  font-weight:500;
  font-style:italic;
  letter-spacing:0.5px;
  color:rgba(255,255,255,0.95);
  margin-bottom:24px;
  line-height:1.4;
  text-shadow:0 2px 10px rgba(0,0,0,0.8);
  margin-top:12px;
}"""
    content = re.sub(old_sub_css, new_sub_css, content)

    # 6. Update CSS for .nc-tag (Buttons)
    old_tag_css = r"\.nc-tag\s*\{[\s\S]*?\}"
    new_tag_css = """.nc-tag{
  font-family:'Space Grotesk',sans-serif;
  font-size:10px;
  font-weight:700;
  letter-spacing:2px;
  text-transform:uppercase;
  padding:12px 24px;
  background:transparent;
  border:1px solid #00756c;
  color:#00756c;
  border-radius:6px;
  cursor:pointer;
  transition:all 0.3s ease;
  display:inline-block;
}
.nc-tag:hover{
  background:rgba(0,117,108,0.1);
  border-color:#02968d;
  color:#02968d;
  box-shadow:0 0 20px rgba(0,117,108,0.25);
}"""
    # Note: the original file might not have a hover state for nc-tag explicitly, so replacing .nc-tag with both works well.
    content = re.sub(old_tag_css, new_tag_css, content)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated deportes.html successfully.")

if __name__ == "__main__":
    update_deportes()
