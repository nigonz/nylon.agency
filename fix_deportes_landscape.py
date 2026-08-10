import sys
import re

def fix_deportes_landscape_css():
    file_path = "c:/Users/Nigonz/OneDrive/Documentos/nylon/nylon-web 14-07 - copia/deportes.html"
    with open(file_path, "r", encoding="utf-8", errors='ignore') as f:
        content = f.read()

    new_vgrid = """.vgrid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 30px;
  max-width: 1100px;
  margin: 0 auto;
  perspective: 1400px;
}"""

    new_vcard = """.vcard {
  display: flex;
  flex-direction: row;
  background: var(--bg2);
  border: 1px solid rgba(26,143,160,.16);
  border-radius: 16px;
  height: 280px;
  overflow: hidden;
  box-shadow: var(--cshadow);
  transition: transform 0.4s ease, box-shadow 0.4s ease;
  transform-style: preserve-3d;
  will-change: transform;
}"""

    new_vframe = """.vframe {
  height: 100%;
  aspect-ratio: 9 / 16;
  position: relative;
  flex-shrink: 0;
  background: #000;
  border-radius: 0;
}"""

    new_vfooter = """.vfooter {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 0 30px;
  background: transparent;
  border-top: none;
  border-left: 1px solid rgba(26,143,160,.14);
}"""

    content = re.sub(r'\.vgrid\s*\{[\s\S]*?\}', new_vgrid, content, count=1)
    # Be careful not to replace hover states if they exist separately, but the regex targets the main class.
    # Wait, there might be .vcard:hover. Let's strictly replace the exact class block: \.vcard\s*\{...\}
    # Our regex captures everything up to the first closing brace, which is correct for standard CSS formatting.
    content = re.sub(r'\.vcard\s*\{[^\}]*?\}', new_vcard, content, count=1)
    content = re.sub(r'\.vframe\s*\{[^\}]*?\}', new_vframe, content, count=1)
    content = re.sub(r'\.vfooter\s*\{[^\}]*?\}', new_vfooter, content, count=1)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated deportes.html bulletproof landscape CSS successfully.")

if __name__ == "__main__":
    fix_deportes_landscape_css()
