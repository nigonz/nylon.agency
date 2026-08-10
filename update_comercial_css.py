import sys
import re

def update_css():
    file_path = "c:/Users/Nigonz/OneDrive/Documentos/nylon/nylon-web 14-07 - copia/comercial.html"
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update :root palette
    content = re.sub(r'--teal-light:\s*#2abccc;', '--teal-light:#00756c;', content)
    content = re.sub(r'--cyan:\s*#00c8e0;', '--cyan:#00756d;', content)

    # 2. Update .hero-subtitle
    # Current: font-size:18px; font-weight:300; letter-spacing:0.3px; color:rgba(255,255,255,0.72);
    old_hero_sub = r"\.hero-subtitle\s*\{[\s\S]*?\}"
    new_hero_sub = """.hero-subtitle{
      font-family:'Cormorant Garamond',serif;
      font-size:28px;
      font-weight:500;
      font-style:italic;
      letter-spacing:0.5px;
      color:rgba(255,255,255,0.95);
      margin-bottom:32px;
      line-height:1.4;
      text-shadow:0 2px 10px rgba(0,0,0,0.8);
    }"""
    content = re.sub(old_hero_sub, new_hero_sub, content)

    # 3. Update Nav .logo
    old_logo = r"\.logo\s*\{[\s\S]*?\}"
    new_logo = """.logo{
      font-family:'Space Grotesk',sans-serif;
      font-size:16px;
      font-weight:600;
      letter-spacing:4px;
      color:rgba(5,215,218,0.8);
      text-transform:uppercase;
    }"""
    content = re.sub(old_logo, new_logo, content)

    # 4. Update .nav-links a
    old_nav_a = r"\.nav-links a\s*\{[\s\S]*?\}"
    new_nav_a = """.nav-links a{
      color:rgba(255,255,255,0.95);
      text-decoration:none;
      font-family:'Space Grotesk',sans-serif;
      font-size:15px;
      font-weight:500;
      letter-spacing:1px;
      text-transform:capitalize;
      transition:color 0.3s ease,text-shadow 0.3s ease;
      text-shadow:0 2px 4px rgba(0,0,0,0.8);
    }"""
    content = re.sub(old_nav_a, new_nav_a, content)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated CSS.")

if __name__ == "__main__":
    update_css()
